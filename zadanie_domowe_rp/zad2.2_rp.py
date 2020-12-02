"""
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę"
ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
​
```
    *
  * * *
* * * * *
"""

a = int(input("Podaj liczbę Naturalną: "))
i = 0

while i < a:
    print('  '*(a-i-1), '* '*(1+i*2))
    i += 1
