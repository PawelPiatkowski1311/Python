#!/usr/bin/python3

def main() -> None:
    fullName = input("Proszę podać imię i nazwisko: ") # Pobranie imienia i nazwiska
    fullNameSplited = fullName.split() # Podzielenie podanego ciągu na imie i nazwisko do tablicy
    firstElement = fullNameSplited[0] # Przypisanie pierwszego elementu tablicy do zmiennej
    secondElement = fullNameSplited[1] # Przypisanie drugiego elementu tablicy do zmiennej
    print(secondElement + ' ' + firstElement) # Wydrukowanie imienia i nazwiska w odwrotnej kolejnosci, uwzględniając spacje

# Wywołanie funkcji main
if __name__ == "__main__":
    main()