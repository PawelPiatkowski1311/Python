#!/usr/bin/python3

# Zaimportowanie biblioteki datetime oraz dodanie aliasu date
from datetime import datetime as date # from datetime umożliwia wykorzystywanie funkcji z biblioteki datetime bez konieczności zapisywania "datetime"


# Zdefiniowanie funkcji main, która nie zwraca wartości
def main() -> None:
    now = date.now() # Przypisanie do zmiennej now daty korzystając z aliasu date. Metoda now zwraca pełny format

    # Metoda strftime konwertuje date zapisaną w zmiennej now i przypisuje do zmiennych first, second i third. Na końcu data jest drukowana w zadanym formacie
    first = now.strftime("%d-%m-%Y %H:%M")
    print(first)
    second = now.strftime("%d-%m-%Y %H:%M:%S")
    print(second)
    third = now.strftime("%Y-%m-%d %H:%M")
    print(third)

# Wywołanie funkcji main
if __name__ == "__main__":
    main()