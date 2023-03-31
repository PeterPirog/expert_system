class Condition:
    def __init__(self, fact_name, category):
        self.fact_name = fact_name
        self.category = category

    def evaluate(self, input_values):
        fact_value = input_values.get(self.fact_name, 0)
        if self.category == "high":
            return fact_value
        elif self.category == "low":
            return 1 - fact_value
        else:
            raise ValueError(f"Unknown category: {self.category}")

    def __str__(self):
        return f"{self.fact_name} ({self.category})"

"""
Klasa Condition jest prostą klasą przechowującą informacje o warunku w regule. Posiada dwa atrybuty: fact_name i category. Metoda __str__ pozwala na łatwe wypisanie warunku jako łańcucha znaków.
"""