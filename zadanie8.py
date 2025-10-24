#!/usr/bin/python3

import datetime as date

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

