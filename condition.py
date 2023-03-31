"""
class Condition:
    def __init__(self, variable, operator, value):
        self.variable = variable
        self.operator = operator
        self.value = value

    def evaluate(self, input_values):
        fact_value = input_values.get(self.fact_name, 0)
        if self.category == "high":
            return fact_value
        elif self.category == "low":
            return 1 - fact_value
        else:
            raise ValueError(f"Unknown category: {self.category}")

    def __str__(self):
        return f"{self.variable} {self.operator} {self.value}"

"""

class Condition:
    def __init__(self, fact_name, operator, value):
        self.fact_name = fact_name
        self.operator = operator
        self.value = value

    def evaluate(self, input_values):
        fact_value = input_values.get(self.fact_name, 0)
        if self.operator == ">":
            return fact_value > self.value
        elif self.operator == "<":
            return fact_value < self.value
        elif self.operator == "==":
            return fact_value == self.value
        elif self.operator == "!=":
            return fact_value != self.value
        elif self.operator == ">=":
            return fact_value >= self.value
        elif self.operator == "<=":
            return fact_value <= self.value
        else:
            return False
