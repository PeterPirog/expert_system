from typing import Dict, List, Tuple

from rule import Rule
from condition import Condition

class ExpertSystem:
    def __init__(self, rules: List[Rule], facts: List["Fact"]):
        self.rules = rules
        self.facts = facts

    def infer(self, input_values: Dict[str, float]) -> Dict[str, float]:
        conclusions = {}
        for rule in self.rules:
            truth_value = rule.evaluate(input_values)
            if truth_value > 0:
                for conclusion, conclusion_value in rule.conclusions.items():
                    if conclusion not in conclusions or conclusions[conclusion] < conclusion_value * truth_value:
                        conclusions[conclusion] = conclusion_value * truth_value
        return conclusions

    def check_conflicting_rules(self, input_values: Dict[str, float]) -> List[Tuple[Rule, Rule]]:
        conflicting_rules = []

        for i, rule1 in enumerate(self.rules):
            for rule2 in self.rules[i+1:]:
                for conclusion in rule1.conclusions:
                    if conclusion in rule2.conclusions:
                        rule1_truth_value = rule1.evaluate(input_values)
                        rule2_truth_value = rule2.evaluate(input_values)

                        if rule1_truth_value > 0 and rule2_truth_value > 0 and rule1.conclusions[conclusion] != rule2.conclusions[conclusion]:
                            conflicting_rules.append((rule1, rule2))

        return conflicting_rules


