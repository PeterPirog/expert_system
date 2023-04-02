from typing import Dict, List, Tuple
from condition import Condition
from rule import Rule
import itertools


class ExpertSystem:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

    def check_conflicting_rules(self, input_values: Dict[str, float]) -> List[Tuple[Rule, Rule]]:
        def _is_condition_subset(cond1, cond2, inputs):
            for c1 in cond1:
                found = False
                for c2 in cond2:
                    if c1.get_fact_name() == c2.get_fact_name() and c1.check(inputs[c1.get_fact_name()]) == c2.check(
                            inputs[c2.get_fact_name()]):
                        found = True
                        break
                if not found:
                    return False
            return True

        conflicting_rules = []
        for rule1, rule2 in itertools.combinations(self.rules, 2):
            rule1_conditions = [list(c) for c in itertools.product(*[cond.expand() for cond in rule1.conditions])]
            rule2_conditions = [list(c) for c in itertools.product(*[cond.expand() for cond in rule2.conditions])]

            for conditions1, conditions2 in itertools.product(rule1_conditions, rule2_conditions):
                if _is_condition_subset(conditions1, conditions2, input_values):
                    temp_rule1 = Rule("TempRule1", conditions1, rule1.conclusions)
                    temp_rule2 = Rule("TempRule2", conditions2, rule2.conclusions)
                    if self._has_conflicting_conclusions(temp_rule1, temp_rule2):
                        conflicting_rules.append((rule1, rule2))
        return conflicting_rules

    def infer(self, fact_values):
        inferred_values = {}

        for rule in self.rules:
            truth_value = rule.evaluate(fact_values)

            for conclusion, conclusion_value in rule.conclusions.items():
                if conclusion not in inferred_values or truth_value * conclusion_value > inferred_values[conclusion]:
                    inferred_values[conclusion] = truth_value * conclusion_value

        return inferred_values

    def _has_conflicting_conclusions(self, rule1, rule2):
        for key in rule1.conclusions:
            if key in rule2.conclusions and rule1.conclusions[key] != rule2.conclusions[key]:
                return True
        return False
    def print_conflicting_rules(self, input_values: Dict[str, float]) -> None:
        conflicting_rules = self.check_conflicting_rules(input_values)
        if conflicting_rules:
            print("Znaleziono sprzeczne reguły:")
            seen_conflicts = set()
            for rule1, rule2 in conflicting_rules:
                if (rule1.name, rule2.name) not in seen_conflicts and (rule2.name, rule1.name) not in seen_conflicts:
                    print(f"{rule1.name}: {rule1}")
                    print(f"{rule2.name}: {rule2}")
                    print("---")
                    seen_conflicts.add((rule1.name, rule2.name))
        else:
            print("Nie znaleziono sprzecznych reguł.")