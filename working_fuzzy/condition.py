"""
class Condition:
    def __init__(self, fact_name, operator, value):
        self.fact_name = fact_name
        self.operator = operator
        self.value = value

    def compute_membership(self, fact_value):
        if self.operator == ">":
            return max(fact_value - self.value, 0)
        elif self.operator == "<":
            return max(self.value - fact_value, 0)
        elif self.operator == "==":
            return 1 - abs(fact_value - self.value)
        elif self.operator == "!=":
            return abs(fact_value - self.value)
        elif self.operator == ">=":
            return max(fact_value - self.value + 1, 0)
        elif self.operator == "<=":
            return max(self.value - fact_value + 1, 0)
        else:
            return 0

    def evaluate(self, input_values):
        fact_value = input_values.get(self.fact_name, 0)
        return self.compute_membership(fact_value)

"""


class Condition:
    def __init__(self, fact_name, operator, value):
        self.fact_name = fact_name
        self.operator = operator
        self.value = value

    def evaluate(self, input_values):
        fact_value = input_values.get(self.fact_name, 0)
        if self.operator == ">":
            return 1.0 if fact_value > self.value else 0.0
        elif self.operator == "<":
            return 1.0 if fact_value < self.value else 0.0
        elif self.operator == "==":
            return 1.0 if fact_value == self.value else 0.0
        elif self.operator == "!=":
            return 1.0 if fact_value != self.value else 0.0
        elif self.operator == ">=":
            return 1.0 if fact_value >= self.value else 0.0
        elif self.operator == "<=":
            return 1.0 if fact_value <= self.value else 0.0
        else:
            return 0.0

