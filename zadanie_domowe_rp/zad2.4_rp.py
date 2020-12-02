### Zadanie 2.4 | Zgadnij liczbę z zakresu
"""
​
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża,
czy za mała. Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując,
w której próbie udało się zgadnąć liczbę.
​
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w
informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach
(bo 2^10=1024).
​
"""
from random import randint

x = randint(0,1000)

i = 1
while True:
    y = int(input("Odgadnij liczbe z przedziału 0-999: "))
    if y == x:
        break
    elif y > x:
        print("Mniej próbuj dalej")
    else:
        print("Więcej próbuj dalej")
    i += 1
print(f'Brawo udało Ci się za {i} razem')
