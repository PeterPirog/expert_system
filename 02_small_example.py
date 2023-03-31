from expert import ExpertSystem
from rule import Rule
from fact import Fact, RelationshipFact
from condition import Condition
from typing import List

# Dodawanie faktów
facts = [
    Fact("nadciśnienie_tętnicze", 0.9),
    Fact("niewydolność_serca", 1),
    Fact("choroba_wieńcowa", 0.5),
    Fact("cukrzyca_typu_1", 0.4),
    Fact("cukrzyca_typu_2", 1.0),
    Fact("przewlekła_niewydolność_nerek", 0.3),
    Fact("nerkowe_nadciśnienie_tętnicze", 0.5),
    Fact("wtórne_nadciśnienie_tętnicze", 0.3),
    Fact("nadciśnienie_lekooporne", 0.2),
    Fact("obwodowe_niedokrwienie_tętnic", 0.4),
    Fact("niedokrwienie_mózgu", 0.3),
    Fact("arytmia", 0.6),
    Fact("migotanie_przedsionków", 0),
    Fact("niski_wynik_CHA2DS2-VASc", 0),
    Fact("wysoki_wynik_CHA2DS2-VASc", 1),
    Fact("zespół_metaboliczny", 0.7),
    Fact("dyslipidemia", 0.7),
    Fact("otyłość", 0.6),
    Fact("palenie", 0.6),
    Fact("brak_aktywności_fizycznej", 0.5),
    Fact("alkohol", 0.4),
    Fact("stres", 0.5),
    Fact("depresja", 0.4),
    Fact("bezsenność", 0.4),
    Fact("wiek", 0.8),
    Fact("płeć", 0.5),
    Fact("choroba_nerek", 0.4),
    Fact("ciąża", 0.0),
    Fact("karmienie_piersią", 0.0),
    Fact("astma", 0.3),
    Fact("wcześniejsze_udary_mózgu", 0.2),
    Fact("migrena", 0.3),
    Fact("choroba_wątroby", 0.2),
    Fact("zaburzenia_elektrolitowe", 0.4),
    Fact("przewlekła_obturacyjna_cholecytka_naciekowa", 0.2),
    Fact("zaburzenia_układu_pokarmowego", 0.4),
    Fact("nadwrażliwość_na_leki", 0.3),
    Fact("anemia", 0.4),
    Fact("osteoporoza", 0.4),
    Fact("niedoczynność_tarczycy", 0.3),
    Fact("nadczynność_tarczycy", 0.2),
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
    Fact("leczenie_hormonalne", 0.3),
]

rules = [
    # Reguła dla osób starszych z cukrzycą typu 2, której wynik to rekomendacja inhibitorów ACE
    Rule(
        [Condition("wiek", ">", 0.6),
         Condition("cukrzyca_typu_2", "=", 1)],
        {"inhibitory_ace": 0.8},
    ),

    # Reguła dla osób z niewydolnością serca, której wynik to rekomendacja antagonistów aldosteronu
    Rule(
        [Condition("niewydolność_serca", "=", 1)],
        {"antagonisty_aldosteronu": 0.9},
    ),

    # Reguła dla osób z nadciśnieniem tętniczym, której wynik to rekomendacja diuretyków tiazydowych
    Rule(
        [Condition("nadciśnienie_tętnicze", "=", 1)],
        {"diuretyki_tiazydowe": 0.8},
    ),

    # ...
]


expert_system = ExpertSystem(rules, facts)
input_values = {fact.name: fact.value for fact in facts}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")
