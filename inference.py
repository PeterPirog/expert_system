import skfuzzy as fuzz
from rule import Rule
from collections import defaultdict


class InferenceEngine:
    def __init__(self):
        pass

    def fuzzy_inference(self, rules, input_values):
        aggregated_conclusions = defaultdict(float)

        for rule in rules:
            fired_rule = rule.fire(input_values)
            for conclusion, truth_value in fired_rule.items():
                aggregated_conclusions[conclusion] = max(aggregated_conclusions[conclusion], truth_value)

        return aggregated_conclusions

    def bayesian_inference(self, rules, input_values, prior_probabilities):
        aggregated_conclusions = defaultdict(float)

        for rule in rules:
            likelihood = rule.evaluate(input_values)
            conclusion = rule.conclusion

            aggregated_conclusions[conclusion] += likelihood * prior_probabilities.get(conclusion, 0)

        normalization_factor = sum(aggregated_conclusions.values())
        if normalization_factor == 0:
            return prior_probabilities

        posterior_probabilities = {k: v / normalization_factor for k, v in aggregated_conclusions.items()}
        return posterior_probabilities
