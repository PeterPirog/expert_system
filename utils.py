import numpy as np


def cosine_similarity(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm == 0 or b_norm == 0:
        return 0
    return np.dot(a, b) / (a_norm * b_norm)


def aggregate_results(results, method='max'):
    if method not in ['max', 'average']:
        raise ValueError("Aggregation method must be either 'max' or 'average'.")

    aggregated_results = {}

    for result in results:
        for key, value in result.items():
            if method == 'max':
                aggregated_results[key] = max(aggregated_results.get(key, 0), value)
            elif method == 'average':
                aggregated_results[key] = aggregated_results.get(key, 0) + value / len(results)

    return aggregated_results
