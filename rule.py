from condition import Condition,OR
from typing import Dict, List
from typing import Dict, List, Union
from condition import Condition

class Rule:
    def __init__(
        self,
        name: str,
        conditions: List[Union[Condition, "OR"]],
        conclusions: Dict[str, float],
    ):
        self.name = name
        self.conditions = conditions
        self.conclusions = conclusions

    def evaluate(self, fact_values):
        if len(self.conditions) == 0:
            return 0.0

        truth_values = []

        for condition in self.conditions:
            if isinstance(condition, OR):
                or_truth_values = [c.evaluate(fact_values) for c in condition.conditions]
                truth_values.append(max(or_truth_values))
            else:
                truth_values.append(condition.evaluate(fact_values))

        return min(truth_values)

    def __str__(self):
        conditions_str = " AND ".join(str(condition) for condition in self.conditions)
        conclusions_str = ", ".join(f"{key}: {value}" for key, value in self.conclusions.items())
        return f"IF {conditions_str} THEN ({conclusions_str})"

"""
class Rule:
    def __init__(self, conditions: List[Condition], conclusions: Dict[str, float]):
        self.conditions = conditions
        self.conclusions = conclusions

    def __str__(self):
        return f"{self.conditions} -> {self.conclusions}"

    def fire(self, input_values: Dict[str, float]) -> Dict[str, float]:
        min_truth_value = 1.0
        for condition in self.conditions:
            if isinstance(condition, OR):
                truth_value = condition.evaluate(input_values)
            else:
                truth_value = condition.evaluate(input_values)
            min_truth_value = min(min_truth_value, truth_value)
        return {conclusion: min_truth_value * weight for conclusion, weight in self.conclusions.items()}

    def is_conflicting(self, other: 'Rule') -> bool:
        return set(self.conditions) == set(other.conditions) and self.conclusions != other.conclusions

    def evaluate(self, input_values: Dict[str, float]) -> float:
        truth_value = 1.0
        for condition in self.conditions:
            truth_value = min(truth_value, condition.evaluate(input_values))
            if truth_value == 0.0:
                break
        return truth_value

"""