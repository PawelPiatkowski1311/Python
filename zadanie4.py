#!/usr/bin/python3

# Zaimportowanie stałej PI z biblioteki math
from math import pi

# Zdefiniowanie funkcji main, która nie zwraca wartości
def main() -> None:
    radius = input("Podaj promień koła: ") # Pobranie wartości i przypisanie jej do zmiennej radius
    radius = float(radius) # Przekonwertowanie zmiennej radius na typ float, gdyż funkcja input narzuca zmiennej typ string

    # Przypisanie do zminnych obliczonych wartości
    circuit = 2 * pi * radius
    area = pi * radius ** 2
    print(f"Results: \n Area: {area} \n Circuit: {circuit}") # Wydrukowanie wyników


# Wywołanie funkcji main
if __name__ == "__main__":
    main()