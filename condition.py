from typing import Dict, List, Union

class Condition:
    def __init__(self, fact_name: str, operator: str, value: float):
        self._fact_name = fact_name
        self._operator = operator
        self._value = value

    def __str__(self):
        return f"({self._fact_name}, {self._operator}, {self._value})"

    def expand(self):
        return [self]

    def evaluate(self, fact_values: Dict[str, float]) -> float:
        if self._fact_name not in fact_values:
            raise ValueError(f"Fakt {self._fact_name} nie istnieje w bazie faktów.")

        fact_value = fact_values[self._fact_name]

        if self._operator == ">":
            return float(fact_value > self._value)
        elif self._operator == "<":
            return float(fact_value < self._value)
        elif self._operator == ">=":
            return float(fact_value >= self._value)
        elif self._operator == "<=":
            return float(fact_value <= self._value)
        elif self._operator == "==":
            return float(fact_value == self._value)
        else:
            raise ValueError(f"Nieznany operator: {self._operator}")

    def get_fact_name(self):
        return self._fact_name

    def check(self, input_value):
        if self._operator == "<":
            return input_value < self._value
        elif self._operator == "<=":
            return input_value <= self._value
        elif self._operator == ">":
            return input_value > self._value
        elif self._operator == ">=":
            return input_value >= self._value
        elif self._operator == "==":
            return input_value == self._value
        elif self._operator == "!=":
            return input_value != self._value
        else:
            raise ValueError(f"Nieznany operator: {self._operator}")

class OR:
    def __init__(self, *conditions):
        self.conditions = conditions

    def expand(self):
        expanded_conditions = []
        for cond in self.conditions:
            expanded_conditions.extend(cond.expand())
        return expanded_conditions

    def __str__(self):
        return " OR ".join([str(cond) for cond in self.conditions])
