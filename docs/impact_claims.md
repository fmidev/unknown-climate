# Impact claims: inventory and source check

All climate-impact claims shown to players, with their exact wording and numbers, the references
the project gives for them, and the result of checking each claim against the literature.

Extracted from commit `e5a0094` and checked on 2026-11-24. A second pass the same day looked
for sources for the unsourced claims, checked the sources that had only been seen through
search summaries, and looked for sourced replacements for the problem claims; its results are
folded into the tables, the suggested fixes and the source list. Nothing in the app has been
changed; the suggested fixes at the end are proposals only.

**Verdicts:**
- ✅ the source states it.
- ≈ roughly right, or derived rather than stated.
- ⚠️ overstated or inconsistent with the source.
- ❌ contradicted by the sources.
- ❓ no source found.

## Where impact claims appear

| # | Location | What it is | Shown to players? |
|---|---|---|---|
| A | `app.py:230` `IMPACTS` (labels in `IMPACT_LABELS`, `app.py:218`) | Impacts page: 5 global + 5 Finland items at 1.5 / 2 / 3 / 4 °C, each with a severity bar | Yes, impacts page |
| B | `app.py:194` `TEMP_ANNOTATIONS` | One- or two-line labels next to the dashed warming-level lines in the temperature chart | Yes, every temperature chart (hidden on narrow screens) |
| C | `make_presentation_figure.py:59` `TEMP_ANNOTATIONS` | Finnish copy of B for the standalone presentation figure ("copied from app.py") | Only in the presentation figure |
| D | `ilmasto_vaikutukset.pptx` (gitignored, local only) | Slides 2–3: tables of the same impacts as A | Only in presentations |

## References as given in the project

There is only a blanket reference; no individual claim has its own source.

| Location | Text |
|---|---|
| `app.py:215–217` (code comment) | "Global figures from IPCC AR6 WG1 (2021) and SR1.5 (2018). Finland figures from Finnish Meteorological Institute projections (Finland warms ~1.5–2× the global average due to Arctic amplification)." |
| `texts.py:106` `imp_sources` (shown at the bottom of the impacts page) | FI: "Lähteet: IPCC AR6 WG1 (2021), SR1.5 (2018) · Suomen luvut: Ilmatieteen laitos" / EN: "Sources: IPCC AR6 WG1 (2021), SR1.5 (2018) · Finland figures: Finnish Meteorological Institute" |
| `CREDITS.md:96–105` | IPCC, 2021: *Climate Change 2021: The Physical Science Basis*, WGI AR6, doi:10.1017/9781009157896. IPCC, 2018: *Global Warming of 1.5 °C*, doi:10.1017/9781009157940. Finland: "Finnish Meteorological Institute. **TODO: name the exact publication(s).**" |
| `README.md:107–109` (caveat) | "Impacts are indicative only … rounded, simplified figures for classroom discussion. They draw loosely on IPCC reports and Finnish sources, but they are not a rigorous synthesis of the research literature." |
| `README.md:202` | "The impact figures are from IPCC AR6 and SR1.5." |
| pptx slides 2–3 footer | "Lähteet: IPCC AR6 WG1 (2021) · SR1.5 (2018) · Ilmatieteen laitos" |
| `TEMP_ANNOTATIONS` (B, C) | No reference of its own |

The impacts page header (`texts.py:81` `imp_intro`) says all levels are relative to the
pre-industrial period 1850–1900.

## Summary of the check

- **Supported (✅):** 19 of 47 claims are stated in a source: corals at 1.5 and 2 °C, the
  Arctic at 1.5–3 °C, insects at 1.5–3 °C, the heat-extreme factors at 1.5, 2 and 4 °C, sea
  level at 2 °C, and some qualitative Finland items. Insects at 3 °C (49 %) is supported, but
  by Warren et al. 2018, which the project doesn't cite.
- **Wrong or overstated:**
  - **Sea level at 3 and 4 °C is too high.** AR6 gives medians of about 61 and 70 cm.
  - **The Arctic at 4 °C is ice-free "in most years", not every year.**
  - **The 4 °C species figure is a different metric.** It most likely comes from Warren et
    al. 2013 (34 % of common *animals*, not insects).
  - **"Helsinki like Stockholm today" at 1.5 °C** comes about half a degree of global warming
    too early.
  - **Snow "a thing of the past" and skiing "no longer viable" at 4 °C are stronger than the
    sources.** In a roughly 4 °C world, southern Finland keeps snow for less than half as many
    days as in 1961–1990 [8b], and artificial snow keeps skiing going in a few places [16].
  - **The ski season "shorter by 1–2 months" at 2 °C is too long at the upper end.** FMI's
    CMIP6 snow scenarios give about a month for southern Finland [14].
  - **Reindeer herding "collapsing" at 4 °C is also stronger than the sources.**
  - **The chart label "Baltic Sea no longer freezes" at 2 °C is contradicted by the sources.**
- **No source found (❓):** only reindeer herding "collapsing" at 4 °C (F20) is left. Sources
  were found for the ski-season lengths (F13, F14) and the skiing items, mostly qualitative or
  derived from scenario results. The FMI TODO in `CREDITS.md` can now be filled (fix 10).
- **Missing references:** the claims actually rest on AR6 WGI Chapter 9, AR6 WGII, Warren et al.
  2018 and Finnish sources. None of these are cited, and AR6 WGII is not cited at all.
- **Second pass:** most sources that had only been seen through search summaries were checked
  against the paper, an accepted manuscript or the abstract (see "Sources used in the check"),
  and the numbers in this file held. Sourced wording for each problem claim is in the
  suggested fixes.

## A. Impacts page (`IMPACTS`, `app.py:230`)

"Sev." is the hand-set severity bar (0–100) drawn under each item. It has no reference.

### Global

| ID | Level | Label (EN / FI) | Value EN | Value FI | Sev. | Line | Verdict | What the source says |
|---|---|---|---|---|---|---|---|---|
| G1 | 1.5 °C | Sea level rise (2100) / Merenpinnannousu (2100) | ~40 cm | ~40 cm | 25 | 234 | ≈ | AR6 WGI Table 9.10: 0.44 (0.34–0.59) m by 2100 vs 1995–2014 [2]. SR1.5 B.2.1: 0.26–0.77 m vs 1986–2005 [1]. "~45 cm" would match AR6. |
| G2 | 2.0 °C | 〃 | ~50 cm | ~50 cm | 45 | 252 | ✅ | Table 9.10: 0.51 (0.40–0.69) m [2]. SR1.5: 0.1 m (0.04–0.16) more than at 1.5 °C [1]. |
| G3 | 3.0 °C | 〃 | ~80 cm | ~80 cm | 65 | 270 | ⚠️ | Table 9.10: 0.61 (0.50–0.81) m [2]. 80 cm is the top of the *likely* range. |
| G4 | 4.0 °C | 〃 | ~100 cm+ | ~100 cm+ | 85 | 287 | ⚠️ | Table 9.10: 0.70 (0.58–0.92) m [2]. Rise of 1 m or more needs low-confidence ice-sheet processes: SSP5-8.5 low-confidence p-box 0.63–1.60 m (17–83 %) [2]; "approaching 2 m" is low likelihood (SPM B.5.3) [3]. |
| G5 | 1.5 °C | Coral reefs / Koralliriutat | 70–90% lost | 70–90 % häviää | 35 | 235 | ✅ | SR1.5 B.4.2: "decline by a further 70–90% at 1.5°C (high confidence)" [1]. "Further" means beyond today's losses. |
| G6 | 2.0 °C | 〃 | >99% lost — practically all | >99 % häviää — käytännössä kaikki | 75 | 253 | ✅ | SR1.5 B.4.2: "larger losses (>99%) at 2ºC (very high confidence)" [1]. |
| G7 | 3.0 °C | 〃 | practically gone | käytännössä hävinneet | 90 | 271 | ≈ | Follows from G6. AR6 WGII SPM: very high near-term risk to warm-water coral reefs [4]. |
| G8 | 4.0 °C | 〃 | gone | hävinneet | 100 | 288 | ≈ | As G7. |
| G9 | 1.5 °C | Arctic: ice-free summer / Arktis: jäätön kesä | once in a hundred years | kerran sadassa vuodessa | 15 | 236 | ✅ | SR1.5 B.4.1: "one sea ice-free Arctic summer is projected per century" (high confidence) [1]. |
| G10 | 2.0 °C | 〃 | once in ten years | kerran kymmenessä vuodessa | 40 | 255 | ✅ | SR1.5 B.4.1: "at least one per decade with 2°C" [1]. AR6 qualifies it: low confidence in the warming level of the first ice-free September [2]. |
| G11 | 3.0 °C | 〃 | in most years | useimpina vuosina | 70 | 272 | ✅ | AR6 WGI Ch 9 (9.3.1.1): "at 3°C warming, the Arctic is practically sea ice free in September in most years (medium confidence)" [2]. |
| G12 | 4.0 °C | 〃 | every year | joka vuosi | 95 | 289 | ⚠️ | AR6 WGI Ch 9 Executive Summary: at 3–5 °C "practically sea ice free throughout several months in most years (high confidence)" [2]. That is "most years", not every year, and for several months, not only in summer. |
| G13 | 1.5 °C | Species losing half their habitat / Lajien elinympäristö puolittuu | ~6% of insects | ~6 % hyönteisistä | 20 | 237 | ✅ | SR1.5 B.3.1: 6 % of insects (8 % of plants, 4 % of vertebrates) lose over half their climatically determined range (medium confidence) [1]. |
| G14 | 2.0 °C | 〃 | ~18% of insects | ~18 % hyönteisistä | 45 | 256 | ✅ | SR1.5 B.3.1: 18 % of insects (16 % plants, 8 % vertebrates) [1]. |
| G15 | 3.0 °C | 〃 | ~49% of insects | ~49 % hyönteisistä | 70 | 273 | ✅ | Not in SR1.5 or AR6 WGI. Source is Warren et al. 2018 [5]: at ~3.2 °C, 49 % (31–65 %) of insects, 44 % of plants and 26 % of vertebrates (confirmed in the accepted manuscript). Needs its own reference. |
| G16 | 4.0 °C | 〃 | >35% of species | >35 % lajeista | 85 | 290 | ⚠️ | Not found as stated. Most likely origin: Warren et al. 2013 [6] (abstract checked): without mitigation (A1B), 34 ± 7 % of common and widespread *animals* and 57 ± 6 % of plants lose ≥50 % of their climatic range by the 2080s. Another candidate is AR6 WGII SPM B.4.1 [4] ("3 to 39%" of species at very high *extinction* risk at 4 °C). Either way it is a different metric from G13–G15, and 35 % after 49 % at 3 °C reads as an improvement. Warren et al. 2018 [5] has no 4 °C number in the text, but its no-mitigation run (4.5 °C) is plotted in AR6 WGII Fig. 2.8 [18]: there ≈ 74 % of invertebrates lose >50 % of range (my reading of the figure; mean of 21 models, no dispersal; the same figure gives ≈ 56 % at 3.2 °C, so its numbers run higher than the 49 % headline). "More than half of insects" at 4 °C is therefore safe. |
| G17 | 1.5 °C | Extreme heatwaves / Äärimmäiset helleaallot | 4× more frequent than in the 1800s | 4× yleisempiä kuin 1800-luvulla | 20 | 238 | ✅ | AR6 WGI Fig. SPM.6 [3]: the hottest-day 10-year event of 1850–1900 occurs 4.1× as often. Note: SPM.6 shows "hot temperature extremes over land" (daily maximum temperature), not heatwaves (multi-day events). |
| G18 | 2.0 °C | 〃 | ~6× more frequent | ~6× yleisempiä | 45 | 257 | ✅ | SPM.6: 5.6× [3]. |
| G19 | 3.0 °C | 〃 | ~8× more frequent | ~8× yleisempiä | 70 | 274 | ≈ | 3 °C is not in SPM.6. Interpolating 5.6× (2 °C) and 9.4× (4 °C) gives ≈7.5×. Fine, but derived. |
| G20 | 4.0 °C | 〃 | ~9× more frequent | ~9× yleisempiä | 90 | 291 | ✅ | SPM.6: 9.4× [3]. For the rarer 50-year event the factors are 8.6×, 13.9× and 39.2× at 1.5, 2 and 4 °C [3]; "extreme" could suggest these. |

### Finland

| ID | Level | Label (EN / FI) | Value EN | Value FI | Sev. | Line | Verdict | What the source says |
|---|---|---|---|---|---|---|---|---|
| F1 | 1.5 °C | Warming in Finland / Lämpötilan nousu Suomessa | +2–3 °C | +2–3 °C | 25 | 242 | ≈ | No FMI table per global warming level found. Finland's 8th National Communication [7] (citing Ruosteenoja & Jylhä 2021): Finland warms "about 1.6 to 1.8 times" the global mean under SSP2-4.5. Ruosteenoja & Jylhä 2021 [13]: the ratio is close to 2 in the early decades and converges towards ~1.6 on longer timescales. Climate Guide: Finland has warmed ~2 °C since the 1880s [8a]. With a 1.6–2× ratio, 1.5 °C gives 2.4–3 °C, so the lower end (2 °C, 1.33×) is a little low. |
| F2 | 2.0 °C | 〃 | +3–4 °C | +3–4 °C | 45 | 260 | ≈ | Consistent with 1.6–2× [7]. |
| F3 | 3.0 °C | 〃 | +4.5–6 °C | +4,5–6 °C | 65 | 277 | ≈ | Consistent with 1.6–2× [7]. |
| F4 | 4.0 °C | 〃 | +6–8 °C | +6–8 °C | 85 | 294 | ≈ | Consistent with 1.6–2× [7]. |
| F5 | 1.5 °C | Helsinki in winter / Helsinki talvella | like Stockholm today | kuin Tukholma tänään | 25 | 243 | ⚠️ | No source found; checked by calculation (see the analogue check below). It needs ≈ +2.1 °C of Helsinki winter warming, but 1.5 °C gives ≈ +1.3–1.6 °C. |
| F6 | 2.0 °C | 〃 | like Warsaw today | kuin Varsova tänään | 45 | 261 | ≈ | Calculation: needs ≈ +1.9–2.2 °C, and 2 °C gives ≈ +2.3–2.8 °C. Warsaw's winter is about the same as Stockholm's, so F5 → F6 shows no real step. |
| F7 | 3.0 °C | 〃 | like Prague today | kuin Praha tänään | 65 | 278 | ≈ | Calculation: needs ≈ +5.0 °C (Klementinum, a city-centre station), and 3 °C gives ≈ +4.3–5.3 °C. |
| F8 | 4.0 °C | 〃 | like Vienna today | kuin Wien tänään | 85 | 295 | ≈ | Calculation: needs ≈ +4.4–5.4 °C, and 4 °C gives ≈ +6.3–7.8 °C, i.e. milder than Vienna. Conservative. |
| F9 | 1.5 °C | Snowy winters in southern Finland / Lumiset talvet Etelä-Suomessa | less common | harvinaisempia | 25 | 244 | ✅ | National Communication [7]: "snow season becomes shorter, and the average snow water equivalent decreases, particularly in southern Finland." Qualitative only. |
| F10 | 2.0 °C | 〃 | unreliable | epäluotettavia | 50 | 262 | ≈ | SYKE press release 2016 [16] (read directly): natural skiing conditions "will become increasingly unreliable in the coming decades, especially in southern Finland". No warming level given. |
| F11 | 3.0 °C | 〃 | very rare | hyvin harvinaisia | 75 | 279 | ≈ | Climate Guide "Less snow" [8b] (page read): under the high SRES A2 scenario, from 1961–1990 to 2070–2099, snow-cover days in southern Finland "may decrease to less than one half" and average snow mass by 80–90 %. A2 in 2070–2099 is roughly 3.5–4 °C above pre-industrial (my estimate), so this belongs between 3 and 4 °C. "Under half the snow days" is less than "very rare". |
| F12 | 4.0 °C | 〃 | a thing of the past | pelkkä muisto | 95 | 296 | ⚠️ | No source found for snow disappearing. The sources describe much shorter and thinner snow cover [7, 8b]: at roughly 4 °C, less than half the snow-cover days of 1961–1990 and 80–90 % less snow mass in southern Finland [8b]. Lapland keeps a permanent winter snow cover even at the end of the century [8b]. |
| F13 | 1.5 °C | Ski season in the south / Hiihtosesonki etelässä | shorter by 2–3 weeks | lyhenee 2–3 viikkoa | 20 | 245 | ≈ | Räisänen, Luomaranta & Jylhä 2025 [14] (read from a printout), Fig. 8b, my reading: in southern Finland (60.5–62° N, 23–27° E, the inland belt north of the coast) the 20-year mean continuous snow season is already about 22 days shorter around 2024 (roughly 1.3 °C) than in 1981–2010. At 1.5 °C that gives about 25 days, so "2–3 weeks" is slightly low but fits. This is snow season, not ski season. For scale: Turunen et al. 2016 [9] project snow onset 19 days later and melt 16 days earlier at Sodankylä in 2035–2064 vs 1980–2009. |
| F14 | 2.0 °C | 〃 | shorter by 1–2 months | lyhenee 1–2 kuukautta | 50 | 263 | ⚠️ | Same source [14]: under SSP2-4.5 the season is "almost 50 days shorter" in the south in 2081–2100 (roughly 2.7 °C; paper text). Fig. 8b (my reading): about 33 days around 2040 under SSP2-4.5 and about 27 days in 2081–2100 under SSP1-2.6 (both roughly 1.8 °C). At 2 °C about a month, so "2 months" is too long. |
| F15 | 3.0 °C | 〃 | moved north | siirtynyt pohjoiseen | 75 | 280 | ✅ | Climate Guide [8c]: skiing "is estimated to concentrate to Northern Finland". Qualitative, no warming level. |
| F16 | 4.0 °C | 〃 | no longer economically viable | ei enää taloudellisesti kannattavaa | 90 | 297 | ⚠️ | Not stated as such. Climate Guide [8c]: artificial snow can keep cross-country skiing going in the south (but makes it a paid hobby), and downhill skiing is less vulnerable. SYKE [16]: snowmaking and snow storage need investment and "would only be viable at a few locations". That supports "skiing in the south mostly on artificial snow", not "no longer viable". |
| F17 | 1.5 °C | Reindeer herding in Lapland / Porotalous Lapissa | growing risk of icy pastures | jäätymisriski kasvaa | 20 | 246 | ✅ | Turunen et al. 2016 [9] (paper read): at Sodankylä, ground ice persisting through the winter rises from 31 % of winters (1980–2009) to 79 % in open areas in 2035–2064 (55 % and 52 % in forests). Rasmus et al. 2018 [10] (abstract): five of the seven most extensive basal-ice events of 1948–2016 occurred in 1991–2016. |
| F18 | 2.0 °C | 〃 | a significant threat | merkittävä uhka | 45 | 264 | ≈ | National Communication [7]: herding is "vulnerable to the negative effects of climate change", together with land-use pressures. Qualitative. |
| F19 | 3.0 °C | 〃 | seriously threatened | vakavasti uhattuna | 75 | 281 | ≈ | As F18. |
| F20 | 4.0 °C | 〃 | collapsing | romahtamassa | 90 | 298 | ❓ | No source for collapse. Herders interviewed in [9] saw a longer snowless season and thin snow as advantageous, but more frequent icing as a problem. [7] and AR6 WGII Box 13.2 (Sámi herding in Sweden; seen only through a news summary) [19] stress the cumulative effect of climate and land use (mining, wind power, forestry). A sourced step up from F19 is icy pastures in most winters (79 % of winters in open areas [9]; scenario not checked). |

#### Analogue check for F5–F8 (Helsinki winter vs other cities)

This is my own estimate, not from a source.

- **City winters.** December–February mean of the 1991–2020 normals, from the Wikipedia climate
  boxes. These were read via an automated summary, so confirm them before use.

  | Station | DJF mean | Difference from Helsinki |
  |---|---|---|
  | Helsinki Kaisaniemi | −2.5 °C | — |
  | Stockholm Observatorielunden | −0.5 °C | +2.1 |
  | Warsaw Okęcie / Bielany | −0.7 / −0.3 °C | +1.9 / +2.2 |
  | Prague Klementinum | +2.5 °C | +5.0 |
  | Vienna Hohe Warte / Innere Stadt | +1.9 / +2.9 °C | +4.4 / +5.4 |

- **"Today" baseline.** "Today" for these normals is 1991–2020. The IGCC GMST in
  `data/IGCC_GMST_1850-2025.csv` averages 0.87 °C over 1991–2020, so a warming level W means
  W − 0.87 °C more global warming than in the normals.
- **Winter warming in Helsinki.** I assumed it is about 2–2.5× the global warming. This is a
  rough assumption: winter warms more than the annual mean, and the annual mean warms 1.6–1.8×
  the global mean [7].
- **Results:**

  | Warming level | Helsinki winter warming |
  |---|---|
  | 1.5 °C | +1.3–1.6 °C |
  | 2 °C | +2.3–2.8 °C |
  | 3 °C | +4.3–5.3 °C |
  | 4 °C | +6.3–7.8 °C |

- **Interpretation.** In winter temperature, the city ladder is about one step behind:
  - 1.5 °C ≈ somewhat milder than Helsinki today.
  - 2 °C ≈ Stockholm or Warsaw.
  - 3 °C ≈ Prague.
  - 4 °C ≈ milder than Vienna.
- **What it leaves out.** Only the winter mean temperature is compared; snow, daylight and
  maritime effects are ignored.

## B. Temperature chart labels (`TEMP_ANNOTATIONS`, `app.py:194`)

| ID | Level | EN | FI | Matches | Verdict | Note |
|---|---|---|---|---|---|---|
| C1 | 1.5 °C | 70–90% of corals lost | 70–90 % koralleista häviää | G5 | ✅ | SR1.5 B.4.2 [1] |
| C2 | 2.0 °C | corals disappear | korallit katoavat | G6 | ✅ | ">99%" [1] |
| C3 | 2.0 °C | Baltic Sea no longer freezes | Itämeri ei enää jäädy | — | ❌ | National Communication [7]: "ice cover in the Gulf of Finland and the Sea of Bothnia will continue to form in winters, but it will happen increasingly later." Climate Guide [8d]: even with ~3 °C regional warming after mid-century, "the mildest winters would see ice only at the bottom of Bothnian Bay". Luomaranta et al. 2014 [11] (abstract read): the Baltic Sea is unlikely to become totally ice-free this century. Under RCP4.5, from the 2060s on (roughly 2–2.5 °C), the maximum ice extent of a typical winter stays below 80 000 km². The average today is about 204 000 km² [8d], so that is less than half. Under RCP8.5 in the 2080s (roughly 4 °C), ice is nearly absent outside the Bay of Bothnia. |
| C4 | 3.0 °C | Arctic Ocean ice-free most summers | Jäämeri jäätön useimpina kesinä | G11 | ✅ | AR6 WGI Ch 9 [2] |
| C5 | 3.0 °C | Lapland reindeer herding threatened | Lapin porotalous uhattuna | F19 | ≈ | Qualitative [7, 9] |
| C6 | 4.0 °C | heatwaves ~9× more frequent | helleaallot ~9× yleisempiä | G20 | ✅ | 9.4×, hottest-day 10-year event [3] |
| C7 | 4.0 °C | southern Finland practically snowless | Etelä-Suomi käytännössä lumeton | F12 | ⚠️ | Stronger than the sources: snow-cover days less than half of 1961–1990 [8b] |

## C, D. Copies outside the app

`make_presentation_figure.py:59` (Finnish only) is identical to B except C6:
"helleaallot **9,4×**" (app: "~9×"), and "etelä-Suomi" in lower case.

`ilmasto_vaikutukset.pptx` slides 2–3 have the same items as A, with these differences in wording
or numbers:

| Item | App (A) | pptx |
|---|---|---|
| G4 | ~100 cm+ | ~100+ cm |
| G13–G15 | ~6 / ~18 / ~49 % hyönteisistä | 6 / 18 / 49 % hyönteisistä (no "~") |
| G18 | ~6× yleisempiä | **5,6×** yleisempiä |
| G20 | ~9× yleisempiä | **9,4×** yleisempiä |
| G17 | 4× yleisempiä kuin 1800-luvulla | 4× yleisempiä |
| F5–F8 | kuin Tukholma tänään … | kuin Tukholma … (no "tänään") |
| F12 | pelkkä muisto | kadonnut muisto |
| F13, F14 | lyhenee 2–3 viikkoa / 1–2 kuukautta | lyhenee 2–3 vk / 1–2 kk |
| F17 | jäätymisriski kasvaa | kasvava riski |

The pptx's 5.6× and 9.4× are the exact SPM.6 values. Any fix in the app should also go to the
pptx and the presentation figure.

## Suggested fixes (not applied)

These need your decision. The wording is only a starting point.

1. **G3, G4: sea level.** Use AR6 Table 9.10 medians: ~60 cm at 3 °C and ~70 cm at 4 °C. You
   could add "(up to ~1 m or more if ice sheets melt faster)" at 4 °C. Optionally use ~45 cm at
   1.5 °C, and state the baseline as relative to 1995–2014.
2. **G12: Arctic at 4 °C.** Say "most years, for several months" instead of "every year".
3. **G16: species at 4 °C.** Use one metric at all four levels. Options:
   - Keep insects losing half their range, and at 4 °C say "over half of insects" ("yli puolet
     hyönteisistä"). That follows from 49 % at 3.2 °C [5] and ≈ 74 % at 4.5 °C in AR6 WGII
     Fig. 2.8 [18] (verdict ≈, derived).
   - Switch the whole row to AR6 WGII extinction risk ("up to 14 / 18 / 29 / 39 % of species
     at very high risk of extinction") [4].
4. **C3: Baltic Sea.** Drop the 2 °C label. Sourced alternatives [11, 8d]:
   - 2 °C: "Baltic Sea ice cover halves" / "Itämeren jääpeite puolittuu" (≈: typical-winter
     maximum extent below 80 000 km² vs ~204 000 km² today, RCP4.5 from the 2060s).
   - 4 °C: "sea ice mostly only in the Bay of Bothnia" / "merijäätä lähinnä vain Perämerellä"
     (≈: RCP8.5 in the 2080s).
   - Either way the sources agree that the Baltic Sea still freezes somewhere every winter
     this century.
5. **F5–F8: Helsinki analogues. Decision: drop the row** (no source; only my calculation).
   If it is ever brought back, shift it one step (e.g. 1.5 °C: "milder than today"; 2 °C:
   "like Stockholm today"; 3 °C: "like Prague"; 4 °C: "milder than Vienna"). No FMI analogue
   study was found. The
   global city-analogue study by Bastin et al. 2019 (PLOS ONE, RCP4.5 in 2050) names
   Stockholm → Budapest but not Helsinki in its text; Helsinki might be in its supplementary
   table (not checked). It uses 19 annual bioclimatic variables, not winter temperature.
6. **F9–F20, C3, C5, C7: snow, skiing, reindeer and Baltic Sea ice.** Reframe these rows
   around what the sources quantify; see "Proposal: reframed rows" below.
7. **Snow-season numbers.** These are changes from 1981–2010 [14], not from 1850–1900 like
   the warming levels. The numbers are my readings of the paper's Fig. 8 for its southern
   Finland box (60.5–62° N, 23–27° E), placed at warming levels by the scenario mappings
   above, so these rows are not on the shortlist of claims stated at warming levels.
8. **F1:** consider "+2.5–3 °C".
9. **Heatwave label.** "Extreme heat days" (hottest-day 10-year event, over land) is closer to
   SPM.6 than "extreme heatwaves".
10. **References.**
    - Add AR6 WGI Chapter 9 (Fox-Kemper et al. 2021), AR6 WGII SPM, Warren et al. 2018, and the
      Finnish sources actually used (e.g. [7]) to `CREDITS.md` and `imp_sources`.
    - Fill in the FMI TODO, for example with Ruosteenoja & Jylhä 2021 [13] (Finland warming)
      and Räisänen et al. 2025 [14] (snow), plus the Climate Guide articles actually used
      [8b–d] and Luomaranta et al. 2014 [11] (Baltic Sea ice).
    - If F20 or the skiing items change, add Turunen et al. 2016 [9] and the SYKE/Luke skiing
      work [16, 17].
    - Consider a per-item source list in this file, or in `CREDITS.md`.

## Shortlist: impacts stated at warming levels

Only claims for which the source itself gives a value at a global warming level (above
1850–1900). Allowed: a value stated at that level, or interpolation between two levels the
same source states, marked (i). Not allowed: extrapolation beyond the source's levels, or my
own conversion of an emission scenario and period into a warming level. "—" means the source
gives nothing at that level. This list supersedes the "derived" rows in the two proposal
sections below where they conflict.

### Global

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Source |
|---|---|---|---|---|---|
| Sea level rise by 2100 / Merenpinnan nousu vuoteen 2100 | ~45 cm | ~50 cm | ~60 cm | ~70 cm | AR6 WGI Table 9.10, medians 0.44 / 0.51 / 0.61 / 0.70 m vs 1995–2014 [2] |
| Sea level rise over the next 2000 years / Merenpinnan nousu seuraavan 2000 vuoden aikana | 2–3 m | 2–6 m | 4–10 m | 12–16 m | AR6 WGI SPM B.5.3 [3], Ch. 9 [2] |
| Once-a-decade hottest day on land / Kerran vuosikymmenessä sattuva kuumin päivä | 4× as often / 4× useammin | 6× | 7–8× (i) | 9× | AR6 WGI Fig. SPM.6: 4.1×, 5.6×, 9.4× [3] |
| Once-a-decade heaviest rain day on land / Kerran vuosikymmenessä sattuva rankin sadepäivä | 1.5× as often, 10% heavier / 1,5× useammin, 10 % rankempi | 1.7×, 14% | ~2×, ~22% (i) | 2.7×, 30% | Fig. SPM.6 [3] |
| Once-a-decade drought in drying regions / Kerran vuosikymmenessä sattuva kuivuus kuivuvilla alueilla | 2× as often / 2× useammin | 2.4× | ~3× (i) | 4× | Fig. SPM.6 [3] |
| Arctic Ocean ice-free in September / Jäämeri jäätön syyskuussa | once a century / kerran sadassa vuodessa | once a decade / kerran kymmenessä vuodessa | in most years / useimpina vuosina | in most years, for several months / useimpina vuosina, useita kuukausia | SR1.5 B.4.1 [1]; AR6 WGI Ch. 9 (3 °C; 3–5 °C) [2] |
| Coral reefs / Koralliriutat | a further 70–90% lost / vielä 70–90 % häviää | over 99% lost / yli 99 % häviää | — | — | SR1.5 B.4.2 [1]. 3 and 4 °C not stated; "practically gone" follows from 2 °C but is not a stated value |
| Insects losing half their range / Hyönteislajit, joiden elinalue puolittuu | ~6% | ~18% | ~half (49% at 3.2 °C) / ~puolet | over half / yli puolet (i) | SR1.5 B.3.1 [1], Warren et al. 2018 [5]; 4 °C between 3.2 °C (49 %) and 4.5 °C (≈ 74 %, AR6 WGII Fig. 2.8 [18]) |
| Species at very high risk of extinction / Erittäin suuressa sukupuuttovaarassa olevat lajit | up to 14% / jopa 14 % | up to 18% | up to 29% | up to 39% | AR6 WGII SPM B.4.1 ("3 to 14 %" … "3 to 39 %") [4]. Alternative to the insect row |
| Climate tipping points likely passed / Todennäköisesti ylitetyt keikahduspisteet | 4 | 7 | 8 | 13 | Thresholds as warming levels in Armstrong McKay et al. 2022 [21]; the count is mine (see the candidate section) |
| Glacier ice lost by 2100 / Jäätiköiden jäästä häviää vuoteen 2100 mennessä | a quarter / neljännes | ~30% (i) | ~35% (i) | two fifths / kaksi viidesosaa | Rounce et al. 2023: 26 % at 1.5 °C, 41 % at 4 °C, linear in between [20] |
| People living where the yearly mean is over 29 °C / Ihmiset, joiden asuinpaikan vuoden keskilämpötila on yli 29 °C | 1 in 20 / joka 20. | 1 in 10 / joka 10. | 1 in 4 (i) / joka 4. | 2 in 5 (i) / 2 viidestä | Lenton et al. 2023: 5 % (1.5), nearly 10 % (1.8), 22 % (2.7), 34 % (3.6), 45 % (4.4 °C) [22]. 2 °C rounded from 1.8 °C |
| River flood damage compared with 1.5 °C / Jokitulvien vahingot verrattuna 1,5 asteeseen | 1× | 1.4–2× | 2.5–3.9× | 4–5× | AR6 WGII SPM B.4.2 [4] (2, 3 °C); 4 °C from Ch. 4 [23], seen only through a news summary |

### Finland

No Finnish study was found that gives impacts at 3 or 4 °C; the FMI warming-level studies stop
at 2 °C. Only the temperature row reaches 4 °C, through FMI's stated ratio.

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Source |
|---|---|---|---|---|---|
| Warming in Finland / Lämpötilan nousu Suomessa | ~+2.5 °C | ~+3 °C | ~+5 °C | ~+6.5 °C | Finland warms "about 1.6 times" the global average (FMI, FINSCAPES [15]); 1.6 × level, rounded. Ratio closer to 2 in the early decades [13] |
| A heatwave that came once a decade at 0.5 °C (around the 1980s) / Helleaalto, joka 0,5 asteen lämpenemisellä tuli kerran vuosikymmenessä | every third summer / joka kolmas kesä | every other summer / joka toinen kesä | — | — | Ruosteenoja & Jylhä 2023: annual probability ~37 % at 1.5 °C (Heinola area) and 50 % at 2.0 °C (outside Lapland) [24]. "Around the 1980s" is my dating of 0.5 °C |
| Heatwave days a year in south-eastern Finland (daily mean above 20 °C) / Hellepäivät vuodessa Kaakkois-Suomessa | — | ~20 (from ~5 at 0.5 °C) / ~20 (0,5 asteella ~5) | — | — | [24] |
| A cold spell that came once a decade at 0.5 °C / Pakkasjakso, joka 0,5 asteen lämpenemisellä tuli kerran vuosikymmenessä | — | once in ~50 years / kerran noin 50 vuodessa | — | — | Ruosteenoja & Jylhä 2025 [32], via FINSCAPES slides [15]; cold days 60–80 % fewer than at 0.5 °C [32] |
| Thermal winter (daily mean below 0 °C) / Terminen talvi | — | 1–2 months shorter than 1971–2000 / 1–2 kuukautta lyhyempi kuin 1971–2000 | — | — | Ruosteenoja et al. 2020 [27]. The authors state that their period (RCP4.5, 2040–2069) corresponds to about 2 °C; this equivalence is theirs, not a warming-level analysis |

### Not on the list: scenario-based, not stated at warming levels

These rows in the proposal sections rest on emission scenarios and periods that I converted to
warming levels, so they are excluded: snow season length and snow amount in southern Finland
[14], the Climate Guide snow figure [8b], skiing [8c, 16], Baltic Sea ice [8d, 11], reindeer
pastures [9], Saimaa ringed seal [26], Helsinki sea level [25], and the 4 °C species figure from
Warren et al. 2013 (A1B scenario) [6].

For Finland at 3 and 4 °C, the rows can show "—", or the impacts page can say that Finnish
studies by warming level go up to 2 °C. No analysis of published data is planned.

## Proposal: reframed rows

The old wording need not be kept where a source supports a different framing better. Each row
below is built around one quantity a source gives across warming levels. Not applied; the
severity bars would need to be set again.

Verdict symbols as above. "Derived" means placed at a warming level by my own estimate,
because the source gives a scenario and period, not a warming level. Scenario-to-warming-level
mappings used: SSP2-4.5 around 2024 ≈ 1.3 °C, around 2090 ≈ 2.7 °C; A1B 2035–2064 ≈ 2–2.5 °C;
RCP4.5 2060s ≈ 2–2.5 °C; SRES A2 2070–2099 and RCP8.5 2080s ≈ 3.5–4.5 °C.

### Global

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Verdict, source |
|---|---|---|---|---|---|
| Sea level rise by 2100 / Merenpinnan nousu vuoteen 2100 | ~45 cm | ~50 cm | ~60 cm | ~70 cm (over 1 m possible if ice sheets melt faster) / ~70 cm (yli 1 m mahdollinen, jos mannerjäätiköt sulavat nopeammin) | ✅ AR6 Table 9.10 medians, relative to 1995–2014 [2]; 4 °C note from the low-confidence range [2, 3] |
| Coral reefs / Koralliriutat | a further 70–90% lost / vielä 70–90 % häviää | over 99% lost / yli 99 % häviää | practically gone / käytännössä hävinneet | gone / hävinneet | ✅ 1.5 and 2 °C [1]; ≈ 3 and 4 °C |
| Arctic Ocean ice-free in September / Jäämeri jäätön syyskuussa | once a century / kerran sadassa vuodessa | once a decade / kerran kymmenessä vuodessa | in most years / useimpina vuosina | in most years, for several months / useimpina vuosina, useita kuukausia | ✅ [1, 2]. SR1.5 says "summer" at 1.5 and 2 °C |
| Insects losing half their range / Hyönteislajit, joiden elinalue puolittuu | ~6% / ~6 % | ~18% / ~18 % | almost half / lähes puolet | over half / yli puolet | ✅ 1.5–3 °C [5] (49 % at 3.2 °C); ≈ 4 °C [18] |
| Once-a-decade hottest day on land / Kerran vuosikymmenessä sattuva kuumin päivä | 4× as often as in the 1800s / 4× useammin kuin 1800-luvulla | ~6× | ~7–8× | ~9× | ✅ 4.1×, 5.6×, 9.4× [3]; ≈ 3 °C interpolated |

Alternative species row (AR6 WGII SPM B.4.1 [4]): "up to 14 / 18 / 29 / 39 % of species at
very high risk of extinction" ("jopa 14 / 18 / 29 / 39 % lajeista erittäin suuressa
sukupuuttovaarassa"). It is the IPCC's own synthesis, but "risk of extinction" with wide
ranges is harder to explain than "half their range".

### Finland

Five rows. The Helsinki winter analogue (F5–F8) is dropped because it has no source; skiing
stays alongside the snow row.

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Verdict, source |
|---|---|---|---|---|---|
| Warming in Finland / Lämpötilan nousu Suomessa | +2.5–3 °C | +3–4 °C | +4.5–6 °C | +6–8 °C | ≈ ratio 1.6–2× [7, 13] |
| Snow season in southern Finland / Lumikausi Etelä-Suomessa | about 3 weeks shorter / noin 3 viikkoa lyhyempi | about a month shorter / noin kuukauden lyhyempi | about 2 months shorter / noin 2 kuukautta lyhyempi | about 3 months shorter, less than half left / noin 3 kuukautta lyhyempi, alle puolet jäljellä | ≈ derived from [14] Fig. 8b (my reading; 20-year means vs 1981–2010): −22 days around 2024 (~1.3 °C); in 2081–2100 −27 (SSP1-2.6, ~1.8 °C), −49 (SSP2-4.5, ~2.7 °C; paper text "almost 50"), −77 (SSP3-7.0, ~3.6 °C), −91 days (SSP5-8.5, ~4.4 °C). Interpolated: ~25, ~33, ~58, ~84 days. The 1981–2010 season there is about 120–150 days (Fig. 9a) |
| Cross-country skiing in the south / Hiihto Etelä-Suomessa | less reliable / epävarmempaa | unreliable / epävarmaa | moves to the north / siirtyy pohjoiseen | mostly on artificial snow, in a few places / lähinnä tykkilumella, harvoissa paikoissa | ≈ qualitative, levels by judgement [8c, 16] |
| Baltic Sea ice / Itämeren jäät | ice season 10–20 days shorter / jääkausi 10–20 päivää lyhyempi | ice cover halves in a typical winter / jääpeite puolittuu tavallisena talvena | ice season 40–70 days shorter / jääkausi 40–70 päivää lyhyempi | ice mostly only in the Bay of Bothnia / jäätä lähinnä vain Perämerellä | ≈ derived [8d, 11]. The Baltic Sea still freezes somewhere every winter this century [11] |
| Ice-locked reindeer pastures in Lapland / Jäätyneet porolaitumet Lapissa | more often than before / aiempaa useammin | every other winter or more / joka toinen talvi tai useammin | in most winters / useimpina talvina | in most winters, also in forests / useimpina talvina, myös metsissä | ✅ 1.5 °C [10]; ≈ derived 2–4 °C from 31 % → 79 % of winters (open areas; forests 52–55 %) at ~2–2.5 °C [9], placed conservatively |

Notes:
- **Baltic Sea ice.** The 1.5 °C and 3 °C values are Climate Guide's two cases, a regional
  warming of 0.5–1 °C and of about 3 °C over "today" [8d]. The page is undated, so "today" is
  probably the 2000s. The 2 °C value is the typical maximum extent below 80 000 km² vs
  ~204 000 km² on average (RCP4.5, from the 2060s) [11, 8d]. The 4 °C value is RCP8.5 in
  the 2080s [11]. The row mixes ice-season length and ice extent; each value is one the
  source states.
- **Reindeer pastures.** The 79 % comes from one site (Sodankylä), A1B in 2035–2064, with an
  annual warming of 2.8 °C there [9]. It is a snow-model result for one location, so "in most
  winters" is the honest level of detail. Herders also saw benefits in a shorter snow season
  [9], and land use adds pressure that is not climate-driven [7, 19].
- **Snow season.** "Than in 1981–2010" can be told to players as "than around the 1990s".
  The paper stresses large uncertainty: the 90 % model range is wide, and natural variability
  alone is 30–50 % of the 2023–2100 trend [14]. The season shortens about equally at both
  ends (later start, earlier end). In Lapland the change is smaller: about 30 days in
  2081–2100 under SSP2-4.5 [14].
- **Alternative snow row: the winter's largest snow amount** (maximum snow water equivalent)
  in southern Finland / Talven suurin lumimäärä Etelä-Suomessa: a quarter less / ~30 % less /
  about half / ~60 % less (neljänneksen / ~30 % / noin puolet / ~60 % vähemmän). Derived from
  [14] Fig. 8a: −22 % around 2024, and in 2081–2100 −22 % (SSP1-2.6), −41 % (SSP2-4.5; text
  "roughly 40%"), −59 % (SSP3-7.0) and −66 % (SSP5-8.5). It varies more from model to model
  and year to year than the season length does [14].

### Chart labels (`TEMP_ANNOTATIONS`)

| Level | EN | FI | Verdict |
|---|---|---|---|
| 1.5 °C | a further 70–90% of corals lost | vielä 70–90 % koralleista häviää | ✅ [1] |
| 2.0 °C | corals practically all lost | korallit lähes kaikki häviävät | ✅ [1] |
| 2.0 °C | Baltic Sea ice cover halves | Itämeren jääpeite puolittuu | ≈ [11, 8d] (replaces C3) |
| 3.0 °C | Arctic Ocean ice-free most Septembers | Jäämeri jäätön useimpina syyskuina | ✅ [2] |
| 3.0 °C | Lapland pastures icy most winters | Lapin laitumet jäässä useimpina talvina | ≈ [9] (replaces C5) |
| 4.0 °C | hottest days ~9× as often | kuumimmat päivät ~9× yleisempiä | ✅ [3] |
| 4.0 °C | snow season in southern Finland 3 months shorter | lumikausi Etelä-Suomessa 3 kuukautta lyhyempi | ≈ [14] (replaces C7) |

## Candidate new impacts

Impacts not yet in the game for which a credible source gives values at several warming levels.
Each row is written in the same form as the reframed rows above. Verdict symbols as before;
"derived" means placed at a warming level by my own estimate. Extra scenario mappings used here
(2081–2100 means, AR6): SSP1-2.6 ≈ 1.8 °C, SSP2-4.5 ≈ 2.7 °C, SSP5-8.5 ≈ 4.4 °C; RCP2.6
2070–2099 ≈ 1.7 °C; RCP4.5 2010–2039 ≈ 1.3 °C, 2040–2069 ≈ 2 °C [27], 2070–2099 ≈ 2.5 °C;
RCP8.5 2070–2099 ≈ 4–4.5 °C.

### Global

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Verdict, source |
|---|---|---|---|---|---|
| Sea level rise over the next 2000 years / Merenpinnan nousu seuraavan 2000 vuoden aikana | 2–3 m | 2–6 m | 4–10 m | 12–16 m | ✅ AR6 WGI SPM B.5.3 [3] and Chapter 9 [2]: committed rise for that peak warming |
| Once-a-decade heaviest rain day on land / Kerran vuosikymmenessä sattuva rankin sadepäivä | 1.5× as often, 10% heavier / 1,5× useammin, 10 % rankempi | 1.7×, 14% | ~2×, ~22% | 2.7×, 30% | ✅ AR6 WGI Fig. SPM.6 [3] (read from the figure); ≈ 3 °C interpolated |
| Once-a-decade drought in drying regions / Kerran vuosikymmenessä sattuva kuivuus kuivuvilla alueilla | 2× as often / 2× useammin | 2.4× | ~3× | 4× | ✅ Fig. SPM.6 [3]; ≈ 3 °C interpolated |
| Climate tipping points likely passed / Todennäköisesti ylitetyt ilmaston keikahduspisteet | 4: Greenland and West Antarctic ice sheets, coral reefs, permafrost thaw / 4: Grönlannin ja Länsi-Antarktiksen jäätiköt, koralliriutat, ikiroudan sulaminen | 7 | 8 | 13, incl. Amazon rainforest and the Atlantic overturning circulation / 13, mm. Amazonin sademetsä ja Atlantin kiertoliike | ≈ my count of best-estimate thresholds at or below each level in Armstrong McKay et al. 2022 [21] |
| People living where the yearly mean is over 29 °C / Ihmiset, joiden asuinpaikan vuoden keskilämpötila on yli 29 °C | 1 in 20 / joka 20. | 1 in 10 / joka 10. | 1 in 4 / joka 4. | 2 in 5 / 2 viidestä | ✅ 1.5 °C (5 %), ≈ others derived from 1.8 °C (nearly 10 %), 2.7 °C (22 %), 3.6 °C (34 %), 4.4 °C (45 %) [22]; today under 1 % |
| Glacier ice lost by 2100 / Jäätiköiden jäästä häviää vuoteen 2100 mennessä | a quarter / neljännes | ~30% | ~35% | two fifths / kaksi viidesosaa | ✅ 1.5 and 4 °C (26 % and 41 % of 2015 mass) [20]; ≈ 2 and 3 °C from the stated linear relation. Also: 49 % of all glaciers vanish at 1.5 °C, 83 % at 4 °C [20] |
| River flood damage compared with 1.5 °C / Jokitulvien vahingot verrattuna 1,5 asteeseen | 1× (baseline) / vertailutaso | 1.4–2× | 2.5–3.9× | 4–5× | ✅ 2 and 3 °C, AR6 WGII SPM B.4.2 [4], no adaptation; ≈ 4 °C from AR6 WGII Chapter 4 [23] (seen through a news summary) |

Notes:
- **Long-term sea level** is the strongest candidate: an IPCC statement for all four levels,
  and it shows that warming locks in change for millennia. It needs a line in the game
  explaining that this is the rise over 2000 years, not by 2100.
- **Tipping points.** The paper calls a tipping point "likely" passed beyond its central
  estimate. I counted all 16 elements; the 3 °C count excludes Sahel greening (2.8 °C), which
  is not a harm. Some take centuries to millennia to play out (Greenland ~10 000 years), so
  "passed" means "set in motion". The southern boreal forest dieback element (4 °C, range
  1.4–5 °C) is the one closest to Finland. The 2025 Global Tipping Points Report puts the
  coral reef threshold at 1.2 °C [29], so the 1.5 °C count may be conservative.
- **Heat exposure** comes from one study with a specific definition (the "human climate
  niche", 9.5 billion people). It is peer-reviewed and open access, but not an IPCC
  assessment.
- **Drought and heavy rain** use the same AR6 figure as the existing heat row, so the three
  could be combined into one extremes row.

### Finland

| Row (EN / FI) | 1.5 °C | 2 °C | 3 °C | 4 °C | Verdict, source |
|---|---|---|---|---|---|
| Winters with too little snow for Saimaa ringed seal lairs / Talvet, joina lunta on liian vähän saimaannorpan pesille | about 1 in 3 / noin joka kolmas | about 1 in 2 / noin joka toinen | 3 in 5 / 3 talvea viidestä | almost 9 in 10 / lähes 9 talvea kymmenestä | ≈ derived from the share of winters with snowdrifts under 20 cm: 28 % (RCP4.5 2010–2039), 42 % (RCP2.6 2070–2099), 50 % (RCP4.5 2040–2069), 60 % (RCP4.5 2070–2099), 86 % (RCP8.5 2070–2099) [26] |
| Sea level in Helsinki by 2100, land uplift included / Merenpinta Helsingissä vuoteen 2100, maankohoaminen mukana | under +10 cm / alle +10 cm | about +10 cm / noin +10 cm | about +25 cm / noin +25 cm | about +50 cm / noin +50 cm | ≈ derived from medians +9, +25 and +54 cm under low, medium and high emissions [25] |
| A heatwave that came once a decade in the 1980s / 1980-luvulla kerran vuosikymmenessä sattunut helleaalto | every third summer / joka kolmas kesä | every other summer / joka toinen kesä | most summers / useimpina kesinä | nearly every summer / lähes joka kesä | ✅ 1.5 and 2 °C [15, 24]; ≈ 3 and 4 °C beyond the study's range (it stops at 2 °C) |
| Thermal winter (daily mean below 0 °C) / Terminen talvi | — | 1–2 months shorter / 1–2 kuukautta lyhyempi | — | — | ✅ 2 °C only: 30–60 days shorter than 1971–2000 (RCP4.5, 2040–2069) [27]. Usable as a 2 °C chart label |

Notes:
- **Saimaa ringed seal.** The most relatable Finland candidate: an endemic, endangered species
  that needs snow drifts on lake ice for its pups. The paper's 2010–2039 and 2070–2099 RCP4.5
  values are for a slightly different statistic (minimum vs mean drift depth), so the 1.5 °C
  value is the least firm. Volunteers already pile up artificial snowdrifts to help.
- **Helsinki sea level** teaches something the global row cannot: land uplift still offsets
  most of the rise at low warming, but not at high warming. In the Bothnian Bay, the median
  still falls under low and medium emissions and stays roughly level under high emissions
  (medians across the coast: −43 to +16 cm low, −28 to +31 cm medium, +1 to +61 cm high)
  [25]. The paper's own baseline is 1995–2014.
- **Heatwaves.** The study's baseline is the 0.5 °C warming level, which was reached around
  the 1980s (my estimate). Ruosteenoja & Jylhä 2023 [24] also give heatwave days (daily mean above
  20 °C) in south-eastern Finland rising from about 5 to 20 a year between 0.5 and 2 °C.

### Looked at but not suitable as rows

- **Ticks** have spread up to ~400 km further north in western Finland since 1958 (crowdsourced tick sightings,
  *Scientific Reports* 2023 [30]), but no projection by warming level was found.
- **Lake ice:** ice break-up has already moved about two weeks earlier [31];
  no Finnish projection by warming level found, apart from Saimaa [26].
- **Forest damage** (storms on unfrozen soil, bark beetles, drought, fire) increases in
  Finland [28], but the review is qualitative.
- **Water scarcity:** AR6 WGII gives "up to 3 billion people" at 2 °C and "up to 4 billion"
  at 4 °C [23], with nothing at 1.5 or 3 °C.

### Chart label candidates

| Level | EN | FI | Verdict |
|---|---|---|---|
| 2.0 °C | Finnish winter 1–2 months shorter | Suomen talvi 1–2 kuukautta lyhyempi | ✅ [27] |
| 2.0 °C | once-a-decade heatwave every other summer | kerran vuosikymmenessä ollut helleaalto joka toinen kesä | ✅ [15, 24] |
| 4.0 °C | 13 tipping points likely passed | 13 keikahduspistettä todennäköisesti ylitetty | ≈ [21] |
| 4.0 °C | 12–16 m of sea level rise locked in | 12–16 m merenpinnan nousu lukittu | ✅ [2] |

## Sources used in the check

How each source was read:
- **Read directly:** [1]–[4] (IPCC web pages in a browser), [7] (text extracted from the PDF)
  and [18] (figure read in a browser; values measured from the image pixels).
- **Read from a page summary**, through an automated fetch: [5] (accepted manuscript), [8a]–[8d],
  [9] (published PDF), [11] (abstract), [13] (PDF), [15] (slides) and [16].
- **Read from a printout of the web page supplied by the user:** [14]; figure values read
  from the rendered page images.
- **Abstract only, through search results:** [6] and [10].
- **Through a news summary only:** [19].
- **Not read:** [17].
- **Candidate new impacts:** Fig. SPM.6 [3] read in a browser. Read through an automated fetch:
  [21] (published PDF), [22] (published PDF), [24] (PDF), [26] (article page) and [27]
  (accepted manuscript); [2] and [4] were fetched again for the new statements. Abstracts or
  summaries only: [20], [25] (abstract and press release; Helsinki medians from the press
  release), [28], [29], [30] and [31]. [23] only through a news summary of AR6.

1. IPCC, 2018: SR1.5 Summary for Policymakers, paragraphs B.2.1, B.3.1, B.4.1, B.4.2.
   <https://www.ipcc.ch/sr15/chapter/spm/>
2. Fox-Kemper, B. et al., 2021: Ocean, Cryosphere and Sea Level Change. AR6 WGI Chapter 9:
   Table 9.10, Executive Summary ("Cryospheric Changes and Sea Level Rise at Specific Levels of
   Global Warming"), Section 9.3.1.1. <https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-9/>
3. IPCC, 2021: AR6 WGI Summary for Policymakers, Figure SPM.6, B.2.5, B.5.3.
   <https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/>
4. IPCC, 2022: AR6 WGII Summary for Policymakers, B.4.1.
   <https://www.ipcc.ch/report/ar6/wg2/chapter/summary-for-policymakers/>
5. Warren, R. et al., 2018: The projected effect on insects, vertebrates, and plants of limiting
   global warming to 1.5 °C rather than 2 °C. *Science* 360, 791–795. doi:10.1126/science.aar3646
6. Warren, R. et al., 2013: Quantifying the benefit of early climate change mitigation in
   avoiding biodiversity loss. *Nature Climate Change* 3, 678–682. doi:10.1038/nclimate1887
7. Finland's Eighth National Communication under the UNFCCC, Chapter 6 (vulnerability, impacts,
   adaptation); projections from Ruosteenoja & Jylhä 2021, *Geophysica* 56(1), 39–69.
   <https://stat.fi/media/uploads/tup/khkinv/nc8_by_chapters/nc8_chapter_6.pdf>
8. Climate Guide (climateguide.fi, FMI and partners):
   a. "Climate in Finland has become warmer" (updated 3.12.2019),
      <https://climateguide.fi/articles/climate-in-finland-has-become-warmer>
   b. "Less snow", <https://climateguide.fi/articles/less-snow>
   c. "Traditional outdoor winter activities become more difficult",
      <https://climateguide.fi/articles/traditional-outdoor-winter-activities-become-more-difficult>
   d. "Baltic Sea ice conditions will change",
      <https://climateguide.fi/articles/baltic-sea-ice-conditions-will-change>
9. Turunen, M. et al., 2016: Coping with difficult weather and snow conditions: Reindeer herders'
   views on climate change impacts and coping strategies. *Climate Risk Management* 11.
   <https://jyx.jyu.fi/jyx/Record/jyx_123456789_49310>
10. Rasmus, S., Kivinen, S. and Irannezhad, M., 2018: Basal ice formation in snow cover in
    Northern Finland between 1948 and 2016. *Environmental Research Letters* 13, 114009.
11. Luomaranta, A. et al., 2014: Multimodel estimates of the changes in the Baltic Sea ice cover
    during the present century. *Tellus A* 66, 22617. doi:10.3402/tellusa.v66.22617
12. City climate normals 1991–2020: Wikipedia climate boxes for Helsinki, Stockholm, Warsaw,
    Prague and Vienna (national weather service data).
13. Ruosteenoja, K. and Jylhä, K., 2021: Projected climate change in Finland during the 21st
    century calculated from CMIP6 model simulations. *Geophysica* 56(1), 39–69.
    <https://www.geophysica.fi/pdf/geophysica_2021_56_1_039_ruosteenoja.pdf>
14. Räisänen, P., Luomaranta, A. and Jylhä, K., 2025: Future snow scenarios for Northern Europe
    based on Coupled Model Intercomparison Project phase 6 data. *International Journal of
    Climatology* 45, e8795. doi:10.1002/joc.8795. Data and code: FMI B2SHARE,
    <https://etsin.fairdata.fi/dataset/f44a3164-606e-4994-9eea-65207370da47>
15. Jylhä, K., Räisänen, P. and Utriainen, J., 2024: Climate projections (FINSCAPES final
    seminar slides, FMI, 24.10.2024).
    <https://www.syke.fi/sites/default/files/documents/Jylh%C3%A4-R%C3%A4is%C3%A4nen_Utriainen_climate-projections.pdf>
16. SYKE and Luke, 2016: press release on the cross-country skiing vulnerability mapping tool
    (18.2.2016). <https://syke.fi/en-US/content/38177/25245>
17. Neuvonen, M. et al., 2015: Vulnerability of cross-country skiing to climate change in
    Finland – An interactive mapping tool. *Journal of Outdoor Recreation and Tourism* 11,
    64–79. doi:10.1016/j.jort.2015.06.010
18. Parmesan, C. et al., 2022: Terrestrial and Freshwater Ecosystems and Their Services. AR6
    WGII Chapter 2, Figure 2.8.
    <https://www.ipcc.ch/report/ar6/wg2/figures/chapter-2/figure-2-008/>
19. Bednar-Friedl, B. et al., 2022: Europe. AR6 WGII Chapter 13, Box 13.2 "Sámi Reindeer Herding
    in Sweden". <https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-13/>
20. Rounce, D. R. et al., 2023: Global glacier change in the 21st century: Every increase in
    temperature matters. *Science* 379, 78–83. doi:10.1126/science.abo1324
21. Armstrong McKay, D. I. et al., 2022: Exceeding 1.5 °C global warming could trigger multiple
    climate tipping points. *Science* 377, eabn7950. doi:10.1126/science.abn7950
22. Lenton, T. M. et al., 2023: Quantifying the human cost of global warming. *Nature
    Sustainability* 6, 1237–1247. doi:10.1038/s41893-023-01132-6 (open access)
23. Caretta, M. A., Mukherji, A. et al., 2022: Water. AR6 WGII Chapter 4.
    <https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-4/>
24. Ruosteenoja, K. and Jylhä, K., 2023: Heatwave projections for Finland at different levels
    of global warming derived from CMIP6 simulations. *Geophysica* 58(1), 47–75.
    <https://www.geophysica.fi/pdf/geophysica_2023_58_1_047_ruosteenoja.pdf>
25. Pellikka, H., Johansson, M. M., Nordman, M. and Ruosteenoja, K., 2023: Probabilistic
    projections and past trends of sea level rise in Finland. *Natural Hazards and Earth
    System Sciences* 23, 1613–1630. doi:10.5194/nhess-23-1613-2023. Helsinki medians from
    the Aalto/FMI press release (2023):
    <https://www.aalto.fi/fi/uutiset/maankohoamisilmio-suojaa-suomen-rannikkoa-merenpinnan-nousulta-mutta-ei-loputtomiin>
26. Saimaa ringed seal breeding habitat under climate change (lake ice and snow modelling),
    *Climatic Change*, 2024. doi:10.1007/s10584-024-03797-0 (authors not checked)
27. Ruosteenoja, K., Markkanen, T. and Räisänen, J., 2020: Thermal seasons in northern Europe
    in projected future climate. *International Journal of Climatology* 40, 4444–4462.
    doi:10.1002/joc.6466
28. Venäläinen, A. et al., 2020: Climate change induces multiple risks to boreal forests and
    forestry in Finland: A literature review. *Global Change Biology* 26, 4178–4196.
    doi:10.1111/gcb.15183
29. Global Tipping Points Report 2025 (Armstrong McKay et al., key messages).
    <https://publications.pik-potsdam.de/rest/items/item_34058_1/component/file_34080/content>
30. Tick contact areas in Finland 1958–2021 from crowdsourced data, *Scientific Reports*, 2023.
    doi:10.1038/s41598-023-48744-8
31. ymparisto.fi: "Climate change is already visible in Finland's nature".
    <https://www.ymparisto.fi/en/state-environment/climate-change/climate-change-advances>
32. Ruosteenoja, K. and Jylhä, K., 2025: Extreme cold days and spells in Northern Europe at
    0.5 °C–2.0 °C global warming levels (abstract only; journal not checked).
    <https://agris.fao.org/search/zh/records/682f31af9d0aa4165340b8ec>
