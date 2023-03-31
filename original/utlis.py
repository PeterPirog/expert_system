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


"""
W pliku utils.py, zdefiniowałem dwie funkcje pomocnicze: cosine_similarity i aggregate_results.

Funkcja cosine_similarity oblicza podobieństwo kosinusowe między dwoma wektorami. Może być używana, jeśli chcesz porównać podobieństwo między wartościami wejściowymi lub wynikami.

Funkcja aggregate_results agreguje wiele wyników wnioskowania (na przykład z różnych systemów eksperckich lub różnych metod wnioskowania) w jeden wynik końcowy. Obsługuje dwa metody agregacji: max (maksimum) i average (średnia). W przypadku metody max, dla każdej konkluzji wybierana jest wartość o najwyższym stopniu przynależności lub prawdopodobieństwie. W przypadku metody average, wartości są sumowane i dzielone przez liczbę wyników, co daje średnią wartość dla każdej konkluzji.

Możesz dostosować te funkcje lub dodać dodatkowe funkcje pomocnicze, które mogą być użyte w systemie eksperckim, aby lepiej obsłużyć specyficzne wymagania Twojego problemu.

"""