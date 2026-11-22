#!/usr/bin/env python3
"""
Fit a fast per-member emulator of the temperature the game will show, so that the app can give
players an estimate of the warming (with uncertainty) from their choices without running FaIR.

Run once offline (after precompute_configs.py):
    python precompute_estimates.py

Produces: data/estimate_emulator.csv  (config_id, a_Y, b_Y for every Y in TARGET_YEARS)
          figures/estimate_emulator_diagnostics.png

MODEL
-----
For every screened member i and target year Y in TARGET_YEARS:

    T_i(Y) = a_i,Y + b_i,Y * C_Y

where T_i(Y) is the FaIR annual-mean temperature of year Y (mean of timebounds Y and Y+1,
°C re. 1850-1900, the seeded stochastic run used in the game) and C_Y is the cumulative game
CO2 FFI emission FIRST_OVERRIDE_YEAR (2023)..Y in 1000 GtCO2.

TARGET YEARS
------------
Every year 2030-2049 and 2090-2109, so that the app can form multi-year means instead of
showing single years, which carry the member's internal variability:
- 2031-2040: the trailing mean that players "observe" (Bayes update 1),
- 2030-2049: the 20-year mean centred on 2040 used to judge the Paris thresholds
  (IPCC AR6 defines warming levels as 20-year means),
- 2090-2109: the 20-year mean centred on 2100, the end-of-century estimate.
A 20-year mean centred on Y.0 covers annual years Y-10..Y+9 (mid-points Y-9.5..Y+9.5).

WHY LINEAR IN CUMULATIVE CO2
----------------------------
All non-CO2 species follow SSP2-4.5 and only the global CO2 FFI total is changed, so the
decisions only enter through the global CO2 pathway. Warming is close to proportional to
cumulative CO2 (TCRE), and intercept a_i carries everything that does not depend on the
decisions (warming already realised, committed warming, SSP2-4.5 non-CO2). Because it is fitted
per member, the correlation between the baseline and the CO2 response (both scale with the
member's climate sensitivity) is kept, which a separate baseline + TCRE would lose.
The same seeded internal variability is used in every run, so the single-year temperature
noise is part of a_i and does not blur the fit.

TRAINING DECISIONS
------------------
Phase 1 style (no net-zero year: pledges are extrapolated after 2040) and Phase 2 style
(random net-zero year per region), with random cuts. The fit is checked with leave-one-
scenario-out cross-validation; the RMS error should be well below the ensemble spread (~0.3-0.7 °C).
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import fair_runner as fr

N_SCENARIOS_EACH = 15       # 15 Phase 1 style + 15 Phase 2 style decision sets
TARGET_YEARS = tuple(range(2030, 2050)) + tuple(range(2090, 2110))
DIAGNOSTIC_YEARS = (2040, 2100)   # years shown in the diagnostics figure (all are printed)
RUN_END = max(TARGET_YEARS) + 1   # last timebound needed: annual mean of Y needs timebound Y+1
# Cut range spans the radio options (India Passiivinen = -80 %, i.e. +80 % growth) up to the
# strongest pledges (-90 %). Net-zero years span the slider/radio range (2041..~2240).
CUT_RANGE = (-0.8, 0.95)
NETZERO_RANGE = (fr.CHECKPOINT_YEAR + 1, fr.CHECKPOINT_YEAR + 200)
SEED = 0
OUT_FIG = fr._HERE / 'figures' / 'estimate_emulator_diagnostics.png'


def draw_decisions(rng, with_netzero: bool):
    regions = list(fr.REGION_EMISSIONS_BASE_GTCO2)
    cuts = {r: rng.uniform(*CUT_RANGE) for r in regions}
    if not with_netzero:
        return cuts, None
    netzero_years = {r: int(rng.integers(NETZERO_RANGE[0], NETZERO_RANGE[1] + 1)) for r in regions}
    return cuts, netzero_years


def run_members(cuts, netzero_years, config_ids):
    """Temperature at the target years for all members. Returns {year: array(n_members)}."""
    f = fr.setup_fair(config_ids, RUN_END)
    trajectory = fr.build_co2_fossil_trajectory(cuts, netzero_years, RUN_END)
    co2_idx = list(f.emissions.specie.values).index('CO2 FFI')
    f.emissions.values[fr.FIRST_OVERRIDE_YEAR - 1750:, 0, :, co2_idx] = trajectory[fr.FIRST_OVERRIDE_YEAR - 1750:, None]
    f.run()
    temp = f.temperature.sel(layer=0, scenario='game')
    temp = fr.rebase_to_1850_1900(temp)
    return {year: fr.annual_mean(temp, year).values for year in TARGET_YEARS}


def main(n_each=N_SCENARIOS_EACH, config_ids=None, write=True):
    rng = np.random.default_rng(SEED)
    if config_ids is None:
        config_ids = list(fr.load_screened_configs().index)

    decisions = ([draw_decisions(rng, False) for _ in range(n_each)]
                 + [draw_decisions(rng, True) for _ in range(n_each)])
    n_scen = len(decisions)

    # cumulative[Y][s] in 1000 GtCO2, temp[Y][s, i] in degC
    cumulative = {y: np.array([fr.cumulative_co2(c, nz, y) for c, nz in decisions]) / 1000.0
                  for y in TARGET_YEARS}
    temp = {y: np.zeros((n_scen, len(config_ids))) for y in TARGET_YEARS}
    for s, (cuts, netzero_years) in enumerate(decisions):
        result = run_members(cuts, netzero_years, config_ids)
        for y in TARGET_YEARS:
            temp[y][s] = result[y]
        print(f'  scenario {s + 1}/{n_scen} done', flush=True)

    coefficients = pd.DataFrame(index=pd.Index(config_ids, name='config_id'))
    fig, axes = plt.subplots(2, len(DIAGNOSTIC_YEARS), figsize=(11, 7))
    for y in TARGET_YEARS:
        x = cumulative[y]
        # Per-member least squares line T = a + b x, vectorised over members.
        slope, intercept = np.polyfit(x, temp[y], 1)
        coefficients[f'a_{y}'] = intercept
        coefficients[f'b_{y}'] = slope

        # Leave-one-scenario-out error: what the app will see for an unseen decision set.
        loo_err = np.zeros_like(temp[y])
        for s in range(n_scen):
            keep = np.arange(n_scen) != s
            sl, ic = np.polyfit(x[keep], temp[y][keep], 1)
            loo_err[s] = ic + sl * x[s] - temp[y][s]
        spread = temp[y].std(axis=1).mean()
        print(f'T{y}: cumulative CO2 range {x.min():.2f}..{x.max():.2f} (1000 GtCO2); '
              f'b median {np.median(slope):.2f} degC/1000 GtCO2 (5-95%: '
              f'{np.percentile(slope, 5):.2f}..{np.percentile(slope, 95):.2f}); '
              f'LOO RMS error {np.sqrt((loo_err ** 2).mean()):.3f} degC, max {abs(loo_err).max():.3f}; '
              f'ensemble sd within a decision set {spread:.2f} degC')

        # Sanity plots of the intermediate result: the fits and the leave-one-out errors.
        if y not in DIAGNOSTIC_YEARS:
            continue
        col = DIAGNOSTIC_YEARS.index(y)
        ax = axes[0, col]
        for i in range(0, len(config_ids), max(1, len(config_ids) // 40)):
            ax.plot(x, temp[y][:, i], '.', color='tab:blue', alpha=0.3)
        xs = np.linspace(x.min(), x.max(), 20)
        for i in range(0, len(config_ids), max(1, len(config_ids) // 40)):
            ax.plot(xs, intercept[i] + slope[i] * xs, color='k', alpha=0.15, linewidth=0.7)
        ax.set_xlabel(f'Cumulative CO2 {fr.FIRST_OVERRIDE_YEAR}..{y} (1000 GtCO2)')
        ax.set_ylabel(f'T {y}, annual mean (°C)')
        ax.set_title(f'T{y}: ~40 members, FaIR (dots) and linear fit (lines)')
        ax = axes[1, col]
        ax.hist(loo_err.ravel(), bins=60, color='tab:orange')
        ax.set_xlabel('Leave-one-scenario-out error (°C)')
        ax.set_title(f'T{y}: emulator error, RMS {np.sqrt((loo_err ** 2).mean()):.3f} °C')
    fig.tight_layout()

    if write:
        coefficients.to_csv(fr.ESTIMATE_EMULATOR_PATH)
        OUT_FIG.parent.mkdir(exist_ok=True)
        fig.savefig(OUT_FIG, dpi=130)
        print(f'Wrote {fr.ESTIMATE_EMULATOR_PATH} and {OUT_FIG}')
    return coefficients


if __name__ == '__main__':
    main()
