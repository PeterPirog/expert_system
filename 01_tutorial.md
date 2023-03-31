Oto tutorial dla pliku 01_example.py skonwertowany na format Markdown:

perl
Copy code
# Tutorial do pliku 01_example.py

## 1. Dodawanie faktów

W celu dodania faktów do systemu eksperckiego, należy najpierw utworzyć obiekty klasy `Fact`. Fakt składa się z nazwy i wartości przynależności (zakres od 0 do 1). Następnie dodaj fakty do systemu eksperckiego, korzystając z metody `add_fact`.

```python
facts = [
    Fact("Ciepła woda", 0.9),
    Fact("Zimna woda", 0.1),
]

for fact in facts:
    expert_system.add_fact(fact)
2. Dodawanie reguł wnioskowania
Reguły wnioskowania składają się z warunków i konkluzji. Warunki są reprezentowane przez obiekty klasy Condition, które zawierają nazwę faktów oraz kategorię (na przykład "high" lub "low"). Następnie utwórz reguły, używając obiektów Condition oraz określając konkluzję i wartość prawdy dla reguł. Dodaj reguły do systemu eksperckiego, korzystając z metody add_rule.

python
Copy code
conditions = [
    Condition("Ciepła woda", "high"),
    Condition("Zimna woda", "low"),
]

rules = [
    Rule(conditions[0], "Niska energia", 0.9),
    Rule(conditions[1], "Wysoka energia", 0.7),
]

for rule in rules:
    expert_system.add_rule(rule)
3. Sprawdzanie sprzeczności reguł
Aby sprawdzić, czy w systemie eksperckim występują sprzeczne reguły, użyj metody check_conflicting_rules. Jeśli metoda zwróci listę niepustych par reguł, oznacza to, że te reguły są sprzeczne.

python
Copy code
conflicting_rules = expert_system.check_conflicting_rules()
if conflicting_rules:
    print("Znaleziono sprzeczne reguły:")
    for rule1, rule2 in conflicting_rules:
        print(f"{rule1} <-> {rule2}")
else:
    print("Nie znaleziono sprzecznych reguł")
4. Wnioskowanie
W celu wnioskowania na podstawie wiedzy eksperckiej, przygotuj słownik zawierający wartości faktów wejściowych. Następnie użyj metody infer systemu eksperckiego, podając wartości wejściowe i wybierając metodę wnioskowania (na przykład "fuzzy" dla logiki rozmytej).

python
Copy code
input_values = {
    "Ciepła woda": 0.9,
    "Zimna woda": 0.1,
}

inferred_results = expert_system.infer(input_values, method="fuzzy")
print("Wnioskowanie na podstawie wiedzy eksperckiej (metoda fuzzy):")
for conclusion, truth_value in inferred_results.items():
    print(f"{conclusion}: {truth_value}")