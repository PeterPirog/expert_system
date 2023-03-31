class Rule:
    def __init__(self, condition, conclusion, membership_degree=1.0):
        self.condition = condition
        self.conclusion = conclusion
        self.membership_degree = membership_degree

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
W tej implementacji, klasa Rule posiada trzy atrybuty: condition, conclusion i membership_degree. Metoda __str__ pozwala na łatwe wypisanie reguły jako łańcucha znaków.

Metoda is_conflicting sprawdza, czy dwie reguły są sprzeczne, czyli mają takie same warunki, różne konkluzje oraz obie mają dodatni stopień przynależności.

Metoda evaluate oblicza wartość prawdy reguły na podstawie wartości wejściowych. Wartość prawdy jest mnożona przez stopień przynależności, aby uwzględnić reguły o różnych poziomach pewności.

Metoda fire jest używana do wywoływania reguły. Oblicza wartość prawdy na podstawie wartości wejściowych i zwraca słownik z konkluzją jako kluczem i wartością prawdy jako wartością.

Aby użyć tej klasy Rule, będziesz musiał zaimplementować również klasę Condition, która będzie miała metodę evaluate przyjmującą wartości wejściowe i zwracającą wartość prawdy warunku. To pozwoli na ocenę reguł na podstawie danych wejściowych.

"""