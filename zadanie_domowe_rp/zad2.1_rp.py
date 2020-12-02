### Zadanie 2.1 | Zagadka matematyczna
"""​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma
(nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo,
aż użytkownik poda prawidłowy wynik.
​
"""

from random import randint

x = randint(0, 100)
y = randint(0, 100)


while True:
    suma = int(input(f'Podaj Sumę {x} i {y}: '))
    if suma == x + y:
        break
    else:
        print("źle spróbuj jeszcze raz")
