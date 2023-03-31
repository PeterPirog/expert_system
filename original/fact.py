class Fact:
    def __init__(self, name, value, membership_degree=1.0):
        self.name = name
        self.value = value
        self.membership_degree = membership_degree

    def __str__(self):
        return f"{self.name}: {self.value} (degree: {self.membership_degree})"

class RelationshipFact(Fact):
    def __init__(self, name, value, element_a, element_b, relationship_type, relationship_degree):
        super().__init__(name, value)
        self.element_a = element_a
        self.element_b = element_b
        self.relationship_type = relationship_type
        self.relationship_degree = relationship_degree

    def __repr__(self):
        return f"{self.element_a} {self.relationship_type} {self.element_b} (degree: {self.relationship_degree}, value: {self.value})"

"""
Polecenie RelationshipFact("ryzyko_niewydolności_serca", 0.7, "wiek", "cukrzyca", "positive_correlation", 0.8) tworzy nowy obiekt klasy RelationshipFact, który przechowuje informacje o związku między dwoma elementami (w tym przypadku wiek i cukrzyca) oraz stopień tego związku.

Oto wyjaśnienie poszczególnych parametrów:

"ryzyko_niewydolności_serca": nazwa faktu, który opisuje związek między wiekiem a cukrzycą w kontekście ryzyka niewydolności serca.
0.7: wartość tego faktu, wskazująca, jak istotny jest dla analizy. Wartość 0.7 oznacza, że związek między wiekiem a cukrzycą ma istotny wpływ na ryzyko niewydolności serca (w skali od 0 do 1).
"wiek": pierwszy element związku, w tym przypadku wiek pacjenta.
"cukrzyca": drugi element związku, w tym przypadku obecność cukrzycy u pacjenta.
"positive_correlation": rodzaj relacji między dwoma elementami. W tym przypadku relacja to pozytywna korelacja, co oznacza, że wzrost jednej cechy (np. wieku) jest związany ze wzrostem drugiej cechy (np. ryzyka cukrzycy).
0.8: stopień relacji między dwoma elementami, w skali od 0 do 1. Wartość 0.8 oznacza silną pozytywną korelację między wiekiem a cukrzycą w kontekście ryzyka niewydolności serca.


Klasa Fact jest prostą klasą przechowującą informacje o fakcie. Posiada trzy atrybuty: name, value oraz membership_degree. Metoda __str__ pozwala na łatwe wypisanie faktu jako łańcucha znaków.

Fakty są używane w systemach eksperckich do przechowywania znanych informacji. W kontekście wnioskowania bayesowskiego, wartość value może reprezentować prawdopodobieństwo aprioryczne. W kontekście wnioskowania opartego na logice rozmytej, membership_degree może reprezentować stopień przynależności do określonej kategorii lub klasy.
"""