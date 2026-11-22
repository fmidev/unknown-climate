"""
User-visible text of the game in Finnish ('fi') and English ('en').

t('key', name=value) returns the text in the current language (st.session_state['lang']) with
str.format placeholders filled in. tr({'fi': ..., 'en': ...}) picks the language from an inline
dict (used for the labels of the data tables in app.py). Numbers are formatted by the caller
(app._num) before they are passed in, so the decimal separator follows the language.

To add a text: add an entry with both languages here; the check at the bottom fails otherwise.
"""
import streamlit as st

LANGUAGES = ('fi', 'en')


def lang():
    return st.session_state['lang']


def tr(texts):
    """The current language's entry of a {'fi': ..., 'en': ...} dict."""
    return texts[lang()]


def t(key, **kwargs):
    return TEXTS[key][lang()].format(**kwargs)


TEXTS = {
    # --- general ---
    'app_name': {
        'fi': 'Tuntematon ilmasto',
        'en': 'Unknown Climate',
    },
    'start_over': {
        'fi': '🔄 Aloita alusta (uusi ilmasto)',
        'en': '🔄 Start over (new climate)',
    },
    'footer_credits': {
        'fi': '© 2026 Ilmatieteen laitos · MIT-lisenssi · Ilmastomalli FaIR · Data: IGCC, '
              'Global Carbon Budget, HadCRUT5 (Met Office), IIASA SSP, IPCC · '
              '[Lähteet ja lisenssit](https://github.com/fmidev/unknown-climate/blob/main/CREDITS.md)',
        'en': '© 2026 Finnish Meteorological Institute · MIT licence · FaIR climate model · Data: IGCC, '
              'Global Carbon Budget, HadCRUT5 (Met Office), IIASA SSP, IPCC · '
              '[Sources and licences](https://github.com/fmidev/unknown-climate/blob/main/CREDITS.md)',
    },
    'nav_back': {'fi': '⬅ Edellinen', 'en': '⬅ Previous'},
    'nav_forward': {'fi': 'Seuraava ➡', 'en': 'Next ➡'},
    'nav_impacts': {'fi': '🌡️ Vaikutukset', 'en': '🌡️ Impacts'},
    'replay': {'fi': '▶ Toista animaatio', 'en': '▶ Replay animation'},
    'spinner_fair': {'fi': 'Lasketaan FaIR-simulaatio...', 'en': 'Running the FaIR simulation...'},
    'pct': {'fi': '{value} %', 'en': '{value}%'},
    'unit_per_year': {'fi': 'GtCO₂/vuosi', 'en': 'GtCO₂/year'},
    'axis_year': {'fi': 'Vuosi', 'en': 'Year'},
    'axis_temp': {'fi': 'Lämpötila-anomalia (°C)', 'en': 'Temperature anomaly (°C)'},

    # --- estimate histograms and exceedance probabilities ---
    'est_ecs_title': {'fi': 'Ilmastoherkkyys', 'en': 'Climate sensitivity (ECS)'},
    'est_temp_title': {
        'fi': 'Lämpeneminen {first}–{last} keskimäärin',
        'en': 'Mean warming {first}–{last}',
    },
    'est_true_value': {'fi': ' oikea arvo {value}', 'en': ' true value {value}'},
    'est_caption': {
        'fi': 'Pylväät: kuinka todennäköinen kukin arvo on. Alla: paras arvio (piste) ja 95 %:n väli – '
              'oikea arvo osuu tälle välille 19 kertaa 20:stä.',
        'en': 'Bars: how likely each value is. Below: best estimate (dot) and 95% range – '
              'the true value falls within this range 19 times out of 20.',
    },
    'exceed_heading': {
        'fi': '**Todennäköisyys, että lämpeneminen vuoden {year} tienoilla (keskiarvo {first}–{last}) '
              'ylittää tason** ({stage}):',
        'en': '**Probability that warming around {year} (mean of {first}–{last}) exceeds the level** '
              '({stage}):',
    },
    'exceed_label': {'fi': 'yli {level} °C', 'en': 'above {level} °C'},
    'exceed_delta': {'fi': '{change} %-yks. alkuarviosta', 'en': '{change} pp vs initial estimate'},

    # --- impacts page ---
    'imp_title': {'fi': '🌡️ Mitä lämpeneminen tarkoittaa?', 'en': '🌡️ What does warming mean?'},
    'imp_intro': {
        'fi': 'Valitse lämpenemistaso nähdäksesi vaikutukset maailmalla ja Suomessa.  \n'
              '*(Verrattuna esiteolliseen aikaan 1850–1900)*',
        'en': 'Choose a warming level to see the impacts around the world and in Finland.  \n'
              '*(Compared with the pre-industrial period 1850–1900)*',
    },
    'imp_back': {'fi': '⬅ Takaisin peliin', 'en': '⬅ Back to the game'},
    'imp_radio': {'fi': 'Lämpenemistaso', 'en': 'Warming level'},
    'imp_global': {'fi': '🌍 Maailmanlaajuisesti', 'en': '🌍 Globally'},
    'imp_finland': {'fi': '🇫🇮 Suomessa', 'en': '🇫🇮 In Finland'},
    'imp_decisions_both': {
        'fi': 'lupauksillanne ja nollapäästövuosillanne',
        'en': 'pledges and net-zero years',
    },
    'imp_decisions_pledges': {'fi': 'lupauksillanne', 'en': 'pledges'},
    'imp_message': {
        'fi': '📊 **Teidän {decisions}** lämpeneminen vuoden {year} tienoilla (keskiarvo {first}–{last}) '
              'ylittää **+{level} °C** todennäköisyydellä **{prob}** ({stage}).',
        'en': '📊 **With your {decisions}**, warming around {year} (mean of {first}–{last}) exceeds '
              '**+{level} °C** with a probability of **{prob}** ({stage}).',
    },
    'imp_centred': {
        'fi': '  \nSimulaationne 20 vuoden keskilämpötila {first}–{last}: **+{value} °C**.',
        'en': '  \nMean temperature of your simulation over the 20 years {first}–{last}: **+{value} °C**.',
    },
    'imp_sources': {
        'fi': 'Lähteet: IPCC AR6 WG1 (2021), SR1.5 (2018) · Suomen luvut: Ilmatieteen laitos',
        'en': 'Sources: IPCC AR6 WG1 (2021), SR1.5 (2018) · Finland figures: Finnish Meteorological Institute',
    },

    # --- temperature chart ---
    'series_obs': {'fi': 'Havaittu', 'en': 'Observed'},
    'series_model': {'fi': 'Ilmastomalli', 'en': 'Climate model'},
    'series_long_term': {'fi': '20 vuoden keskiarvo', 'en': '20-year mean'},
    'series_obs_unc': {'fi': 'Havaintojen epävarmuus (95 %)', 'en': 'Observational uncertainty (95%)'},
    'tt_series': {'fi': 'Sarja', 'en': 'Series'},
    'tt_temp': {'fi': 'Lämpötila', 'en': 'Temperature'},
    'paris_15': {'fi': '1,5 °C (Pariisin tavoite)', 'en': '1.5 °C (Paris goal)'},
    'paris_20': {'fi': '2,0 °C (Pariisin raja)', 'en': '2.0 °C (Paris limit)'},
    'peak_label': {
        'fi': 'Huippu (20 v. keskiarvo): {value} °C (n. {year})',
        'en': 'Peak (20-yr mean): {value} °C (~{year})',
    },

    # --- emissions charts ---
    'bar_base': {'fi': 'Päästöt {year}', 'en': 'Emissions {year}'},
    'bar_pledge': {'fi': 'Päästöt {year} (lupaus)', 'en': 'Emissions {year} (pledge)'},
    'bar_later': {
        'fi': 'Päästöt {year} (sama vuosimuutos jatkuu)',
        'en': 'Emissions {year} (same annual change continues)',
    },
    'pathway_title': {'fi': 'Päästöpolku alueittain', 'en': 'Emission pathway by region'},

    # --- screen: pledges ---
    'pl_title': {
        'fi': '🌍 Ilmastoneuvottelut — Mitä lupaatte?',
        'en': '🌍 Climate negotiations — What do you pledge?',
    },
    'pl_intro': {
        'fi': 'Jokainen ryhmä edustaa yhtä maailman suurta päästöaluetta. '
              'Sopikaa, kuinka paljon leikkaatte **fossiilisia CO₂-päästöjä** vuoteen **{year}** mennessä.',
        'en': "Each group represents one of the world's major emitting regions. "
              'Agree how much you will cut **fossil CO₂ emissions** by **{year}**.',
    },
    'pl_caption': {
        'fi': 'Fossiiliset CO₂-päästöt tarkoittavat fossiilisten polttoaineiden ja teollisuuden päästöjä. '
              'Maankäytön päästöt (esim. metsäkato) eivät muutu pelissä: ne noudattavat SSP2-4.5-skenaariota.',
        'en': 'Fossil CO₂ emissions are the emissions from fossil fuels and industry. '
              'Land-use emissions (e.g. deforestation) do not change in the game: they follow the '
              'SSP2-4.5 scenario.',
    },
    'pl_locked': {
        'fi': '🔒 Lupaukset on lukittu, koska ilmasto on jo arvottu. '
              'Jos haluatte muuttaa niitä, aloittakaa alusta.',
        'en': '🔒 The pledges are locked because the climate has already been drawn. '
              'To change them, start over.',
    },
    'pl_subheader': {'fi': 'Aseta jokaisen alueen lupaus', 'en': "Set each region's pledge"},
    'pl_slider_caption': {
        'fi': 'Päästöjen muutos vuodesta {base_year} vuoteen {year}: '
              '−100 % = nollapäästöt, 0 % = ennallaan, + = päästöt kasvavat.',
        'en': 'Change in emissions from {base_year} to {year}: '
              '−100% = zero emissions, 0% = unchanged, + = emissions grow.',
    },
    'pl_region_caption': {
        'fi': '{base_year}: **{base}** GtCO₂/v  \n{year}: **{pledged}** GtCO₂/v',
        'en': '{base_year}: **{base}** GtCO₂/yr  \n{year}: **{pledged}** GtCO₂/yr',
    },
    'pl_cut': {'fi': '{pct} % leikkaus', 'en': '{pct}% cut'},
    'pl_growth': {'fi': '{pct} % kasvu', 'en': '{pct}% growth'},
    'pl_total': {
        # Plain text (no Markdown): shown as the title of the matplotlib emissions bar chart
        'fi': 'Yhteensä {year}: {total} GtCO₂/vuosi ({change} vuoden {base_year} tasosta)',
        'en': 'Total {year}: {total} GtCO₂/year ({change} from the {base_year} level)',
    },
    'pl_estimate': {'fi': 'Alkuarvio näillä lupauksilla',
                    'en': 'Initial estimate with these pledges'},
    'pl_prior': {
        'fi': 'Keskilämpötila {first}–{last}: **{mean} °C** ({lo}–{hi} °C)  \n'
              'Paras arvio ja 95 %:n väli – emme vielä tiedä, kuinka herkkä ilmastomme on.',
        'en': 'Mean warming {first}–{last}: **{mean} °C** ({lo}–{hi} °C)  \n'
              'Best estimate and 95% range – we do not yet know how sensitive our climate is.',
    },
    'pl_assumption': {
        'fi': 'Oletus {year} jälkeen: kunkin alueen päästöt muuttuvat vuosittain yhtä paljon kuin '
              'vuosina {base_year}–{year} (laskevat korkeintaan nollaan; kasvavat pysyvät ennallaan).',
        'en': "Assumption after {year}: each region's emissions keep changing by the same amount per "
              'year as in {base_year}–{year} (falling emissions stop at zero; growing ones stay level).',
    },
    'pl_next': {
        'fi': 'Katsotaan alkuarvio tarkemmin →',
        'en': 'Take a closer look at the initial estimate →',
    },

    # --- screen: prior ---
    'pr_title': {
        'fi': '🤔 Mitä tiedämme ennen kuin mitään on tapahtunut?',
        'en': '🤔 What do we know before anything has happened?',
    },
    'pr_intro': {
        'fi': 'Tutkijat eivät tiedä tarkalleen, **kuinka herkästi ilmasto reagoi** hiilidioksidiin. '
              'Siksi ilmastomallissa on {n} versiota – **mahdollista ilmastoa** – jotka kaikki sopivat '
              'yhteen tähänastisten havaintojen kanssa.',
        'en': 'Scientists do not know exactly **how sensitively the climate responds** to carbon '
              'dioxide. That is why the climate model has {n} versions – **possible climates** – that '
              'all agree with the observations so far.',
    },
    'pr_ecs': {
        'fi': '**Ilmastoherkkyys** kertoo, kuinka paljon ilmasto lopulta lämpenisi, jos ilman '
              'CO₂-pitoisuus kaksinkertaistuisi pysyvästi. Mitä suurempi ilmastoherkkyys, sitä enemmän '
              'samat päästöt lämmittävät.',
        'en': '**Climate sensitivity** tells how much the climate would eventually warm if the CO₂ '
              'concentration of the air doubled permanently. The higher the climate sensitivity, the '
              'more the same emissions warm the planet.',
    },
    'pr_info': {
        'fi': '👆 Tämä on **alkuarvio**. Harmaa jakauma pysyy näkyvissä koko pelin ajan, '
              'jotta näette, miten arvio tarkentuu.',
        'en': '👆 This is the **initial estimate**. The grey distribution stays visible for the whole '
              'game, so you can see how the estimate becomes sharper.',
    },
    'pr_next': {'fi': 'Arvotaan meidän ilmastomme →', 'en': 'Draw our climate →'},

    # --- screen: draw ---
    'dr_title': {
        'fi': '🎲 Arvonta: mikä ilmastoista on meidän?',
        'en': '🎲 The draw: which climate is ours?',
    },
    'dr_intro': {
        'fi': 'Arvotaan yksi {n} mahdollisesta ilmastosta. Se on pelin "todellinen" ilmasto: '
              '**sen ilmastoherkkyys on salaisuus**, ja teidän on pääteltävä sitä havainnoista, '
              'kuten tutkijat tekevät oikeassakin maailmassa.',
        'en': 'One of the {n} possible climates is drawn. It is the "real" climate of the game: '
              '**its climate sensitivity is a secret**, and you have to work it out from observations, '
              'just as scientists do in the real world.',
    },
    'dr_button': {'fi': '🎲 Arvo ilmasto', 'en': '🎲 Draw a climate'},
    'dr_success': {
        'fi': '✨ Ilmasto nro {number} arvottu! Sen ilmastoherkkyys paljastetaan vasta pelin lopussa.',
        'en': '✨ Climate no. {number} has been drawn! Its climate sensitivity will be revealed only '
              'at the end of the game.',
    },
    'dr_simulate': {'fi': '🔬 Simuloi {start}–{end} →', 'en': '🔬 Simulate {start}–{end} →'},

    # --- screen: simulation 2040 ---
    's1_title': {
        'fi': '📊 Mitä tapahtui vuoteen {year} mennessä?',
        'en': '📊 What happened by {year}?',
    },
    's1_obs': {'fi': 'Havaittu {year}', 'en': 'Observed {year}'},
    's1_year': {'fi': 'Vuosi {year}', 'en': 'Year {year}'},
    's1_centred': {'fi': 'Keskiarvo {first}–{last}', 'en': 'Mean {first}–{last}'},
    's1_centred_help': {
        'fi': '95 %:n väli {lo}–{hi} °C, koska vuodet {p0}–{p1} on arvioitu',
        'en': '95% range {lo}–{hi} °C, because the years {p0}–{p1} are projected',
    },
    's1_below15': {
        'fi': '✅ 20 vuoden jakson {first}–{last} keskilämpötila on alle 1,5 °C:n tavoitteen!',
        'en': '✅ The 20-year mean temperature {first}–{last} is below the 1.5 °C goal!',
    },
    's1_between': {
        'fi': '⚠️ 20 vuoden jakson {first}–{last} keskilämpötila on yli 1,5 °C mutta alle 2 °C:n '
              'rajan.',
        'en': '⚠️ The 20-year mean temperature {first}–{last} is above 1.5 °C but below the 2 °C limit.',
    },
    's1_above20': {
        'fi': '❌ 20 vuoden jakson {first}–{last} keskilämpötila ylittää 2 °C:n Pariisin rajan.',
        'en': '❌ The 20-year mean temperature {first}–{last} exceeds the 2 °C Paris limit.',
    },
    's1_why': {
        'fi': '**Miksi keskiarvo eikä vain vuosi {year}?** Yksittäinen vuosi heittelee luonnollisen '
              'vaihtelun (esim. El Niño) takia. Pariisin sopimuksen rajat tarkoittavat pitkän ajan '
              'lämpenemistä, jota IPCC arvioi 20 vuoden keskiarvona, ja niin tehdään myös tässä pelissä. '
              'Vuoden {year} lopussa vuodet {p0}–{p1} ovat vielä tulevaisuutta, joten ne on arvioitu '
              '(katkoviiva ja varjostus). Arvio käyttää kaikkea vuoden {year} lopussa saatavilla olevaa '
              'tietoa: mittauksia ja uusinta tutkimusta, joihin tutustutte seuraavaksi.',
        'en': '**Why a mean and not just the year {year}?** A single year jumps up and down because of '
              'natural variability (e.g. El Niño). The limits of the Paris Agreement refer to long-term '
              'warming, which the IPCC measures as a 20-year mean, and this game does the same. At the '
              'end of {year}, the years {p0}–{p1} are still in the future, so they are estimated (dashed '
              'line and shading). The estimate uses all information available at the end of {year}: '
              'measurements and the latest research, which you will look at next.',
    },
    's1_split': {
        'fi': '💡 Huomatkaa: vuosi {year} ({single} °C) ja 20 vuoden keskiarvo ({centred} °C) ovat '
              'eri puolilla 1,5 °C:n rajaa. Yksi vuosi ei vielä kerro, onko raja ylitetty.',
        'en': '💡 Notice: the year {year} ({single} °C) and the 20-year mean ({centred} °C) are on '
              'different sides of the 1.5 °C limit. A single year does not yet tell whether the limit '
              'has been crossed.',
    },
    's1_real': {
        # Human-induced warming (IGCC 2025, ESSD 18, 3889, 2026) stands in for the 20-year
        # centred warming level, which needs projections and has no published 2025 value; WMO's
        # 2024 report gave 1.34-1.41 °C for the current warming level by three methods.
        'fi': 'Oikeassa maailmassa vuosi 2024 oli ensimmäinen yli 1,5 °C:n vuosi (1,51 °C), mutta '
              'pitkän ajan lämpenemisen arvioidaan olevan noin 1,4 °C (ihmisen aiheuttama '
              'lämpeneminen 2025: 1,37 °C, IGCC 2025).',
        'en': 'In the real world, 2024 was the first year above 1.5 °C (1.51 °C), but long-term '
              'warming is estimated at about 1.4 °C (human-induced warming in 2025: 1.37 °C, '
              'IGCC 2025).',
    },
    's1_next': {'fi': 'Mitä opimme havainnoista? →', 'en': 'What do the observations tell us? →'},

    # --- screen: observations 2040 ---
    'ob_title': {
        'fi': '🔭 Havainnot {year}: mitä lämpeneminen kertoo ilmastostamme?',
        'en': '🔭 Observations {year}: what does the warming tell us about our climate?',
    },
    'ob_intro': {
        'fi': 'Vuoden {year} lopussa tiedämme, kuinka paljon meidän ilmastomme lämpeni. '
              'Mitattu keskilämpötila vuosina {first}–{last}: **{observed} °C** '
              '(mittausepävarmuus ±{err} °C).  \n'
              'Ilmastot, joiden lämpeneminen sopii tähän mittaukseen, muuttuvat todennäköisemmiksi.',
        'en': 'At the end of {year} we know how much our climate has warmed. '
              'Measured mean temperature in {first}–{last}: **{observed} °C** '
              '(measurement uncertainty ±{err} °C).  \n'
              'Climates whose warming fits this measurement become more likely.',
    },
    'range_narrowed': {
        'fi': 'kapeni **{old} → {new} °C** ({pct} %)',
        'en': 'narrowed **{old} → {new} °C** ({pct}%)',
    },
    'range_widened': {
        'fi': 'leveni **{old} → {new} °C**',
        'en': 'widened **{old} → {new} °C**',
    },
    'ob_ranges': {
        'fi': 'Ilmastoherkkyyden 95 %:n väli {ecs_change}, vuoden {year} tienoilla odotettavan '
              'lämpenemisen {t_change}. ',
        'en': 'The 95% range of climate sensitivity {ecs_change}, that of warming around {year} '
              '{t_change}. ',
    },
    'ob_widened': {
        'fi': 'Havainto ei kaventanut väliä vaan siirsi arviota kohti {direction} ilmastoherkkyyttä '
              '(paras arvio {old} → {new} °C). Ilmastoherkkyyden jakauma on vino, joten väli voi '
              'silloin jopa levetä.',
        'en': 'The observation did not narrow the range but moved the estimate towards {direction} '
              'climate sensitivity (best estimate {old} → {new} °C). The distribution of climate '
              'sensitivity is lopsided, so the range can even widen when this happens.',
    },
    'ob_higher': {'fi': 'suurempaa', 'en': 'higher'},
    'ob_lower': {'fi': 'pienempää', 'en': 'lower'},
    'ob_small': {
        'fi': 'Arvio tarkentui – mutta vähemmän kuin voisi odottaa!',
        'en': 'The estimate became sharper – but less than you might expect!',
    },
    'ob_large': {
        'fi': 'Tällä kertaa havainnot kertoivat paljon, koska ilmastomme lämpeni selvästi {direction} '
              'kuin ilmastot keskimäärin ({prior_mean} °C). Yleensä arvio tarkentuu tässä vaiheessa '
              'vain vähän.',
        'en': 'This time the observations told us a lot, because our climate warmed clearly {direction} '
              'than the climates on average ({prior_mean} °C). Usually the estimate sharpens only a '
              'little at this stage.',
    },
    'ob_less': {'fi': 'vähemmän', 'en': 'less'},
    'ob_more': {'fi': 'enemmän', 'en': 'more'},
    'ob_expander_title': {
        'fi': 'Miksi 15 vuoden lämpeneminen kertoo ilmastoherkkyydestä yleensä niin vähän?',
        'en': 'Why do 15 years of warming usually tell so little about climate sensitivity?',
    },
    'ob_expander_body': {
        'fi': '- Lähivuosikymmenten lämpeneminen riippuu ennen kaikkea **lyhyen aikavälin vasteesta** '
              '(TCR): meret lämpenevät hitaasti, eikä ilmasto ole ehtinyt tasapainoon. ECS kuvaa '
              'lopullista tasapainoa.\n'
              '- **Pienhiukkaset (aerosolit)** viilentävät ilmastoa, ja niiden vaikutus tunnetaan '
              'huonosti. Herkkä ilmasto, jossa on voimakas aerosolien viilennys, lämpenee lähes '
              'yhtä paljon kuin vähemmän herkkä, jolla viilennys on heikko.\n'
              '- Sama pätee oikeaan maailmaan: havaittu lämpeneminen rajaa ilmastoherkkyyttä vain löyhästi.',
        'en': '- Warming over the next decades depends above all on the **short-term response** '
              '(TCR): the oceans warm slowly, and the climate has not had time to reach equilibrium. '
              'ECS describes the final equilibrium.\n'
              '- **Small particles (aerosols)** cool the climate, and their effect is poorly known. '
              'A sensitive climate with strong aerosol cooling warms almost as much as a less '
              'sensitive one with weak cooling.\n'
              '- The same holds in the real world: observed warming constrains climate sensitivity '
              'only loosely.',
    },
    'ob_next': {'fi': 'Tutkimus etenee →', 'en': 'Research advances →'},

    # --- screen: research ---
    're_title': {'fi': '🧪 Tutkimus etenee', 'en': '🧪 Research advances'},
    're_intro': {
        'fi': 'Vuoteen {year} mennessä tutkijat ovat oppineet lisää esimerkiksi muinaisilmastoista '
              'ja pilvien käyttäytymisestä. Uusi tutkimus arvioi meidän ilmastomme herkkyydeksi '
              '**{clue} °C ± {err} °C** (95 %:n väli).',
        'en': 'By {year}, scientists have learned more about, for example, past climates and the '
              'behaviour of clouds. A new study estimates the sensitivity of our climate to be '
              '**{clue} °C ± {err} °C** (95% range).',
    },
    're_ranges': {
        'fi': 'Alkuarvioon verrattuna ilmastoherkkyyden 95 %:n väli {ecs_change}, vuoden {year} '
              'tienoilla odotettavan lämpenemisen {t_change}.',
        'en': 'Compared with the initial estimate, the 95% range of climate sensitivity {ecs_change}, '
              'that of warming around {year} {t_change}.',
    },
    're_expander_title': {
        'fi': 'Miksi lämpenemisen arvio ei tarkentunut yhtä paljon kuin ilmastoherkkyyden?',
        'en': 'Why did the warming estimate not sharpen as much as the climate sensitivity estimate?',
    },
    're_expander_body': {
        'fi': 'Lämpeneminen vuoden {year} tienoilla ei riipu vain ilmastoherkkyydestä. Siihen '
              'vaikuttavat myös lyhyen aikavälin vaste, aerosolien viilennys ja se, kuinka paljon meret ja kasvillisuus '
              'sitovat hiilidioksidia. Vaikka ilmastoherkkyys tunnettaisiin tarkasti, lämpenemisessä '
              'olisi silti epävarmuutta.',
        'en': 'Warming around {year} does not depend on climate sensitivity alone. It is also affected '
              'by the short-term response, aerosol cooling and how much carbon dioxide the oceans and '
              'vegetation take up. Even if climate sensitivity were known precisely, warming would '
              'still be uncertain.',
    },
    're_next': {'fi': 'Vaihe 2: Nollapäästövuodet →', 'en': 'Phase 2: Net-zero years →'},

    # --- screen: phase 2 (net-zero years) ---
    'p2_title': {
        'fi': '🎯 Milloin kukin alue saavuttaa nollapäästöt?',
        'en': '🎯 When does each region reach net-zero emissions?',
    },
    'p2_intro': {
        'fi': 'Jokainen ryhmä päättää, milloin **oman alueensa** fossiiliset CO₂-päästöt laskevat '
              'nollaan. Metaani, maankäytön päästöt ja muut kasvihuonekaasut seuraavat nykyistä '
              'kehitystä (SSP2-4.5). Käyttäkää päätöksessä sitä, mitä nyt tiedätte ilmastostanne.',
        'en': 'Each group decides when the fossil CO₂ emissions of **its own region** fall to zero. '
              'Methane, land-use emissions and other greenhouse gases follow current trends '
              '(SSP2-4.5). Use what you now know about your climate when you decide.',
    },
    'p2_subheader': {
        'fi': 'Valitse nollapäästövuosi alueittain',
        'en': 'Choose a net-zero year for each region',
    },
    'p2_region_caption': {
        'fi': '{year}: {em} GtCO₂/v → 0 vuoteen **{nz}**',
        'en': '{year}: {em} GtCO₂/yr → 0 by **{nz}**',
    },
    'p2_estimate': {'fi': 'Arvio näillä päätöksillä', 'en': 'Estimate with these decisions'},
    'p2_button': {'fi': '🔬 Laske huippulämpötila', 'en': '🔬 Calculate the peak temperature'},
    'p2_stale': {
        'fi': 'Valinnat muuttuivat – laskekaa simulaatio uudelleen nähdäksenne tuloksen.',
        'en': 'The choices have changed – run the simulation again to see the result.',
    },
    'p2_results': {'fi': '📊 Simulaatiotulokset', 'en': '📊 Simulation results'},
    'p2_below15': {
        'fi': '✅ Lämpenemisen huippu (20 vuoden keskiarvo) jää alle 1,5 °C:n – pysytään tavoitteessa!',
        'en': '✅ Peak warming (20-year mean) stays below 1.5 °C – we stay within the goal!',
    },
    'p2_between': {
        'fi': '⚠️ Lämpenemisen huippu (20 vuoden keskiarvo) on yli 1,5 °C mutta alle 2 °C.',
        'en': '⚠️ Peak warming (20-year mean) is above 1.5 °C but below 2 °C.',
    },
    'p2_above20': {
        'fi': '❌ Lämpenemisen huippu (20 vuoden keskiarvo) ylittää 2 °C:n Pariisin rajan.',
        'en': '❌ Peak warming (20-year mean) exceeds the 2 °C Paris limit.',
    },
    'p2_split': {
        'fi': '💡 Kuumin yksittäinen vuosi ({year}: {single} °C) on yli {level} °C, mutta 20 vuoden '
              'keskiarvon huippu ({peak} °C) jää sen alle. Yksi lämmin vuosi ei vielä tarkoita, että '
              'raja on ylitetty.',
        'en': '💡 The hottest single year ({year}: {single} °C) is above {level} °C, but the peak of '
              'the 20-year mean ({peak} °C) stays below it. One warm year does not mean that the limit '
              'has been crossed.',
    },
    'p2_next': {'fi': '🔎 Paljasta ilmaston salaisuus →', 'en': "🔎 Reveal the climate's secret →"},

    # --- screen: reveal ---
    'rv_title': {
        'fi': '🔎 Paljastus: millainen ilmastomme oikeasti oli?',
        'en': '🔎 The reveal: what was our climate really like?',
    },
    'rv_need_phase2': {
        'fi': 'Laskekaa ensin vaiheen 2 simulaatio.',
        'en': 'Run the Phase 2 simulation first.',
    },
    'rv_intro': {
        'fi': 'Meidän ilmastomme herkkyys oli **{ecs} °C**, ja teidän päätöksillänne se lämpeni '
              'vuoden {year} tienoilla (keskiarvo {first}–{last}) **{temp} °C**.',
        'en': 'The sensitivity of our climate was **{ecs} °C**, and with your decisions it warmed by '
              '**{temp} °C** around {year} (mean of {first}–{last}).',
    },
    'rv_ecs_name': {'fi': 'Ilmastoherkkyys', 'en': 'Climate sensitivity'},
    'rv_temp_name': {'fi': 'Lämpeneminen {first}–{last}', 'en': 'Warming {first}–{last}'},
    'rv_hit': {
        'fi': '🎯 {name}: oikea arvo {value} °C osui arvion 95 %:n välille '
              '({lo}–{hi} °C, paras arvio {mean} °C).',
        'en': '🎯 {name}: the true value {value} °C fell within the 95% range of the estimate '
              '({lo}–{hi} °C, best estimate {mean} °C).',
    },
    'rv_miss': {
        'fi': '😮 {name}: oikea arvo {value} °C jäi arvion 95 %:n välin '
              '({lo}–{hi} °C) ulkopuolelle. Näin käy noin kerran 20 pelistä – '
              'se kuuluu epävarmuuteen.',
        'en': '😮 {name}: the true value {value} °C fell outside the 95% range of the estimate '
              '({lo}–{hi} °C). This happens in about one game in 20 – it is part of uncertainty.',
    },
    'rv_lesson': {
        'fi': '**Mitä tästä opimme?** Emme voi tietää etukäteen, kuinka herkkä ilmasto on. Päätökset on '
              'silti tehtävä nyt. Mitä nopeammin päästöjä vähennetään, sitä pienempi on riski päätyä '
              'vaarallisen lämpenemisen puolelle.',
        'en': '**What do we learn from this?** We cannot know in advance how sensitive the climate is. '
              'Decisions still have to be made now. The faster emissions are cut, the smaller the risk '
              'of ending up with dangerous warming.',
    },
}

# Every text must exist in every language
for _key, _entry in TEXTS.items():
    assert set(_entry) == set(LANGUAGES), f'texts.py: {_key!r} must have exactly {LANGUAGES}'
