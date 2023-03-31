"""
class Rule:
    def __init__(self, conditions, output, weight=1.0):
        self.conditions = conditions
        self.output = output
        self.weight = weight

    def __str__(self):
        return f"IF {self.condition} THEN {self.conclusion} (degree: {self.membership_degree})"

    def is_conflicting(self, other_rule):
        return (
            self.condition == other_rule.condition
            and self.conclusion != other_rule.conclusion
            and self.membership_degree > 0
            and other_rule.membership_degree > 0
        )

    def evaluate(self, input_values):
        truth_value = self.condition.evaluate(input_values)
        return truth_value * self.membership_degree

    def fire(self, input_values):
        truth_value = self.evaluate(input_values)
        return {self.conclusion: truth_value}



"""
"""
class Rule:
    def __init__(self, conditions, output, weight=1.0):
        self.conditions = conditions
        self.output = output
        self.weight = weight

    def evaluate(self, input_values):
        truth_values = [condition.evaluate(input_values) for condition in self.conditions]
        return min(truth_values)

    def fire(self, input_values):
        truth_value = self.evaluate(input_values)
        if truth_value:
            return {conclusion.fact_name: (conclusion.value, truth_value * self.weight)
                    for conclusion in self.conclusions}
        else:
            return {}

"""

class Rule:
    def __init__(self, condition: Condition, conclusions: Dict[str, float]):
        self.condition = condition
        self.conclusions = conclusions

    def __str__(self):
        return f"{self.condition} -> {self.conclusions}"

    def fire(self, input_values: Dict[str, float]) -> Dict[str, float]:
        truth_value = self.condition.evaluate(input_values)
        return {conclusion: truth_value * weight for conclusion, weight in self.conclusions.items()}

    def is_conflicting(self, other: 'Rule') -> bool:
        conflicting_conditions = []
        for key, value in self.condition.input_values.items():
            if key in other.condition.input_values and value != other.condition.input_values[key]:
                conflicting_conditions.append(key)
        return len(conflicting_conditions) > 0
