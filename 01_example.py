"""
W tym przykładzie stworzono bazę faktów i bazę reguł wnioskowania, a następnie zainicjowano system ekspercki z tymi danymi. Przedstawiono również sposób sprawdzenia, czy w systemie eksperckim występują sprzeczne reguły. Wreszcie, zaprezentowano przykład wnioskowania na podstawie wiedzy eksperckiej, używając metody opartej na logice rozmytej.

Upewnij się, że zaimplementowałeś klasę Condition w swoim module, aby ten przykład działał poprawnie. Warto zauważyć, że w tym przykładzie nie używamy danych eksperymentalnych, ale w rzeczywistym zastosowaniu można je uwzględnić, podając je jako argument do metody infer.

from expert import ExpertSystem
from fact import Fact
from rule import Rule
from condition import Condition

# Tworzenie bazy faktów
facts = [
    Fact("Ciepła woda", 0.9),
    Fact("Zimna woda", 0.1),
]

# Tworzenie bazy reguł wnioskowania
conditions = [
    Condition("Ciepła woda", "high"),
    Condition("Zimna woda", "low"),
]

rules = [
    Rule(conditions[0], "Niska energia", 0.9),
    Rule(conditions[1], "Wysoka energia", 0.7),
]

# Inicjalizacja systemu eksperckiego
expert_system = ExpertSystem()

# Dodawanie faktów i reguł do systemu eksperckiego
for fact in facts:
    expert_system.add_fact(fact)

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

# Przykład wnioskowania na podstawie wiedzy eksperckiej
input_values = {
    "Ciepła woda": 0.9,
    "Zimna woda": 0.1,
}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")


"""
from expert import ExpertSystem
from fact import Fact
from rule import Rule
from condition import Condition

# Tworzenie bazy faktów
facts = [
    Fact("Ciepła woda", 0.9),
    Fact("Zimna woda", 0.1),
]

# Tworzenie bazy reguł wnioskowania
conditions = [
    Condition("Ciepła woda", "high", 0.9),
    Condition("Zimna woda", "low", 0.1),
]

rules = [
    Rule(conditions[0], {"Niska energia": 0.9}),
    Rule(conditions[1], {"Wysoka energia": 0.7}),
]

# Inicjalizacja systemu eksperckiego
expert_system = ExpertSystem(rules, facts)

# Sprawdzanie sprzeczności reguł
conflicting_rules = expert_system.check_conflicting_rules()
if conflicting_rules:
    print("Znaleziono sprzeczne reguły:")
    for rule1, rule2 in conflicting_rules:
        print(f"{rule1} <-> {rule2}")
else:
    print("Nie znaleziono sprzecznych reguł")

# Przykład wnioskowania na podstawie wiedzy eksperckiej
input_values = {
    "Ciepła woda": 0.9,
    "Zimna woda": 0.1,
}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")
