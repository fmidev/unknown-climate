#!/usr/bin/env python3
"""
FaIR v2.2 wrapper for the climate negotiations classroom demo.

Uses the fair-calibrate v1.6.0 constrained posterior (841 members, FaIR 2.2.4;
Smith et al. 2024, https://github.com/chrisroadmap/fair-calibrate),
vendored in data/fair_calibrate/ (see the README there). The FaIR setup follows
fair-calibrate's input/constraining/07_constrained-ssp-projections.py (tag v1.6.0).

A single config is drawn randomly from a pre-screened shortlist
(data/screened_configs.csv, produced by precompute_configs.py).
CO2 FFI (fossil fuel and industry) emissions 2023+ are replaced by the game trajectory: observed
(GCB) global totals for 2023-24, then the user-defined regional pledges from BASE_YEAR on.
CO2 AFOLU (land use) is NOT changed by the players; it follows SSP2-4.5 like all other species,
from the harmonized emissions NetCDF.

Runs are stochastic with the seeds stored in the posterior, so a given config always
reproduces the same internal variability. This is what makes the screening in
precompute_configs.py valid for the runs shown in the game.
"""
from functools import lru_cache
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
from fair import FAIR
from fair.io import read_properties
from fair.interface import fill, initialise

_HERE = Path(__file__).parent
FAIR_CAL_DIR = _HERE / 'data' / 'fair_calibrate'
POSTERIOR_PATH = FAIR_CAL_DIR / 'output' / 'posteriors' / 'calibrated_constrained_parameters.csv'
SPECIES_PROPERTIES_PATH = FAIR_CAL_DIR / 'output' / 'posteriors' / 'species_configs_properties.csv'
SCREENED_CONFIGS_PATH = _HERE / 'data' / 'screened_configs.csv'
ESTIMATE_EMULATOR_PATH = _HERE / 'data' / 'estimate_emulator.csv'
OBSERVED_GMST_PATH = _HERE / 'data' / 'IGCC_GMST_1850-2025.csv'
OBS_UNCERTAINTY_PATH = _HERE / 'data' / 'obs_uncertainty.csv'   # precompute_obs_error.py

# Base SSP for non-CO2 gases and historical CO2.
# SSP2-4.5 is "middle of the road" — reasonable as current-policy backdrop.
BASE_SSP = 'ssp245'

# Phase 1 pledge year: CO2 cuts are specified relative to this year.
# Must match CHECKPOINT in app.py.
CHECKPOINT_YEAR = 2040

# Game CO2 FFI emissions (fossil fuel + industry, GtCO2/yr). Land use (AFOLU) is not included
# and is not changed by the players.
#
# Source: Global Carbon Budget (GCB 2025 vintage, national territorial fossil CO2) as
# redistributed by Our World in Data (owid-co2-data.csv, 'co2' column). 2025 is the GCB
# projection, not a measurement. "Muu maailma" is the remainder World - (China + USA + EU27 +
# India) and so contains international aviation and shipping (~1.1 GtCO2/yr), which no country owns
# but which is part of the global CO2 FFI that FaIR needs.
# Why this vintage: the world total (38.14 GtCO2 in 2023) is within 0.6 GtCO2 of the SSP2-4.5
# CEDS series FaIR was calibrated with (38.71), so the game trajectory joins the historical record
# without a step (SSP2-4.5 2022: 38.09 -> game 2023: 38.14).

# First year with regional resolution. Pledged cuts are relative to this year, and the linear
# ramp to CHECKPOINT_YEAR starts here. 2025 is the latest year GCB has (a projection).
BASE_YEAR = 2025

# Global CO2 FFI for the years between the SSP2-4.5 historical record (ends 2022) and BASE_YEAR.
HISTORICAL_CO2_FFI_GTCO2 = {
    2023: 38.14,
    2024: 38.65,
}

REGION_EMISSIONS_BASE_GTCO2 = {
    'Kiina 🇨🇳':      12.42,
    'USA 🇺🇸':         5.04,
    'EU 🇪🇺':          2.41,
    'Intia 🇮🇳':       3.20,
    'Muu maailma 🌍': 15.93,
}

# First year of the emissions array that the game overrides (CO2 FFI before this year is SSP2-4.5).
FIRST_OVERRIDE_YEAR = min(HISTORICAL_CO2_FFI_GTCO2)


@lru_cache(maxsize=1)
def load_posterior() -> pd.DataFrame:
    """The 841 calibrated, constrained posterior members (rows) and their parameters."""
    return pd.read_csv(POSTERIOR_PATH, index_col=0)


def load_screened_configs() -> pd.DataFrame:
    """Load the pre-screened config shortlist produced by precompute_configs.py."""
    if not SCREENED_CONFIGS_PATH.exists():
        raise FileNotFoundError(
            f'{SCREENED_CONFIGS_PATH} not found. Run precompute_configs.py first.'
        )
    return pd.read_csv(SCREENED_CONFIGS_PATH, index_col='config_id')


def load_observed_gmst() -> pd.DataFrame:
    """
    Load the IGCC observed annual GMST series, 1850–2025 (IGCC-2025a release, Zenodo 10.5281/
    zenodo.21494229, `global_mean_temperatures/annual_averages.csv`), relative to 1850–1900.

    The posterior was calibrated against the earlier 1850–2024 IGCC vintage (still vendored in
    data/fair_calibrate/data/forcing/). The two vintages differ by -0.009 °C on average
    (max |0.044| °C), which is small compared with the screening limit of ~0.25 °C.

    Returns a DataFrame with columns 'year' (float, mid-year: 1850.5 ... 2025.5) and 'gmst' (°C).
    """
    df = pd.read_csv(OBSERVED_GMST_PATH)
    return df[['year', 'gmst']]


def load_obs_uncertainty() -> pd.Series:
    """
    95 % half-width (°C) of annual GMST relative to 1850–1900, from the HadCRUT5 ensemble
    (see precompute_obs_error.py). Index: calendar year (int, 1850 ... 2025).
    """
    df = pd.read_csv(OBS_UNCERTAINTY_PATH)
    return df.set_index('year')['half_width_95']


def rebase_to_1850_1900(temp: xr.DataArray) -> xr.DataArray:
    """
    Express temperature relative to the 1850–1900 mean, exactly as the calibration does.

    FaIR temperature sits on timebounds (1 January of each year). The mean of the annual
    means 1850–1900 equals the mean of timebounds 1850…1901 with half weight on the two
    end points.
    """
    base = temp.sel(timebounds=slice(1850, 1901))
    weights = np.ones(base.sizes['timebounds'])
    weights[0] = 0.5
    weights[-1] = 0.5
    weights = xr.DataArray(weights, coords={'timebounds': base.timebounds})
    baseline = base.weighted(weights).mean(dim='timebounds')
    return temp - baseline


def annual_mean(temp: xr.DataArray, year: int) -> xr.DataArray:
    """
    Annual mean temperature of `year`: the average of timebounds `year` and `year + 1`.

    Observations are annual means stamped at mid-year, so the observation for year Y
    corresponds to this quantity, not to the timebound `Y` (1 January of Y).
    """
    return 0.5 * (temp.sel(timebounds=year) + temp.sel(timebounds=year + 1))


def annual_series(temp: xr.DataArray) -> xr.DataArray:
    """
    Annual means of every complete year of a timebounds series, on a new integer dim 'year'.

    Year Y is the mean of timebounds Y and Y+1 (see annual_mean), so a run whose last timebound
    is E gives annual means up to year E-1. Everything the game shows or uses is an annual mean;
    plot it at mid-year (Y + 0.5) to line up with the IGCC observations.
    """
    values = 0.5 * (temp.isel(timebounds=slice(None, -1)).values
                    + temp.isel(timebounds=slice(1, None)).values)
    years = temp.timebounds.values[:-1].astype(int)
    return xr.DataArray(values, coords={'year': years}, dims=['year'])


def extrapolate_after_checkpoint(em_base: float, em_chk: float, years: np.ndarray) -> np.ndarray:
    """
    Regional CO2 emissions (GtCO₂/yr) after CHECKPOINT_YEAR when no net-zero year is chosen
    ("current policy" extrapolation).

    The absolute annual change of the BASE_YEAR–CHECKPOINT_YEAR pledge ramp (GtCO₂/yr per year) is
    continued, so a region that cuts keeps cutting at the same pace until it reaches zero
    (floor at zero, no negative emissions). A linear rather than a fractional-rate extrapolation
    is used so that emissions can reach zero. A region whose emissions grow to the checkpoint
    stays flat afterwards: continuing growth to 2100 would be an extrapolation of BAU growth
    well beyond the pledge period.
    """
    slope = (em_chk - em_base) / float(CHECKPOINT_YEAR - BASE_YEAR)
    slope = min(slope, 0.0)
    return np.maximum(0.0, em_chk + slope * (np.asarray(years) - CHECKPOINT_YEAR))


def build_co2_fossil_trajectory(cuts: dict, netzero_years: dict | None, year_end: int) -> np.ndarray:
    """
    Build a global annual CO2 FFI emission time series (GtCO₂/yr) from 1750 to year_end.

    1750–2022: zeros here — caller leaves the SSP2-4.5 historical values intact.
    2023–(BASE_YEAR−1): observed global totals (HISTORICAL_CO2_FFI_GTCO2), the same for all players.
    BASE_YEAR–CHECKPOINT_YEAR: each region ramps linearly from its BASE_YEAR level to
    (1−cut)×level.
    CHECKPOINT_YEAR–netzero_year: each region ramps linearly from its checkpoint level to zero.
    After netzero_year: zero (no CDR).
    If no netzero year is given for a region: its BASE_YEAR–CHECKPOINT_YEAR annual change is
    extrapolated (see extrapolate_after_checkpoint).

    Parameters
    ----------
    cuts : dict
        {region: fraction_cut} where fraction_cut ∈ [0, 1].
    netzero_years : dict or None
        {region: year} for Phase 2; None keeps each region at its checkpoint level.
    year_end : int
        Last year of the FaIR run.

    Returns
    -------
    trajectory : ndarray, shape (year_end − 1750,)
        Timepoints-aligned global CO2 FFI in GtCO₂/yr — same unit as the
        harmonized SSP NetCDF that FaIR's parameters were calibrated against.
        Indices 0…(FIRST_OVERRIDE_YEAR−1−1750) are zero and will be overwritten by SSP data.
    """
    years = np.arange(1750, year_end)
    trajectory = np.zeros(len(years))

    for year, total in HISTORICAL_CO2_FFI_GTCO2.items():
        trajectory[year - 1750] = total

    for region, base_gtco2 in REGION_EMISSIONS_BASE_GTCO2.items():
        cut     = cuts.get(region, 0.0)
        em_base = base_gtco2                    # GtCO₂/yr in BASE_YEAR
        em_chk  = base_gtco2 * (1.0 - cut)     # GtCO₂/yr at CHECKPOINT_YEAR

        # BASE_YEAR → CHECKPOINT_YEAR: linear ramp
        mask1 = (years >= BASE_YEAR) & (years < CHECKPOINT_YEAR)
        t1 = (years[mask1] - BASE_YEAR) / float(CHECKPOINT_YEAR - BASE_YEAR)
        trajectory[mask1] += em_base + t1 * (em_chk - em_base)

        nz = (netzero_years or {}).get(region)
        if nz and nz > CHECKPOINT_YEAR:
            # CHECKPOINT_YEAR → netzero_year: linear decline to zero
            mask2 = (years >= CHECKPOINT_YEAR) & (years < nz)
            t2 = (years[mask2] - CHECKPOINT_YEAR) / float(nz - CHECKPOINT_YEAR)
            trajectory[mask2] += em_chk * (1.0 - t2)
            # after netzero_year: zero (no CDR)
        else:
            mask2 = years >= CHECKPOINT_YEAR
            trajectory[mask2] += extrapolate_after_checkpoint(em_base, em_chk, years[mask2])

    return trajectory


def regional_emissions_in_year(cuts: dict, year: int) -> dict:
    """Extrapolated (no net-zero chosen) emissions of each region in `year` >= CHECKPOINT_YEAR, GtCO₂/yr."""
    emissions = {}
    for region, em_base in REGION_EMISSIONS_BASE_GTCO2.items():
        em_chk = em_base * (1.0 - cuts.get(region, 0.0))
        emissions[region] = float(extrapolate_after_checkpoint(em_base, em_chk, [year])[0])
    return emissions


def cumulative_co2(cuts: dict, netzero_years: dict | None, temperature_year: int) -> float:
    """
    Cumulative game CO2 FFI emissions (GtCO₂) from FIRST_OVERRIDE_YEAR up to and including
    temperature_year.

    The game temperature of year Y is the annual mean, i.e. the mean of timebounds Y and Y+1.
    FaIR timebound Y+1 (1 Jan) is driven by the emissions up to and including year Y, so the
    emissions of year Y are counted.
    """
    trajectory = build_co2_fossil_trajectory(cuts, netzero_years, temperature_year + 1)
    return float(trajectory[FIRST_OVERRIDE_YEAR - 1750:].sum())


@lru_cache(maxsize=1)
def load_estimate_emulator() -> pd.DataFrame:
    """
    Per-member linear emulator written by precompute_estimates.py:
    T_year = a_year + b_year * (cumulative CO2 FIRST_OVERRIDE_YEAR..year in 1000 GtCO₂), where
    T_year is the annual mean of `year` and year is one of precompute_estimates.TARGET_YEARS.
    """
    if not ESTIMATE_EMULATOR_PATH.exists():
        raise FileNotFoundError(
            f'{ESTIMATE_EMULATOR_PATH} not found. Run precompute_estimates.py first.'
        )
    return pd.read_csv(ESTIMATE_EMULATOR_PATH, index_col='config_id')


def posterior_weights(reference_temperature: pd.Series, observation: float, sigma: float) -> pd.Series:
    """
    Weights of the screened members after a noisy observation of the drawn member.

    The player is told only `observation` = (drawn member's reference temperature) + N(0, sigma).
    With the member drawn uniformly from the screened ensemble, Bayes' rule gives each member the
    weight exp(-(T_ref,i - observation)^2 / (2 sigma^2)). Weighted means and intervals of any
    member property (temperature under other decisions, ECS) are then calibrated, and quantities
    that correlate with the reference temperature (ECS) narrow consistently.
    """
    weights = np.exp(-0.5 * ((reference_temperature - observation) / sigma) ** 2)
    return weights / weights.sum()


def weighted_mean_interval(values: pd.Series, weights: pd.Series, level: float = 0.95):
    """Weighted mean and central `level` interval of values (aligned to weights' index)."""
    values = values.loc[weights.index]
    order = np.argsort(values.values)
    sorted_values = values.values[order]
    sorted_weights = weights.values[order]
    # Mid-point cumulative weights, so that equal weights reproduce the usual interpolated quantile.
    cumulative = (np.cumsum(sorted_weights) - 0.5 * sorted_weights) / sorted_weights.sum()
    lower, upper = (1.0 - level) / 2.0, 1.0 - (1.0 - level) / 2.0
    interval = np.interp([lower, upper], cumulative, sorted_values)
    mean = float(np.average(values.values, weights=weights.values))
    return mean, float(interval[0]), float(interval[1])


def emulate_temperature(cuts: dict, netzero_years: dict | None, year: int) -> pd.Series:
    """
    Fast (no FaIR) temperature estimate (°C re. 1850–1900, annual mean of `year`) for every
    screened member, indexed by config_id.
    """
    emulator = load_estimate_emulator()
    cum_tco2 = cumulative_co2(cuts, netzero_years, year) / 1000.0
    return emulator[f'a_{year}'] + emulator[f'b_{year}'] * cum_tco2


def setup_fair(config_ids, year_end: int, base_ssp: str = BASE_SSP) -> FAIR:
    """
    Configure a FaIR instance for the given posterior members (not yet run).

    Follows fair-calibrate v1.6.0 input/constraining/07_constrained-ssp-projections.py:
    the same species (Irrigation removed, land-use forcing calculated), harmonized SSP
    emissions, scaled solar and volcanic forcing, posterior parameters and initial
    conditions. Differences: only the given members, one scenario (named 'game', with the
    emissions of base_ssp; the caller may overwrite CO2 FFI) and a variable end year.
    Runs are stochastic with each member's stored seed.

    Parameters
    ----------
    config_ids : sequence of int
        Index values of data/fair_calibrate/.../calibrated_constrained_parameters.csv.
    year_end : int
        Last timebound of the run (timebounds are 1 January of 1750 … year_end).
    """
    config_ids = list(config_ids)
    df_configs = load_posterior().loc[config_ids]
    nyears = year_end - 1750 + 1   # number of timebounds

    # Solar ERF is relative to 1850–2019 and volcanic ERF to 1850–2021, matching the
    # baselines used when the posterior forcing scales were calibrated.
    df_solar = pd.read_csv(
        FAIR_CAL_DIR / 'output' / 'forcing' / 'solar_forcing_timebounds_cmip7.csv', index_col=0)
    df_volcanic = pd.read_csv(
        FAIR_CAL_DIR / 'data' / 'forcing' / 'volcanic_forcing_timebounds_cmip7.csv', index_col=0)
    solar_forcing = df_solar['solar_erf_rel_1850-2019'].loc[1750:year_end].values
    volcanic_forcing = df_volcanic['volcanic_erf_rel_1850-2021'].loc[1750:year_end].values

    f = FAIR(ch4_method='Thornhill2021')
    f.define_time(1750, year_end, 1)
    f.define_scenarios(['game'])
    f.define_configs(config_ids)

    species, properties = read_properties(SPECIES_PROPERTIES_PATH)
    species.remove('Irrigation')
    # Land use forcing is derived from cumulative CO2 AFOLU emissions
    properties['Land use']['input_mode'] = 'calculated'
    f.define_species(species, properties)
    f.allocate()

    # Harmonized emissions of base_ssp as the base for all species
    da_emissions = xr.load_dataarray(
        FAIR_CAL_DIR / 'output' / 'emissions' / 'ssps_harmonized_1750-2499.nc')
    da = da_emissions.loc[
        dict(config='unspecified', scenario=[base_ssp], specie=species)][:nyears - 1, ...]
    fe = da.expand_dims(dim=['config'], axis=(2))
    f.emissions = fe.drop_vars('config') * np.ones((1, 1, len(config_ids), 1))
    f.emissions.coords['config'] = f.configs
    f.emissions = f.emissions.assign_coords(scenario=['game'])

    fill(f.forcing,
         volcanic_forcing[:, None, None] * df_configs['forcing_scale[Volcanic]'].values.squeeze(),
         specie='Volcanic')
    fill(f.forcing,
         solar_forcing[:, None, None] * df_configs['forcing_scale[Solar]'].values.squeeze(),
         specie='Solar')

    # Species defaults first, then the full posterior parameter set (climate response, carbon
    # cycle, aerosols, ozone, forcing scales, seeds, stochastic_run=True ...) on top.
    f.fill_species_configs(SPECIES_PROPERTIES_PATH)
    f.override_defaults(POSTERIOR_PATH)

    initialise(f.concentration, f.species_configs['baseline_concentration'])
    initialise(f.forcing, 0)
    initialise(f.temperature, 0)
    initialise(f.cumulative_emissions, 0)
    initialise(f.airborne_emissions, 0)

    return f


def run_fair_game(cuts: dict, netzero_years: dict | None, config_id: int) -> xr.DataArray:
    """
    Set up and run a single-config seeded stochastic FaIR run for the classroom game.

    Parameters
    ----------
    cuts : dict
        {region: fraction_cut} where fraction_cut ∈ [0, 1].
    netzero_years : dict or None
        {region: year} for Phase 2 net-zero dates; None extrapolates each region's
        BASE_YEAR–CHECKPOINT_YEAR annual change (see extrapolate_after_checkpoint).
    config_id : int
        Index value from data/screened_configs.csv / the calibrated posterior.

    Returns
    -------
    temp : xr.DataArray
        Surface temperature anomaly (°C re. 1850–1900 mean) on timebounds, dim (timebounds,).
    """
    # Give the model enough runway to capture peak temperature after net-zero.
    # High-ECS configs take 80–120 years post-net-zero to reach their maximum.
    # The cap keeps the run length (and the app's response time) bounded.
    _YEAR_END_DEFAULT = 2150
    _YEAR_END_MAX = 2300
    _POST_NETZERO_BUFFER = 150
    if netzero_years:
        latest_nz = max(netzero_years.values())
        year_end = min(max(_YEAR_END_DEFAULT, latest_nz + _POST_NETZERO_BUFFER), _YEAR_END_MAX)
    else:
        year_end = _YEAR_END_DEFAULT

    f = setup_fair([config_id], year_end, base_ssp=BASE_SSP)

    # Overwrite CO2 FFI from FIRST_OVERRIDE_YEAR onwards with the game trajectory.
    # dims of f.emissions: (timepoints, scenario, config, specie)
    game_co2 = build_co2_fossil_trajectory(cuts, netzero_years, year_end)
    co2_idx  = list(f.emissions.specie.values).index('CO2 FFI')
    f.emissions.values[FIRST_OVERRIDE_YEAR - 1750:, 0, 0, co2_idx] = game_co2[FIRST_OVERRIDE_YEAR - 1750:]

    f.run()

    temp = f.temperature.sel(layer=0, scenario='game', config=config_id)
    return rebase_to_1850_1900(temp)


def run_fair_ssp(ssp_name: str, config_id: int, year_end: int = 2100) -> xr.DataArray:
    """
    Run a seeded stochastic FaIR simulation using a pre-defined SSP scenario without
    any custom CO2 override (all emissions taken directly from the SSP NetCDF).

    Parameters
    ----------
    ssp_name : str
        SSP scenario key as it appears in the harmonized emissions file,
        e.g. 'ssp119', 'ssp245', 'ssp370', 'ssp585'.
    config_id : int
        Index value from data/screened_configs.csv / the calibrated posterior.
    year_end : int
        Last year of the FaIR run (default 2100).

    Returns
    -------
    temp : xr.DataArray
        Surface temperature anomaly (°C re. 1850–1900 mean), dim (timebounds,).
    """
    f = setup_fair([config_id], year_end, base_ssp=ssp_name)
    f.run()

    temp = f.temperature.sel(layer=0, scenario='game', config=config_id)
    return rebase_to_1850_1900(temp)
