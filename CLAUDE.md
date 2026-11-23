# Tuntematon ilmasto (Unknown Climate) — Project Notes for Claude

## What this is

A Streamlit classroom app for a climate negotiation role-play led by a teacher or other
presenter, for players from grade 7 upwards, including adults (younger players need more
help from the presenter).
Run with `streamlit run app.py`; instructor slider mode by opening the URL with `?mode=sliders`.
Pinned pip dependencies in `requirements.txt` (used by Streamlit Cloud); conda dev env in
`environment-dev.yml` (Python 3.11, FaIR 2.2). UI in Finnish and English: the language is
chosen on the first page and can be switched at any time (FI/EN switch at the top right).

## Publishing and deployment

Status: beta. Live at https://unknown-climate.streamlit.app/ on Streamlit Community Cloud, shared
with invited reviewers before the public launch (`v1.0.0`; beta tag `v1.0.0-beta.1`). Open
publishing tasks are tracked in `TODO.md` (untracked, local only).

- Repositories: `fmidev/unknown-climate` is the main public repo (code, issues, credits).
  The app deploys from the fork `aipartanen/unknown-climate`, because the author has no admin
  rights on fmidev. Local remotes: `origin` = fmidev, `personal` = fork.
- **Every push to the fork's `main` goes live.** `git push origin main` saves work without
  touching the app; push to `personal` only when a change is tested and meant to be released.
  Never push to `personal` unless asked.
- Dependencies: `requirements.txt` (pinned, pip) is what Streamlit Cloud installs; Python 3.11.
  Add new dependencies there (pinned) and to `environment-dev.yml`. Pin transitive packages
  when a new release breaks the app: `starlette==1.3.1` is pinned (first release without the
  advisories of 1.0.0) because newer starlette breaks Streamlit 1.57's file serving (1.9: static
  files fail, 1.10: `st.pyplot` images return HTTP 500).
- Test changes to dependencies with a clean pip venv from a fresh clone, and click through a whole
  game checking that matplotlib images load (not only page headings).

When developing new features, keep them compatible with Streamlit Community Cloud:
- Avoid local file paths that would break in a cloud environment
- Keep dependencies on PyPI (pip-installable), not just conda-forge
- If adding precomputed data files, they must be committable to git or generatable on startup
- No secrets or credentials hardcoded; use environment variables or Streamlit secrets
  (`st.secrets`). The app currently needs none.
- The app should start cleanly with `streamlit run app.py` from a fresh clone
- Instructor options go in URL parameters (`st.query_params`), since script arguments cannot be
  passed on Streamlit Cloud

## Pipeline

- `precompute_configs.py` — screens FaIR ensemble members, generates `data/screened_configs.csv`
  (rule and rationale are documented in the script header)
- `fair_runner.py` — FaIR v2.2 wrapper used by the app (also used by the screening, so the
  seeded stochastic runs shown in the game are the ones that were screened)
- `precompute_estimates.py` — fits a per-member linear emulator (T = a + b·cumulative CO₂ FFI) of
  the annual-mean temperature for every year 2030–2049 and 2090–2109, writes `data/estimate_emulator.csv`.
  Gives the app ensemble estimates without running FaIR. Re-run (~5 min) after any change to the
  emissions setup, screening or targets; run `precompute_configs.py` first.
- `precompute_obs_error.py` — 95 % observational uncertainty of annual GMST vs 1850–1900 from the
  HadCRUT5 200-member ensemble (Morice et al. 2021; raw file in gitignored `data/raw/`), writes
  `data/obs_uncertainty.csv`. Chart band only (around observations and the whole drawn-climate
  line, recent ±0.084 °C after 2024); it does not enter the Bayes updates. Noisy observations are never plotted.
- `app.py` — Streamlit UI (main entry point)
- `texts.py` — all user-visible text in both languages (`t('key', ...)`)
- `make_presentation_figure.py` — standalone figure generation utility
- `docs/observational_uncertainty_options.md` — design notes on observational uncertainty (option A, the band, is implemented; option B is open)
- `README.md` (setup, caveats, privacy), `CREDITS.md` (sources and licences), `LICENSE` (MIT)

## App structure

Eight screens in order (`SCREENS` in `app.py`): pledges → prior → draw → simulation 2040 →
observation 2040 → research → net-zero years (Phase 2) → reveal. The impacts page opens on top of
any screen. Pledges lock once a member is drawn (the observation depends on them).

The game is about uncertainty: one screened member is drawn uniformly and its ECS stays hidden until
the reveal. Estimates are the ensemble reweighted by Bayes (`posterior_weights`); the scientific
choices are commented by the constants in `app.py` (`OBS_WINDOW`, `OBS_2040_SD`, `ECS_CLUE_SD`,
`CENTRED_WINDOW`). In short:
- Update 1: observed 2031–2040 mean, noise SD 0.05 °C. Member internal variability is not added
  (it is part of the member's identity, fixed seed). Usually narrows ECS only ~20 %.
- Update 2: research estimate of ECS, noise SD 0.5 °C. Weights of the two updates multiply.
- Both noise draws happen once per game (at the first simulation), so revisiting screens cannot
  average them away.
- Long-term warming is always a 20-year mean centred on Y.0 (annual years Y−10…Y+9,
  `LONG_TERM_YEARS`, `_centred_window()`), as IPCC AR6 warming levels; single years are shown
  only to contrast with it.
- Paris verdict at 2040 uses the 20-year mean centred on 2040 (2030–2049): known years 2030–2040
  plus 2041–2049 projected with the combined update-1 × update-2 weights (both exist at the end of
  2040 in the story; the prior is clearly less accurate, research alone too).
- Phase 2 verdict: peak of the 20-year centred mean of the drawn member's run after 2040.
- End-of-century estimate (histogram, reveal, impacts page) = 2090–2109 mean (`ESTIMATE_WINDOW`).
  Exceedance probabilities (1.5/2/3/4 °C) are sums of the current weights.

## Scientific conventions

- Temperature anomalies relative to 1850–1900 baseline
- CO₂ emissions in GtCO₂/yr
- FaIR 2.2.4 with the fair-calibrate v1.6.0 constrained posterior (841 members), vendored in
  `data/fair_calibrate/` (copied from ghgbudgets). The SSP emissions file is trimmed to ssp119 +
  ssp245 (IIASA SSP Database licence); do not re-add other scenarios. Sources and licences:
  `CREDITS.md` (MIT © Finnish Meteorological Institute for code and derived data).
- FaIR temperature is on timebounds (1 Jan); IGCC observations are annual means at mid-year.
  Annual mean of year Y = mean of timebounds Y and Y+1. Everything the game shows or uses is an
  annual mean (`annual_series()` / `annual_mean()` in `fair_runner.py`), plotted at mid-year
  (Y + 0.5). `cumulative_co2` sums emissions through year Y, since timebound Y+1 depends on them.
- Observations: IGCC-2025a annual GMST 1850–2025 in `data/IGCC_GMST_1850-2025.csv` (Zenodo
  10.5281/zenodo.21494229). The calibration used the earlier 1850–2024 vintage (differs by ~0.01 °C).
- Players set only fossil CO₂ (CO₂ FFI). Land-use CO₂ (AFOLU) and all other species follow SSP2-4.5.
  CO₂ FFI: SSP2-4.5 to 2022, observed global totals for 2023–24 (GCB via OWID), regional baselines
  for 2025 (`REGION_EMISSIONS_BASE_GTCO2`, GCB 2025 projection), pledge ramp 2025→2040.
- Screening (continuity with observations after 2025): keep members whose seeded stochastic 2026
  annual mean is within the 90th percentile of the historical misfit (≈0.25 °C) of the observed
  2023–25 mean (IGCC). No ECS trim.

## UI conventions

- Light theme pinned in `.streamlit/config.toml` (projector readability). Matplotlib charts use
  `CHART_BG`/`CHART_FG`; level colours get darker shades for text via `TEXT_SHADE`.
- Two languages (`st.session_state['lang']`, 'fi' / 'en'). Never hard-code displayed text:
  prose goes in `texts.py` as `{'fi': ..., 'en': ...}` and is shown with `t('key', name=value)`
  (str.format placeholders; an import-time check fails if a language is missing). Labels of the
  data tables in `app.py` (`EMISSION_OPTIONS` levels, `NETZERO_OFFSETS`, `TEMP_ANNOTATIONS`,
  `IMPACTS`, `SCREEN_TITLES`, `STAGE_STYLE`) are inline `{'fi', 'en'}` dicts read with `tr()`.
- Region IDs are the Finnish names (keys of `REGION_EMISSIONS_BASE_GTCO2`); display them with
  `_region_name()` / `_plain_name()`. Widget keys use the ID, so switching language keeps choices.
- Numbers follow the language (decimal comma in Finnish, point in English; `15 %` vs `15%`):
  `_num()` for text, `_pct()` for percentages, `NUM_TICKS` for matplotlib, a `labelExpr` for
  Altair axes. `make_presentation_figure.py` is standalone and stays Finnish.
- The temperature chart is Altair (`_temperature_chart`), animated by redrawing it in a placeholder
  once per result. Do not reintroduce `st.components.v1.html` (deprecated).
- Slider mode shows the 2025→2040 change in emissions (same sign as the radio labels), range
  −100…+80 %; internally the cut fraction is still used.
