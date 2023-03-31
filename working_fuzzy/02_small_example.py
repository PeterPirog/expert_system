"""

"""
from expert import ExpertSystem
from rule import Rule
from condition import Condition
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
            Condition("kaszel", ">", 0.5),
        ],
        conclusions={"inhibitory_ace": 0.7}
    ),
    Rule(
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            Condition("kaszel", "<=", 0.5),
        ],
        conclusions={"wariant2": 0.7}
    ),
]

# Tworzenie systemu eksperckiego
expert_system = ExpertSystem(rules, facts)

# Wnioskowanie
input_values = {fact.name: fact.value for fact in facts}
inferred_results = expert_system.infer(input_values)

print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")
