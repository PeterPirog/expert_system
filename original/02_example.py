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
    Rule(conditions[0], "ACEI", 0.7),
    Rule(conditions[1], "ARB", 0.9),
    Rule(conditions[2], "Diuretyki", 0.5),
    Rule(conditions[3], "CCB", 0.6),
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
