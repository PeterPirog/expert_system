"""

"""
from expert import ExpertSystem
from rule import Rule
from condition import Condition, OR
from fact import Fact

# Zdefiniowanie faktów
facts = [
    Fact("skurcz_oskrzeli", 0.9),
    Fact("dusznosc", 0.7),
    Fact("wheezing", 0.8),
    Fact("kaszel", 0.5),
]

# Zdefiniowanie reguł
rules = [
    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            Condition("kaszel", "==", 0.5),
        ],
        conclusions={"inhibitory_ace": 0.7}
    ),
    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.6),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            Condition("kaszel", "==", 0.5),
        ],
        conclusions={"inhibitory_ace": 0.1}
    ),

    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            OR(Condition("kaszel", "<=", 0.4),Condition("kaszel", ">=", 0.6)),
        ],
        conclusions={"wariant2": 0.7}
    ),
    # Dodaj te reguły do listy reguł
    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
        ],
        conclusions={"lekarstwo_A": 0.7}
    ),
    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
        ],
        conclusions={"lekarstwo_A": 0.8}
    ),
]

# Tworzenie systemu eksperckiego
expert_system = ExpertSystem(rules, facts)


input_values = {fact.name: fact.value for fact in facts}

# Sprawdzanie sprzecznych reguł
conflicting_rules = expert_system.check_conflicting_rules(input_values)
if conflicting_rules:
    print("Znaleziono sprzeczne reguły:")
    for rule1, rule2 in conflicting_rules:
        print(f"Reguła 1: {rule1}")
        print(f"Reguła 2: {rule2}")
        print("---")
else:
    print("Nie znaleziono sprzecznych reguł.")

# Wnioskowanie
inferred_results = expert_system.infer(input_values)

print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")
