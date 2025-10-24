#!/usr/bin/python3

# ===== Importy =====
# W tym miejscu importujemy biblioteki standardowe lub zewnętrzne, np.:
# import typing

#Zdefiniowanie stałej zawierającej ciąg znaków "Hello world"
WELCOME: str = "Hello World!"
variable: int = 1

# Zdefiniowanie funkcji main, która nie zwraca wartości
def main() -> None:
    print(WELCOME) # Wydrukowanie napisu powitalnego w konsoli

# Wywołanie funkcji main
if __name__ == "__main__":
    main()