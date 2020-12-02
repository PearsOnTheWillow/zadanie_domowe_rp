"""
### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
​
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
​
Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
​
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
​
```
import math
​
x = math.sqrt(10)
```
"""
import math
a = float(input("Podaj długość 1 boku: "))
b = float(input("Podaj długość 2 boku: "))
c = float(input("Podaj długość 3 boku: "))
p = (a + b + c)/2
if a >= b and a >= c:
    if a < b + c:
        print(f'Pole wynosi {math.sqrt(p*(p-a)*(p-b)*(p-c)):.2f}')
    else:
        print("Z tych boków nie da się stworzyć trójkąta")
elif b >= a and b >= c:
    if b < a + c:
        print(f'Pole wynosi {math.sqrt(p*(p-a)*(p-b)*(p-c)):.2f}')
    else:
        print("Z tych boków nie da się stworzyć trójkąta")
else:
    if c < b + a:
        print(f'Pole wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c)):.2f}')
    else:
        print("Z tych boków nie da się stworzyć trójkąta")