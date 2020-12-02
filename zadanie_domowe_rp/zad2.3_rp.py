"""
### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
​
NIE używaj funkcji wbudowanych!
​
"""

i = 0
suma = 0
max = None
min = None
srednia = None

while True:
    liczba = input("Podaj liczbę lub wpisz koniec aby zakończyć: ")
    if liczba == "koniec":
        break
    liczba = int(liczba)

    if max == None:
        max = liczba
        min = liczba
    if max < liczba:
        max = liczba
    if min > liczba:
        min = liczba

    suma += liczba
    i += 1
if i>0:
    print(f"""Max: {max}
    Min: {min}
    Suma: {suma}
    Ilość liczb: {i}
    Średnia: {suma/i}
    """)
else:
    print("Nie podales żadnej liczby więc nie moge podać wyniku")