"""
### Zadanie 1.10 Położenie na planszy
​
Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100
wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...)
lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.
​
Przykładowy komunikat programu:
Podaj pozycję gracza X: 95
Podaj pozycję gracza Y: 95
Gracz znajduje się w prawym górnym rogu.
​
Plansza poglądowa: https://drive.google.com/file/d/1Ek18pnoqiGiDcZJT6RBT1yufPUMaMJ7N/view?usp=sharing
​
"""

x = int(input("Podaj współrzędną X:"))
y = int(input("Podaj współrzędną Y:"))
pozycja = None

if 0 <= x <=10:
    if 0 <= y <=10:
        print("gracz znajduje się w lewym dolnym rogu")
    elif 10 < y < 90:
        print("gracz znaduje się obok lewego boku")
    elif 90 <= y <= 100:
        print("gracz znajduje się w lewym górnym rogu")
    else:
        print("gracz znaduje się poza planszą")
elif 10 < x < 90:
    if 0 <= y <=10:
        print("gracz znajduje się obok lewego boku")
    elif 10 < y < 90:
        print("gracz znaduje się w środku planszy")
    elif 90 <= y <= 100:
        print("gracz znajduje się obok prawego boku")
    else:
        print("gracz znaduje się poza planszą")
elif 90 <= x <= 100:
    if 0 <= y <=10:
        print("gracz znajduje się w prawym dolnym rogu")
    elif 10 < y < 90:
        print("gracz znaduje się obok prawego boku")
    elif 90 <= y <= 100:
        print("gracz znajduje się w prawym górnym rogu")
    else:
        print("gracz znaduje się poza planszą")
else:
    print("gracz znaduje się poza planszą")
