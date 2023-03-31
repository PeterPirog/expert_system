class Fact:
    def __init__(self, name, value, membership_degree=1.0):
        self.name = name
        self.value = value
        self.membership_degree = membership_degree

    def __str__(self):
        return f"{self.name}: {self.value} (degree: {self.membership_degree})"

"""
Klasa Fact jest prostą klasą przechowującą informacje o fakcie. Posiada trzy atrybuty: name, value oraz membership_degree. Metoda __str__ pozwala na łatwe wypisanie faktu jako łańcucha znaków.

Fakty są używane w systemach eksperckich do przechowywania znanych informacji. W kontekście wnioskowania bayesowskiego, wartość value może reprezentować prawdopodobieństwo aprioryczne. W kontekście wnioskowania opartego na logice rozmytej, membership_degree może reprezentować stopień przynależności do określonej kategorii lub klasy.
"""