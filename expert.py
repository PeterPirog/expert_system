from rule import Rule
from fact import Fact
from inference import InferenceEngine


class ExpertSystem:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts
        self.inference_engine = InferenceEngine()

    def add_rule(self, rule):
        if not isinstance(rule, Rule):
            raise ValueError("Input must be an instance of Rule class.")
        self.rules.append(rule)

    def add_fact(self, fact):
        if not isinstance(fact, Fact):
            raise ValueError("Input must be an instance of Fact class.")
        self.facts.append(fact)

    def check_conflicting_rules(self):
        conflicting_rules = []
        for i, rule1 in enumerate(self.rules):
            for rule2 in self.rules[i + 1:]:
                if rule1.is_conflicting(rule2):
                    conflicting_rules.append((rule1, rule2))
        return conflicting_rules

    def infer(self, input_values, method="fuzzy"):
        if method not in ["fuzzy", "bayesian"]:
            raise ValueError("Inference method must be either 'fuzzy' or 'bayesian'.")

        if method == "fuzzy":
            return self.inference_engine.fuzzy_inference(self.rules, input_values)
        elif method == "bayesian":
            prior_probabilities = {fact.name: fact.value for fact in self.facts}
            return self.inference_engine.bayesian_inference(self.rules, input_values, prior_probabilities)
