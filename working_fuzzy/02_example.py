from expert import ExpertSystem
from rule import Rule
from fact import Fact, RelationshipFact
from condition import Condition


# Dodawanie faktów
facts = [
    Fact("wiek", 0.6),
    Fact("płeć", 0.5),
    Fact("cukrzyca_typu_1", 0.4),
    Fact("cukrzyca_typu_2", 0.8),
    Fact("choroba_nerek", 0.4),
    Fact("przewlekła_niewydolność_nerek", 0.3),
    Fact("ciąża", 0.0),
    Fact("karmienie_piersią", 0.0),
    Fact("astma", 0.3),
    Fact("niewydolność_serca", 0.5),
    Fact("dyslipidemia", 0.7),
    Fact("palenie", 0.6),
    Fact("otyłość", 0.6),
    Fact("stres", 0.5),
    Fact("brak_aktywności_fizycznej", 0.5),
    Fact("alkohol", 0.4),
    Fact("wcześniejsze_udary_mózgu", 0.2),
    Fact("choroba_wieńcowa", 0.5),
    Fact("nadciśnienie_tętnicze", 0.9),
    Fact("migrena", 0.3),
    Fact("choroba_wątroby", 0.2),
    Fact("zaburzenia_elektrolitowe", 0.4),
    Fact("depresja", 0.4),
    Fact("arytmia", 0.6),
    Fact("zespół_metaboliczny", 0.7),
    Fact("nerkowe_nadciśnienie_tętnicze", 0.5),
    Fact("wtórne_nadciśnienie_tętnicze", 0.3),
    Fact("nadciśnienie_lekooporne", 0.2),
    Fact("obwodowe_niedokrwienie_tętnic", 0.4),
    Fact("niedokrwienie_mózgu", 0.3),
    Fact("przewlekła_obturacyjna_cholecytka_naciekowa", 0.2),
    Fact("zaburzenia_układu_pokarmowego", 0.4),
    Fact("nadwrażliwość_na_leki", 0.3),
    Fact("anemia", 0.4),
    Fact("osteoporoza", 0.4),
    Fact("niedoczynność_tarczycy", 0.3),
    Fact("nadczynność_tarczycy", 0.2),
    Fact("zespół_długo_przedłużonego_qt", 0.1),
    Fact("choroba_parkinsona", 0.2),
    Fact("choroba_raynauda", 0.3),
    Fact("zaburzenia_lymphocytyczne", 0.2),
    Fact("niewydolność_zastawki_aortalnej", 0.3),
    Fact("niewydolność_zastawki_mitralnej", 0.3),
    Fact("kardiomiopatia_przerostowa", 0.2),
    Fact("reumatoidalne_zapalenie_stawów", 0.4),
    Fact("dna_moczanowa", 0.3),
    Fact("zespół_niespokojnych_nóg", 0.2),
    Fact("sarkoidoza", 0.1),
    Fact("choroba_addisona", 0.1),
    Fact("histerektomia", 0.1),
    Fact("zespół_cushinga", 0.1),
    Fact("choroba_celiakia", 0.2),
    Fact("zespół_downa", 0.1),
    Fact("fibromialgia", 0.3),
    Fact("niedokrwistość_sierpowata", 0.1),
    Fact("twardzina_układowa", 0.2),
    Fact("zespol_wolff_parkinson_white", 0.1),
    Fact("zespol_williamsa", 0.1),
    Fact("zespół_nieadekwatności_autonomicznej", 0.2),
    Fact("choroba_menierea", 0.1),
    Fact("bezsenność", 0.4),
    Fact("leczenie_hormonalne", 0.3),
    Fact("migotanie_przedsionków", 0),
    Fact("niski_wynik_CHA2DS2-VASc", 0),
    Fact("wysoki_wynik_CHA2DS2-VASc", 1),
    Fact("niewydolność_serca", 1),
    Fact("cukrzyca_typu_2", 1),
    Fact("nadciśnienie", 1),
]

rules = [
    # Reguła dla osób starszych z cukrzycą typu 2, której wynik to rekomendacja inhibitorów ACE
    Rule(
        conditions=[
            Condition("wiek", ">", 0.6),
            Condition("cukrzyca_typu_2", "=", 1),
        ],
        output="inhibitory_ace",
        weight=0.8,
    ),

    # Reguła dla osób z niewydolnością serca, której wynik to rekomendacja antagonistów aldosteronu
    Rule(
        conditions=[
            Condition("niewydolność_serca", "=", 1),
        ],
        output="antagonisty_aldosteronu",
        weight=0.9,
    ),

    # Reguła dla osób z nadciśnieniem tętniczym, której wynik to rekomendacja diuretyków tiazydowych
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
        ],
        output="diuretyki_tiazydowe",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów aldosteronu
    Rule(
        conditions=[
            Condition("choroba_nerek", "=", 1),
            Condition("zaburzenia_elektrolitowe", "=", 1),
        ],
        output="antagonisty_aldosteronu",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do inhibitorów ACE
    Rule(
        conditions=[
            Condition("ciąża", "=", 1),
            Condition("karmienie_piersią", "=", 1),
            Condition("zespół_długo_przedłużonego_qt", "=", 1),
        ],
        output="inhibitory_ace",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do diuretyków tiazydowych
    Rule(
        conditions=[
            Condition("choroba_wątroby", "=", 1),
            Condition("osteoporoza", "=", 1),
            Condition("dna_moczanowa", "=", 1),
        ],
        output="diuretyki_tiazydowe",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów wapnia
    Rule(
        conditions=[
            Condition("zaburzenia_układu_pokarmowego", "=", 1),
            Condition("niedokrwistość_sierpowata", "=", 1),
        ],
        output="antagonisty_wapnia",
        weight=-1.0,
    ),
    # Reguła dla osób z astmą oskrzelową, której wynik to rekomendacja beta-blokerów kardioselektywnych
    Rule(
        conditions=[
            Condition("astma_oskrzelowa", "=", 1),
        ],
        output="beta_blokery_kardioselektywne",
        weight=0.7,
    ),

    # Reguła dla osób z chorobą wieńcową, której wynik to rekomendacja beta-blokerów
    Rule(
        conditions=[
            Condition("choroba_wieńcowa", "=", 1),
        ],
        output="beta_blokery",
        weight=0.9,
    ),

    # Reguła dla osób z tachykardią zatokową, której wynik to rekomendacja antagonistów wapnia
    Rule(
        conditions=[
            Condition("tachykardia_zatokowa", "=", 1),
        ],
        output="antagonisty_wapnia",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do beta-blokerów kardioselektywnych
    Rule(
        conditions=[
            Condition("bradykardia", "=", 1),
            Condition("blok_serca", "=", 1),
            Condition("niewydolność_serca", "=", 1),
        ],
        output="beta_blokery_kardioselektywne",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do beta-blokerów
    Rule(
        conditions=[
            Condition("astma_oskrzelowa", "=", 1),
            Condition("niewydolność_tętnic_nóg", "=", 1),
            Condition("zaburzenia_przewodzenia_serca", "=", 1),
        ],
        output="beta_blokery",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów wapnia
    Rule(
        conditions=[
            Condition("bradykardia", "=", 1),
            Condition("hipotonia", "=", 1),
            Condition("choroba_duhringa", "=", 1),
        ],
        output="antagonisty_wapnia",
        weight=-1.0,
    ),
# Reguła dla osób z obrzękiem płucnym, której wynik to rekomendacja diuretyków pętlowych
    Rule(
        conditions=[
            Condition("obrzęk_płuc", "=", 1),
        ],
        output="diuretyki_pętlowe",
        weight=0.9,
    ),

    # Reguła dla osób z przewlekłymi migotaniem przedsionków, której wynik to rekomendacja antykoagulantów
    Rule(
        conditions=[
            Condition("przewlekłe_migotanie_przedsionków", "=", 1),
        ],
        output="antykoagulanty",
        weight=0.8,
    ),

    # Reguła dla osób z nadciśnieniem opornym, której wynik to rekomendacja antagonistów alfa-1
    Rule(
        conditions=[
            Condition("nadciśnienie_oporne", "=", 1),
        ],
        output="antagonisty_alfa_1",
        weight=0.7,
    ),

    # Reguła dla osób z przeciwwskazaniami do diuretyków pętlowych
    Rule(
        conditions=[
            Condition("ciężka_niewydolność_nerek", "=", 1),
            Condition("ostre_porostowe_zapalenie_wątroby", "=", 1),
        ],
        output="diuretyki_pętlowe",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antykoagulantów
    Rule(
        conditions=[
            Condition("krwawienie", "=", 1),
            Condition("nadwrażliwość", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="antykoagulanty",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów alfa-1
    Rule(
        conditions=[
            Condition("hipotonia", "=", 1),
            Condition("niewydolność_wątroby", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="antagonisty_alfa_1",
        weight=-1.0,
    ),
    # Reguła dla osób z chroniczną niewydolnością nerek, której wynik to rekomendacja inhibitorów SGLT2
    Rule(
        conditions=[
            Condition("przewlekła_niewydolność_nerek", "=", 1),
        ],
        output="inhibitory_sodium_glucose_cotransporter_2",
        weight=0.8,
    ),

    # Reguła dla osób z niewydolnością serca z zachowaną frakcją wyrzutową, której wynik to rekomendacja antagonistów receptora neprilizyny
    Rule(
        conditions=[
            Condition("niewydolność_serca_zachowana_frakcja_wyrzutowa", "=", 1),
        ],
        output="antagonisty_receptora_neprilizyny",
        weight=0.7,
    ),

    # Reguła dla osób z przeciwwskazaniami do inhibitorów SGLT2
    Rule(
        conditions=[
            Condition("cukrzyca_typu_1", "=", 1),
            Condition("ciąża", "=", 1),
            Condition("ostre_zapalenie_trzustki", "=", 1),
        ],
        output="inhibitory_sodium_glucose_cotransporter_2",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów receptora neprilizyny
    Rule(
        conditions=[
            Condition("czynne_zapalenie_mięśnia_serca", "=", 1),
            Condition("hipotonia", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="",
        weight=-1.0,
    ),
    # Reguła dla osób z wysokim ryzykiem choroby wieńcowej, której wynik to rekomendacja leków dwuskładnikowych zawierających ACEI/ARB i CCB
    Rule(
        conditions=[
            Condition("wysokie_ryzyko_choroby_wieńcowej", "=", 1),
        ],
        output="leki_dwuskładnikowe_ACEI_ARB_CCB",
        weight=0.9,
    ),

    # Reguła dla osób z ciężką hipotensją, której wynik to rekomendacja leków dwuskładnikowych zawierających diuretyk i beta-bloker
    Rule(
        conditions=[
            Condition("ciężka_hipotensja", "=", 1),
        ],
        output="leki_dwuskładnikowe_diuretyk_beta_bloker",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do leków dwuskładnikowych zawierających ACEI/ARB i CCB
    Rule(
        conditions=[
            Condition("niewydolność_serca", "=", 1),
            Condition("hiperkaliemia", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="leki_dwuskładnikowe_ACEI_ARB_CCB",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do leków dwuskładnikowych zawierających diuretyk i beta-bloker
    Rule(
        conditions=[
            Condition("astma", "=", 1),
            Condition("zaburzenia_przewodzenia_serca", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="leki_dwuskładnikowe_diuretyk_beta_bloker",
        weight=-1.0,
    ),
    # Reguła dla osób z łagodnym nadciśnieniem tętniczym, której wynik to rekomendacja leków moczopędnych
    Rule(
        conditions=[
            Condition("łagodne_nadciśnienie_tętnicze", "=", 1),
        ],
        output="leki_moczopędne",
        weight=0.7,
    ),

    # Reguła dla osób z migotaniem przedsionków, której wynik to rekomendacja beta-blokerów
    Rule(
        conditions=[
            Condition("migotanie_przedsionków", "=", 1),
        ],
        output="beta_blokery",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do leków moczopędnych
    Rule(
        conditions=[
            Condition("niewydolność_nerek", "=", 1),
            Condition("hiponatremia", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="leki_moczopędne",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do beta-blokerów
    Rule(
        conditions=[
            Condition("astma", "=", 1),
            Condition("zaburzenia_przewodzenia_serca", "=", 1),
            Condition("bradykardia", "=", 1),
        ],
        output="beta_blokery",
        weight=-1.0,
    ),
    # Reguła dla osób z wysokim ryzykiem udaru, której wynik to rekomendacja antagonistów wapnia
    Rule(
        conditions=[
            Condition("wysokie_ryzyko_udaru", "=", 1),
        ],
        output="antagoniści_wapnia",
        weight=0.8,
    ),

    # Reguła dla osób z tętniakiem aorty, której wynik to rekomendacja blokerów kanału wapniowego
    Rule(
        conditions=[
            Condition("tętniak_aorty", "=", 1),
        ],
        output="blokery_kanału_wapniowego",
        weight=0.9,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów wapnia
    Rule(
        conditions=[
            Condition("hipotensja", "=", 1),
            Condition("blok_przedsionkowo-komorowy", "=", 1),
        ],
        output="antagoniści_wapnia",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do blokerów kanału wapniowego
    Rule(
        conditions=[
            Condition("niewydolność_serca", "=", 1),
            Condition("bradykardia", "=", 1),
        ],
        output="blokery_kanału_wapniowego",
        weight=-1.0,
    ),
    # Reguła dla osób z niewydolnością serca, której wynik to rekomendacja inhibitorów ACE
    Rule(
        conditions=[
            Condition("niewydolność_serca", "=", 1),
        ],
        output="inhibitory_ACE",
        weight=0.8,
    ),

    # Reguła dla osób z cukrzycą, której wynik to rekomendacja inhibitorów SGLT2
    Rule(
        conditions=[
            Condition("cukrzyca", "=", 1),
        ],
        output="inhibitory_SGLT2",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do inhibitorów ACE
    Rule(
        conditions=[
            Condition("obrzęk_naczynioruchowy", "=", 1),
            Condition("niewydolność_nerek", "=", 1),
        ],
        output="inhibitory_ACE",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do inhibitorów SGLT2
    Rule(
        conditions=[
            Condition("ciąża", "=", 1),
            Condition("dawka_glomerularna_filtracji", "<", 45),  # GFR < 45 mL/min/1.73 m^2
        ],
        output="inhibitory_SGLT2",
        weight=-1.0,
    ),
    # Reguła dla osób z nadciśnieniem tętniczym, której wynik to rekomendacja diuretyków
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
        ],
        output="diuretyki",
        weight=0.8,
    ),

    # Reguła dla osób z dną moczanową, której wynik to rekomendacja antagonistów receptora V2
    Rule(
        conditions=[
            Condition("dna_moczanowa", "=", 1),
        ],
        output="antagoniści_receptora_V2",
        weight=0.7,
    ),

    # Reguła dla osób z przeciwwskazaniami do diuretyków
    Rule(
        conditions=[
            Condition("hipokaliemia", "=", 1),
            Condition("ciąża", "=", 1),
        ],
        output="diuretyki",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do antagonistów receptora V2
    Rule(
        conditions=[
            Condition("wodonercze", "=", 1),
            Condition("hiponatremia", "=", 1),
        ],
        output="antagoniści_receptora_V2",
        weight=-1.0,
    ),
    # Reguła dla osób z nadciśnieniem tętniczym i cukrzycą, której wynik to rekomendacja leków złożonych: diuretyk + inhibitor SGLT2
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("cukrzyca", "=", 1),
        ],
        output="diuretyk_inhibitor_SGLT2",
        weight=0.9,
    ),

    # Reguła dla osób z nadciśnieniem tętniczym i astmą, której wynik to rekomendacja leków złożonych: diuretyk + beta-bloker
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("astma", "=", 1),
        ],
        output="diuretyk_beta_bloker",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych diuretyk + inhibitor SGLT2
    Rule(
        conditions=[
            Condition("ciąża", "=", 1),
            Condition("dawka_glomerularna_filtracji", "<", 45),  # GFR < 45 mL/min/1.73 m^2
        ],
        output="diuretyk_inhibitor_SGLT2",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych diuretyk + beta-bloker
    Rule(
        conditions=[
            Condition("bradykardia", "=", 1),
            Condition("niewydolność_serca", "=", 1),
        ],
        output="diuretyk_beta_bloker",
        weight=-1.0,
    ),
    # Reguła dla osób z nadciśnieniem tętniczym i dławicą piersiową, której wynik to rekomendacja leków złożonych: kalcynowy antagonist + inhibitor ACE
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("dławica_piersiowa", "=", 1),
        ],
        output="kalcynowy_antagonist_inhibitor_ACE",
        weight=0.9,
    ),

    # Reguła dla osób z nadciśnieniem tętniczym i migreną, której wynik to rekomendacja leków złożonych: beta-bloker + antydepresant
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("migrena", "=", 1),
        ],
        output="beta_bloker_antydepresant",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych kalcynowy antagonist + inhibitor ACE
    Rule(
        conditions=[
            Condition("ciąża", "=", 1),
            Condition("angioedema", "=", 1),
        ],
        output="kalcynowy_antagonist_inhibitor_ACE",
        weight=-1.0,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych beta-bloker + antydepresant
    Rule(
        conditions=[
            Condition("depresja", "=", 1),
            Condition("niewydolność_serca", "=", 1),
        ],
        output="beta_bloker_antydepresant",
        weight=-1.0,
    ),
    # Reguła dla osób z nadciśnieniem tętniczym i cukrzycą, której wynik to rekomendacja leków złożonych: inhibitor ACE + diuretyk
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("cukrzyca", "=", 1),
        ],
        output="inhibitor_ACE_diuretyk",
        weight=0.9,
    ),

    # Reguła dla osób z nadciśnieniem tętniczym i przewlekłą chorobą nerek, której wynik to rekomendacja leków złożonych: inhibitor ACE + diuretyk
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("przewlekła_choroba_nerek", "=", 1),
        ],
        output="inhibitor_ACE_diuretyk",
        weight=0.9,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych inhibitor ACE + diuretyk
    Rule(
        conditions=[
            Condition("ciąża", "=", 1),
            Condition("niewydolność_wątroby", "=", 1),
        ],
        output="inhibitor_ACE_diuretyk",
        weight=-1.0,
    ),

    # Reguła dla osób z nadciśnieniem tętniczym i otyłością, której wynik to rekomendacja leków złożonych: beta-bloker + diuretyk
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("otyłość", "=", 1),
        ],
        output="beta_bloker_diuretyk",
        weight=0.8,
    ),

    # Reguła dla osób z przeciwwskazaniami do stosowania leków złożonych beta-bloker + diuretyk
    Rule(
        conditions=[
            Condition("astma", "=", 1),
            Condition("niewydolność_serca", "=", 1),
        ],
        output="beta_bloker_diuretyk",
        weight=-1.0,
    ),
    # Reguła 18: Rekomendacja antagonistów receptora angiotensyny II (ARB) dla osób z przeciwwskazaniami do inhibitorów ACE (źródło: ESC/ESH 2018)
    Rule(
        conditions=[
            Condition("przeciwwskazania_inhibitory_ACE", "=", 1),
        ],
        output="ARB",
        weight=0.8,
    ),

    # Reguła 19: Rekomendacja inhibitorów reniny dla pacjentów z nadciśnieniem tętniczym, którzy mają nietolerancję na ACEI i ARB (źródło: ESC/ESH 2018)
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("nietolerancja_ACEI_ARB", "=", 1),
        ],
        output="inhibitory_reniny",
        weight=0.7,
    ),

    # Reguła 20: Rekomendacja leków złożonych inhibitorów ACE + CCB (kanałów wapniowych) dla pacjentów z nadciśnieniem tętniczym i miażdżycą tętnic (źródło: ESC/ESH 2018)
    Rule(
        conditions=[
            Condition("nadciśnienie_tętnicze", "=", 1),
            Condition("miażdżyca_tętnic", "=", 1),
        ],
        output="inhibitory_ACE_CCB",
        weight=0.8,
    ),
    # Reguła 21: Rekomendacja leków złożonych zawierających statyny dla pacjentów z ryzykiem sercowo-naczyniowym (źródło: ACC/AHA 2018)
    Rule(
        conditions=[
            Condition("ryzyko_serco-naczyniowe", "=", 1),
        ],
        output="leki_złożone_statyny",
        weight=0.8,
    ),

    # Reguła 22: Rekomendacja leków złożonych zawierających ezetymib dla pacjentów z ryzykiem sercowo-naczyniowym, którzy nie osiągają odpowiednich wartości lipidowych na statynach (źródło: ACC/AHA 2018)
    Rule(
        conditions=[
            Condition("ryzyko_serco-naczyniowe", "=", 1),
            Condition("niewystarczająca_redukcja_lipidów_na_statynach", "=", 1),
        ],
        output="leki_złożone_ezetymib",
        weight=0.7,
    ),

    # Reguła 23: Rekomendacja inhibitorów PCSK9 dla pacjentów z bardzo wysokim ryzykiem sercowo-naczyniowym i wysokim stężeniem cholesterolu LDL (źródło: ACC/AHA 2018)
    Rule(
        conditions=[
            Condition("bardzo_wysokie_ryzyko_serco-naczyniowe", "=", 1),
            Condition("wysokie_stężenie_cholesterolu_LDL", "=", 1),
        ],
        output="inhibitory_PCSK9",
        weight=0.9,
    ),
]


expert_system = ExpertSystem(rules, facts)
input_values = {fact.name: fact.value for fact in facts}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")


"""

inferred_results = expert_system.infer(input_values, method="fuzzy")
print(inferred_results)
W oparciu o "2018 ESC/ESH Guidelines for the management of arterial hypertension" (European Heart Journal, Volume 39, Issue 33, 1 September 2018, Pages 3021–3104) stworzyłem kolejne reguły. 
"""