# fair-calibrate v1.6.0 files used by the game

Files from [fair-calibrate](https://github.com/chrisroadmap/fair-calibrate) v1.6.0, the calibrated
and constrained parameter set for FaIR 2.2.4 by Chris Smith and co-authors (Smith et al. 2024,
<https://doi.org/10.5194/gmd-17-8569-2024>; calibration data on Zenodo,
<https://doi.org/10.5281/zenodo.7112539>). Only the files the game needs are kept.

| File | Used for |
|---|---|
| `output/posteriors/calibrated_constrained_parameters.csv` | 841 constrained posterior members (climate response, carbon cycle, aerosols, forcing scales, seeds) |
| `output/posteriors/species_configs_properties.csv` | species list, FaIR species properties and defaults (incl. baseline emissions) |
| `output/emissions/ssps_harmonized_1750-2499.nc` | harmonized SSP emissions, ssp119 and ssp245 only (SSP2-4.5 is the game's backdrop) |
| `output/forcing/solar_forcing_timebounds_cmip7.csv` | solar ERF relative to 1850-2019 |
| `data/forcing/volcanic_forcing_timebounds_cmip7.csv` | volcanic ERF relative to 1850-2021 |
| `data/forcing/IGCC_GMST_1850-2024.csv` | observed annual GMST (IGCC), stamped at mid-year (1850.5 ... 2024.5); the observation the calibration was constrained against. No longer read by the game, which uses `data/IGCC_GMST_1850-2025.csv` (IGCC-2025a, differs by ~0.01 °C on average) |

`ssps_harmonized_1750-2499.nc` is trimmed to the scenarios ssp119 and ssp245 (values unchanged;
ssp245 also carries the 1750–2022 history). The game uses ssp245 and `make_presentation_figure.py`
uses ssp119. The SSP Database licence (IIASA) does not allow redistributing a substantial portion
of the data, so the other scenarios are left out. See `CREDITS.md` for sources and licences.
