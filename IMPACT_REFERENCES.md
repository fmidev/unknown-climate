# Impact references

Climate impacts that the game can show per global warming level (1.5, 2, 3 and 4 °C), with
English and Finnish wording and their sources. This file is the basis for `IMPACTS`,
`TEMP_ANNOTATIONS`, the source line `imp_sources` in `texts.py` and the impact references in
`CREDITS.md`.

## Rules

- **Warming levels** are global mean surface temperature above 1850–1900, as in the game.
- **Only values the source itself gives at a warming level.** A value between two levels that
  the same source states may be interpolated; these are marked (i). No extrapolation beyond
  the source's levels, and no conversion of an emission scenario and period into a warming
  level by us.
- **"—"** means the source gives nothing at that level. Leave the cell empty or say so in the
  game rather than filling it.
- **Rounding** is for classroom use. The exact source values are in the "Source values" lines.
- **Checked** says how the value was verified (2026-11-24): *full text* (paper, report page or
  figure read), *abstract* (abstract or summary only) or *not verified*.

Number formatting follows the game: decimal comma and `70 %` in Finnish, decimal point and
`70%` in English.

## Global

### Sea level rise by 2100 / Merenpinnan nousu vuoteen 2100

| Level | EN | FI |
|---|---|---|
| 1.5 °C | ~45 cm | ~45 cm |
| 2 °C | ~50 cm | ~50 cm |
| 3 °C | ~60 cm | ~60 cm |
| 4 °C | ~70 cm | ~70 cm |

- Source values: medians 0.44 (0.34–0.59), 0.51 (0.40–0.69), 0.61 (0.50–0.81) and
  0.70 (0.58–0.92) m, relative to 1995–2014 [2, Table 9.10].
- Note: a rise of 1 m or more by 2100 needs ice-sheet processes that the IPCC rates as low
  confidence [2]; mention it only as a possibility, not as the 4 °C value.
- Checked: full text.

### Sea level rise over the next 2000 years / Merenpinnan nousu seuraavan 2000 vuoden aikana

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 2–3 m | 2–3 m |
| 2 °C | 2–6 m | 2–6 m |
| 3 °C | 4–10 m | 4–10 m |
| 4 °C | 12–16 m | 12–16 m |

- Source values: committed rise over 2000 years for that peak warming: 2–3 m at 1.5 °C
  [3, SPM B.5.3]; 2–6, 4–10 and 12–16 m at 2, 3 and 4 °C [2]. The rise continues after that.
- Note: the game needs to say that this is over 2000 years, not by 2100.
- Checked: full text.

### Once-a-decade hottest day on land / Kerran vuosikymmenessä sattuva kuumin päivä (maalla)

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 4× as often, 1.9 °C hotter | 4× useammin, 1,9 °C kuumempi |
| 2 °C | ~6× as often, 2.6 °C hotter | ~6× useammin, 2,6 °C kuumempi |
| 3 °C | ~7–8× as often, ~4 °C hotter (i) | ~7–8× useammin, ~4 °C kuumempi (i) |
| 4 °C | ~9× as often, 5.1 °C hotter | ~9× useammin, 5,1 °C kuumempi |

- Source values: the hottest-day event that occurred once in 10 years in 1850–1900 occurs
  4.1×, 5.6× and 9.4× as often, and is 1.9, 2.6 and 5.1 °C hotter, at 1.5, 2 and 4 °C
  [3, Fig. SPM.6]. Today (≈1 °C): 2.8×, 1.2 °C. For the once-in-50-years event: 8.6×, 13.9×
  and 39.2× (2.0, 2.7 and 5.3 °C hotter).
- Note: these are hot days (daily maximum temperature), not multi-day heatwaves. 3 °C is not
  in the figure.
- Checked: full text (figure).

### Once-a-decade heaviest rain day on land / Kerran vuosikymmenessä sattuva rankin sadepäivä (maalla)

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 1.5× as often, 10% heavier | 1,5× useammin, 10 % rankempi |
| 2 °C | 1.7× as often, 14% heavier | 1,7× useammin, 14 % rankempi |
| 3 °C | ~2× as often, ~22% heavier (i) | ~2× useammin, ~22 % rankempi (i) |
| 4 °C | 2.7× as often, 30% heavier | 2,7× useammin, 30 % rankempi |

- Source values: 1.5×, 1.7× and 2.7× as often; +10.5, +14.0 and +30.2 % [3, Fig. SPM.6].
  Today: 1.3×, +6.7 %.
- Checked: full text (figure).

### Once-a-decade drought in drying regions / Kerran vuosikymmenessä sattuva kuivuus kuivuvilla alueilla

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 2× as often | 2× useammin |
| 2 °C | 2.4× as often | 2,4× useammin |
| 3 °C | ~3× as often (i) | ~3× useammin (i) |
| 4 °C | 4× as often | 4× useammin |

- Source values: agricultural and ecological drought in drying regions: 2.0×, 2.4× and 4.1×
  [3, Fig. SPM.6]. Today: 1.7×.
- Note: the hot-day, rain and drought rows come from the same figure and could be combined
  into one "extremes" row.
- Checked: full text (figure).

### Arctic Ocean ice-free in September / Jäämeri jäätön syyskuussa

| Level | EN | FI |
|---|---|---|
| 1.5 °C | once a century | kerran sadassa vuodessa |
| 2 °C | once a decade | kerran kymmenessä vuodessa |
| 3 °C | in most years | useimpina vuosina |
| 4 °C | in most years, for several months | useimpina vuosina, useita kuukausia |

- Source values: one ice-free summer per century at 1.5 °C, at least one per decade at 2 °C
  [1, SPM B.4.1]; practically ice-free in September in most years at 3 °C (medium
  confidence) and throughout several months in most years at 3–5 °C (high confidence) [2].
- Note: SR1.5 says "summer"; AR6 has low confidence in the warming level of the first
  ice-free September [2].
- Checked: full text.

### Coral reefs / Koralliriutat

| Level | EN | FI |
|---|---|---|
| 1.5 °C | a further 70–90% lost | vielä 70–90 % häviää |
| 2 °C | over 99% lost | yli 99 % häviää |
| 3 °C | — | — |
| 4 °C | — | — |

- Source values: "decline by a further 70–90%" at 1.5 °C (high confidence), ">99%" at 2 °C
  (very high confidence) [1, SPM B.4.2].
- Note: nothing is stated at 3 and 4 °C. Showing the 2 °C value at higher levels is a logical
  consequence, not a stated value.
- Checked: full text.

### Insects losing half their range / Hyönteislajit, joiden elinalue puolittuu

| Level | EN | FI |
|---|---|---|
| 1.5 °C | ~6% | ~6 % |
| 2 °C | ~18% | ~18 % |
| 3 °C | about half | noin puolet |
| 4 °C | over half (i) | yli puolet (i) |

- Source values: share of insects losing over half of their climatically determined range:
  6 % at 1.5 °C and 18 % at 2 °C [1, SPM B.3.1]; 49 % (31–65 %) at 3.2 °C [4]. The same study's
  4.5 °C run is plotted in AR6 WGII Fig. 2.8 [5], where about 74 % of invertebrates lose over
  half their range (our reading of the figure; 21-model mean without dispersal). At 4 °C the
  value lies between 49 % and 74 %, hence "over half".
- Note: the 3 °C value is for 3.2 °C. Plants and vertebrates: 8 % and 4 % at 1.5 °C, 16 % and
  8 % at 2 °C [1]; 44 % and 26 % at 3.2 °C [4].
- Checked: full text (SR1.5; accepted manuscript of [4]; figure of [5]).

Alternative row: species at very high risk of extinction / erittäin suuressa sukupuuttovaarassa
olevat lajit: up to 14 / 18 / 29 / 39 % at 1.5 / 2 / 3 / 4 °C ("3 to 14%" … "3 to 39%")
[6, SPM B.4.1]. Checked: full text. IPCC's own synthesis, but harder to explain.

### Climate tipping points likely passed / Todennäköisesti ylitetyt ilmaston keikahduspisteet

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 4: Greenland and West Antarctic ice sheets, coral reefs, abrupt permafrost thaw | 4: Grönlannin ja Länsi-Antarktiksen mannerjäätiköt, koralliriutat, ikiroudan äkillinen sulaminen |
| 2 °C | 7: also Barents Sea ice, Labrador Sea convection, mountain glaciers | 7: lisäksi Barentsinmeren jää, Labradorinmeren konvektio, vuoristojäätiköt |
| 3 °C | 8: also East Antarctic subglacial basins | 8: lisäksi Itä-Antarktiksen jäätikkösyvänteet |
| 4 °C | 13: also the Amazon rainforest, the Atlantic overturning circulation, boreal permafrost and the boreal forest | 13: lisäksi Amazonin sademetsä, Atlantin kiertoliike, pohjoinen ikirouta ja havumetsävyöhyke |

- Source values: tipping thresholds as warming levels, with a best estimate and a range [7].
  The paper calls crossing a threshold "possible" beyond its minimum and "likely" beyond its
  best estimate. The counts are ours: elements whose best estimate is at or below the level,
  out of 16, leaving out Sahel greening (2.8 °C) because it is not a harm. Best estimates used:
  1.5 °C Greenland and West Antarctic ice sheets, coral reefs, abrupt boreal permafrost thaw;
  1.6 °C Barents Sea ice; 1.8 °C Labrador Sea convection; 2.0 °C mountain glaciers; 3.0 °C East
  Antarctic subglacial basins; 3.5 °C Amazon; 4.0 °C Atlantic overturning circulation, boreal
  permafrost collapse, southern boreal forest dieback and northern boreal forest expansion.
- Note: some elements take centuries or millennia to play out (Greenland ~10 000 years), so
  "passed" means "set in motion". The uncertainty ranges are wide. The southern boreal forest
  dieback (4 °C) is the element closest to Finland.
- Checked: full text.

### Glacier ice lost by 2100 / Jäätiköiden jäästä häviää vuoteen 2100 mennessä

| Level | EN | FI |
|---|---|---|
| 1.5 °C | a quarter; half of all glaciers vanish | neljännes; puolet jäätiköistä katoaa |
| 2 °C | ~30% (i) | ~30 % (i) |
| 3 °C | ~35% (i) | ~35 % (i) |
| 4 °C | two fifths; 4 in 5 glaciers vanish | kaksi viidesosaa; 4/5 jäätiköistä katoaa |

- Source values: 26 ± 6 % of glacier mass (relative to 2015) lost at 1.5 °C and 41 ± 11 % at
  4 °C; 49 ± 9 % and 83 ± 7 % of glaciers disappear [8]. Interpolation of the mass loss uses the
  linear relation with temperature reported by the study.
- Note: the number of glaciers vanishing is not interpolated.
- Checked: abstract.

### People living where the yearly mean temperature is over 29 °C / Ihmiset, joiden asuinpaikan vuoden keskilämpötila on yli 29 °C

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 1 in 20 | joka 20. |
| 2 °C | 1 in 10 | joka 10. |
| 3 °C | 1 in 4 (i) | joka 4. (i) |
| 4 °C | 2 in 5 (i) | 2 viidestä (i) |

- Source values: share of a 9.5 billion population (SSP2, ~2070) exposed to unprecedented heat
  (mean annual temperature ≥ 29 °C): 5 % at 1.5 °C, "nearly 10 %" at 1.8 °C, 22 % at 2.7 °C,
  34 % at 3.6 °C and 45 % at 4.4 °C [9]. Today (≈1 °C): 0.9 % (62 million).
- Note: the 2 °C value is rounded from 1.8 °C. One peer-reviewed study, not an IPCC assessment.
- Checked: full text.

### River flood damage compared with 1.5 °C / Jokitulvien vahingot verrattuna 1,5 asteeseen

| Level | EN | FI |
|---|---|---|
| 1.5 °C | 1× | 1× |
| 2 °C | 1.4–2× | 1,4–2× |
| 3 °C | 2.5–3.9× | 2,5–3,9× |
| 4 °C | 4–5× | 4–5× |

- Source values: direct flood damages without adaptation "higher by 1.4 to 2 times at 2°C and
  2.5 to 3.9 times at 3°C" compared with 1.5 °C [6, SPM B.4.2]. The 4 °C value is from AR6
  WGII Chapter 4 [10].
- Checked: full text for 2 and 3 °C; 4 °C not verified (seen only in a news summary). Check
  [10] before using the 4 °C value.

## Finland

FMI's studies of Finland by warming level go up to 2 °C. Only the temperature row reaches 3 and
4 °C. For the other rows, leave 3 and 4 °C empty, or note on the impacts page that Finnish
studies by warming level go up to 2 °C (FI: "Suomea koskevat lämpenemistasotutkimukset
ulottuvat 2 asteeseen").

### Warming in Finland / Lämpötilan nousu Suomessa

| Level | EN | FI |
|---|---|---|
| 1.5 °C | ~+2.5 °C | noin +2,5 °C |
| 2 °C | ~+3 °C | noin +3 °C |
| 3 °C | ~+5 °C | noin +5 °C |
| 4 °C | ~+6.5 °C | noin +6,5 °C |

- Source values: Finland's annual mean temperature rises "about 1.6 times faster than the global
  average" [11]. The ratio is close to 2 in the early decades of the projections and converges
  towards ~1.6 on longer timescales [12]. Values above are 1.6 × the warming level, rounded.
- Note: the ratio is stated relative to global warming, so it applies at any level; the values
  are our multiplication. With a ratio of 2, the 1.5 and 2 °C values would be +3 and +4 °C.
- Checked: full text.

### A heatwave that came once a decade at 0.5 °C (around the 1980s) / Helleaalto, joka 0,5 asteen lämpenemisellä (1980-luvun tienoilla) tuli kerran vuosikymmenessä

| Level | EN | FI |
|---|---|---|
| 1.5 °C | every third summer | joka kolmas kesä |
| 2 °C | every other summer | joka toinen kesä |
| 3 °C | — | — |
| 4 °C | — | — |

- Source values: heatwaves are ≥ 3-day periods measured by a heatwave extremity index. Near
  Heinola, a heatwave occurring once in 10 years at the 0.5 °C level has an annual probability
  of about 37 % at 1.5 °C and 51 % at 2 °C [13]. Apart from Lapland, heatwaves occurring once in
  10 (100) years at 0.5 °C have annual probabilities of 50 % (> 10 %) at 2 °C [13].
- Note: "around the 1980s" is our dating of the 0.5 °C level, not from the source.
- Checked: full text.

### Heatwave days a year / Hellepäivät vuodessa

| Level | EN | FI |
|---|---|---|
| 1.5 °C | — | — |
| 2 °C | south-east: ~20 (was ~5); central Lapland: ~5 (was ~1) | Kaakkois-Suomi: ~20 (ennen ~5); Keski-Lappi: ~5 (ennen ~1) |
| 3 °C | — | — |
| 4 °C | — | — |

- Source values: from the 0.5 °C to the 2.0 °C level, the mean annual number of heatwave days
  (daily mean above 20 °C) increases from 1 to 5 in central Lapland and from 5 to 20 in
  south-eastern Finland. At 2.0 °C, heatwaves above 20 °C occur in southern Finland nearly every
  year and in most of northern Lapland about every second year [13].
- Checked: full text.

### A cold spell that came once a decade at 0.5 °C / Pakkasjakso, joka 0,5 asteen lämpenemisellä tuli kerran vuosikymmenessä

| Level | EN | FI |
|---|---|---|
| 1.5 °C | — | — |
| 2 °C | once in ~50 years | kerran noin 50 vuodessa |
| 3 °C | — | — |
| 4 °C | — | — |

- Source values: an annual maximum cold spell that occurred once in 10 years at 0.5 °C occurs
  about once in 50 years at 2.0 °C [11, citing 14]. From 0.5 to 2.0 °C, the number of cold days
  (below the 10th percentile of winter daily means at 0.5 °C) falls by 60–80 % [14].
- Checked: abstract and slides.

### Thermal winter (daily mean below 0 °C) / Terminen talvi (vuorokauden keskilämpötila alle 0 °C)

| Level | EN | FI |
|---|---|---|
| 1.5 °C | — | — |
| 2 °C | 1–2 months shorter than in 1971–2000 | 1–2 kuukautta lyhyempi kuin 1971–2000 |
| 3 °C | — | — |
| 4 °C | — | — |

- Source values: thermal winter 30–60 days shorter and thermal summer nearly 30 days longer in
  2040–2069 under RCP4.5 than in 1971–2000; the authors state that this period approximately
  corresponds to 2 °C of global warming [15].
- Note: the equivalence with 2 °C is the authors', not a warming-level analysis.
- Checked: full text (accepted manuscript).

## Chart labels (`TEMP_ANNOTATIONS`)

Candidates drawn from the rows above:

| Level | EN | FI | Row |
|---|---|---|---|
| 1.5 °C | a further 70–90% of corals lost | vielä 70–90 % koralleista häviää | Coral reefs |
| 2.0 °C | over 99% of corals lost | yli 99 % koralleista häviää | Coral reefs |
| 2.0 °C | heatwaves nearly every summer in southern Finland | helleaaltoja lähes joka kesä Etelä-Suomessa | Heatwave days |
| 3.0 °C | Arctic Ocean ice-free in most Septembers | Jäämeri jäätön useimpina syyskuina | Arctic Ocean |
| 4.0 °C | once-a-decade hottest day ~9× as often | kerran vuosikymmenessä sattuva kuumin päivä ~9× useammin | Hottest day |
| 4.0 °C | 12–16 m of sea level rise in 2000 years | 12–16 m merenpinnan nousu 2000 vuodessa | Sea level, 2000 years |

## Changes needed in the current game (`app.py` at commit `e5a0094`)

- **Sea level by 2100:** ~40 / ~50 / ~80 / ~100 cm+ → ~45 / ~50 / ~60 / ~70 cm.
- **Coral reefs:** keep 1.5 and 2 °C; 3 and 4 °C have no stated value.
- **Arctic sea ice:** "every year" at 4 °C → "in most years, for several months". Consider
  "September" instead of "summer".
- **Species:** ">35% of species" at 4 °C (a different metric, not stated at 4 °C) → "over half
  of insects", or switch the whole row to extinction risk.
- **Extreme heatwaves:** the source is about the once-a-decade hottest day, not heatwaves;
  relabel. 3 °C (~8×) is interpolated.
- **Warming in Finland:** check all four values against ~1.6 × the warming level; "+2–3 °C" at
  1.5 °C is a little low.
- **Rows with no warming-level source: remove or replace:** Helsinki winter like other cities,
  snowy winters, ski season, and reindeer herding. Replacement candidates: heatwaves, cold spells
  and thermal winter (Finland), and sea level over 2000 years, rain, drought, tipping points,
  glaciers and heat exposure (global).
- **Chart labels to remove:** "Baltic Sea no longer freezes" (2 °C, contradicted by the
  sources: the Baltic Sea is unlikely to become totally ice-free this century), "Lapland
  reindeer herding threatened" (3 °C) and "southern Finland practically snowless" (4 °C).
- **References in the game:** `imp_sources` in `texts.py`, the code comment above `IMPACTS`, the
  presentation figure and slides, `README.md` and the FMI TODO in `CREDITS.md` should cite the
  sources actually used (below), including AR6 WGII and the FMI papers.

## References

1. IPCC, 2018: Summary for Policymakers. In: *Global Warming of 1.5 °C* (SR1.5).
   doi:10.1017/9781009157940.001. <https://www.ipcc.ch/sr15/chapter/spm/>
2. Fox-Kemper, B. et al., 2021: Ocean, Cryosphere and Sea Level Change. In: *Climate Change
   2021: The Physical Science Basis* (AR6 WGI), Chapter 9.
   <https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-9/>
3. IPCC, 2021: Summary for Policymakers. In: *Climate Change 2021: The Physical Science Basis*
   (AR6 WGI). Figure SPM.6:
   <https://www.ipcc.ch/report/ar6/wg1/figures/summary-for-policymakers/figure-spm-6/>
4. Warren, R., Price, J., Graham, E., Forstenhaeusler, N. and VanDerWal, J., 2018: The
   projected effect on insects, vertebrates, and plants of limiting global warming to 1.5 °C
   rather than 2 °C. *Science* 360, 791–795. doi:10.1126/science.aar3646.
   Accepted manuscript: <https://core.ac.uk/download/159073638.pdf>
5. Parmesan, C. et al., 2022: Terrestrial and Freshwater Ecosystems and Their Services. In:
   *Climate Change 2022: Impacts, Adaptation and Vulnerability* (AR6 WGII), Chapter 2,
   Figure 2.8. <https://www.ipcc.ch/report/ar6/wg2/figures/chapter-2/figure-2-008/>
6. IPCC, 2022: Summary for Policymakers. In: *Climate Change 2022: Impacts, Adaptation and
   Vulnerability* (AR6 WGII). <https://www.ipcc.ch/report/ar6/wg2/chapter/summary-for-policymakers/>
7. Armstrong McKay, D. I. et al., 2022: Exceeding 1.5 °C global warming could trigger multiple
   climate tipping points. *Science* 377, eabn7950. doi:10.1126/science.abn7950
8. Rounce, D. R. et al., 2023: Global glacier change in the 21st century: Every increase in
   temperature matters. *Science* 379, 78–83. doi:10.1126/science.abo1324
9. Lenton, T. M. et al., 2023: Quantifying the human cost of global warming. *Nature
   Sustainability* 6, 1237–1247. doi:10.1038/s41893-023-01132-6 (open access)
10. Caretta, M. A., Mukherji, A. et al., 2022: Water. In: *Climate Change 2022: Impacts,
    Adaptation and Vulnerability* (AR6 WGII), Chapter 4.
    <https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-4/>
11. Jylhä, K., Räisänen, P. and Utriainen, J., 2024: Climate projections. FINSCAPES final
    seminar, Finnish Meteorological Institute, 24 October 2024 (slides).
    <https://www.syke.fi/sites/default/files/documents/Jylh%C3%A4-R%C3%A4is%C3%A4nen_Utriainen_climate-projections.pdf>
12. Ruosteenoja, K. and Jylhä, K., 2021: Projected climate change in Finland during the 21st
    century calculated from CMIP6 model simulations. *Geophysica* 56(1), 39–69.
    <https://www.geophysica.fi/pdf/geophysica_2021_56_1_039_ruosteenoja.pdf>
13. Ruosteenoja, K. and Jylhä, K., 2023: Heatwave projections for Finland at different levels
    of global warming derived from CMIP6 simulations. *Geophysica* 58(1), 47–75.
    <https://www.geophysica.fi/pdf/geophysica_2023_58_1_047_ruosteenoja.pdf>
14. Ruosteenoja, K. and Jylhä, K., 2025: Extreme cold days and spells in Northern Europe at
    0.5 °C–2.0 °C global warming levels (journal not checked).
    <https://agris.fao.org/search/zh/records/682f31af9d0aa4165340b8ec>
15. Ruosteenoja, K., Markkanen, T. and Räisänen, J., 2020: Thermal seasons in northern Europe in
    projected future climate. *International Journal of Climatology* 40, 4444–4462.
    doi:10.1002/joc.6466
