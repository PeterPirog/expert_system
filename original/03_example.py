from expert import ExpertSystem
from fact import Fact
from condition import Condition
from rule import Rule
from fact import RelationshipFact

# Tworzenie systemu eksperckiego
expert_system = ExpertSystem()

# Dodawanie faktów
facts = [
    Fact("wiek", 0.6),
    Fact("cukrzyca", 0.8),
    Fact("choroba_nerek", 0.4),
    Fact("ciąża", 0.0),
    RelationshipFact("ryzyko_niewydolności_serca", 0.7, "wiek", "cukrzyca", "positive_correlation", 0.8),
]

for fact in facts:
    expert_system.add_fact(fact)

# Dodawanie reguł wnioskowania
conditions = [
    Condition("wiek", "high"),
    Condition("cukrzyca", "high"),
    Condition("choroba_nerek", "high"),
    Condition("ciąża", "high"),
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
]

for rule in rules:
    expert_system.add_rule(rule)

# Sprawdzanie sprzeczności reguł
conflicting_rules = expert_system.check_conflicting_rules()
if conflicting_rules:
    print("Znaleziono sprzeczne reguły:")
    for rule1, rule2 in conflicting_rules:
        print(f"{rule1} <-> {rule2}")
else:
    print("Nie znaleziono sprzecznych reguł")

# Wnioskowanie
input_values = {
    "wiek": 0.6,
    "cukrzyca": 0.8,
    "choroba_nerek": 0.4,
    "ciąża": 0.0,
}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Rekomendacja leków hipotensyjnych (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")
