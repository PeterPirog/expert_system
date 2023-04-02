from expert import ExpertSystem
from rule import Rule
from condition import Condition, OR
from fact import Fact
from rules import rules

# Zdefiniowanie faktów
facts = [Fact("skurcz_oskrzeli", 0.9), Fact("dusznosc", 0.7), Fact("wheezing", 0.8), Fact("kaszel", 0.5)]


# Tworzenie systemu eksperckiego
expert_system = ExpertSystem(rules, facts)

input_values = {fact.name: fact.value for fact in facts}

# Sprawdzanie sprzecznych reguł
expert_system.print_conflicting_rules(input_values)

# Wnioskowanie
inferred_results = expert_system.infer(input_values)

print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")

