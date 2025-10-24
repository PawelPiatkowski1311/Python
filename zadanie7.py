#!/usr/bin/python3

from math import sqrt # Zaimportowanie funkcji sqrt() z biblioteki math

# Zdefiniowanie funkcji obliczającej pierwiastki kwadratowe
def squareRoot(a, b, c) -> str:
    delta = b ** 2 - 4 * a * c # Równanie delty

    # Obsługa błędu - jeśli delta mniejsza niż 0 to zwrócona zostaje informacja, że równanie jest sprzeczne
    if delta < 0:
        return "Równanie sprzeczne"
    squareDelta = sqrt(delta) # Przypisanie pierwiastka delty do zmiennej

    # Rozwiązania równania
    x1 = (-b + squareDelta) / (2 * a)
    x2 = (-b - squareDelta) / (2 * a)
    return str(f"x1 = {x1}\nx2 = {x2}") # Zwraca wyniki

def main() -> None:

    # Pobranie wartości a, b i c
    a = input("Podaj a: ") #
    b = input("Podaj b: ") #
    c = input("Podaj c: ") #

    # Przekonwertowanie zmiennych na float
    a = float(a)
    b = float(b)
    c = float(c)

    # Wywołanie funkcji do obliczenia pierwiastka kwadratowego i zwrócenie wyniku
    print(squareRoot(a, b, c))

# Wywołanie funkcji main
if __name__ == "__main__":
    main()

