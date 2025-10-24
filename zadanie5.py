#!/usr/bin/python3

# Przy pisanie wartości do zmiennej globalnej i stałej globalnej
a = "wartość zmiennej"
A = "wartość stałej"

def values() -> None:
    a = "inna wartość" # Przypisanie do zmiennej lokalnej innej wartości

    # Wydrukowanie wartości zmiennej lokalnej i stałej globalnej
    print(f"Wartość zmiennej a w nowej funkcji: {a}") # Funkcja wykorzysta zmienną lokalną
    print(f"Wartość stałej A w nowej funkcji: {A}\n")

def main() -> None:
    values() # Wywołanie funkcji

    # Przypisanie do zmiennych typów a i A
    variableAType = type(a)
    constantAType = type(A)
    print(f"Typ zmiennej a: {variableAType}\nTyp stałej A: {constantAType}") # Wydrukowanie wyników

# Wywołanie funkcji main
if __name__ == "__main__":
    main()