from condition import Condition
from typing import Dict, List

class Rule:
    def __init__(self, conditions: List[Condition], conclusions: Dict[str, float]):
        self.conditions = conditions
        self.conclusions = conclusions

    def __str__(self):
        return f"{self.conditions} -> {self.conclusions}"

    def fire(self, input_values: Dict[str, float]) -> Dict[str, float]:
        min_truth_value = 1.0
        for condition in self.conditions:
            truth_value = condition.evaluate(input_values)
            min_truth_value = min(min_truth_value, truth_value)
        return {conclusion: min_truth_value * weight for conclusion, weight in self.conclusions.items()}

    def is_conflicting(self, other: 'Rule') -> bool:
        conflicting_conditions = []
        for self_condition in self.conditions:
            for other_condition in other.conditions:
                if self_condition.is_conflicting(other_condition):
                    conflicting_conditions.append((self_condition, other_condition))
        return len(conflicting_conditions) > 0
