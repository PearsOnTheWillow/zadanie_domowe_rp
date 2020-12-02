"""
​
Napisz program zamieniający miejscami w zadanej liście liczb element
największy z najmniejszym.
na wejsciu: [49, 50, 20, 40, 35, 10]
na wyjsciu: [49, 10, 20, 40, 35, 50]
​
Jak to zrobimy?
1. Musimy znaleźć indeks elementu o największej wartosci
i indeks elementu o najmniejszej wartości
2. Zamiana miejscami elementów z tych indeksów
​
Wersja A
1. używamy pętli for do znalezienia indeksów
2. Zamieniamy wartości pod tymi indeksami
​
Wersja B
1. Używając funkcji min(), max() znajduje najmniejszą i najwieksza wartosc
2. Znajduję indeks tych elementów w liscie
3. Zamieniam te elementy miejscami
​
"""

lista = [49, 50, 20, 40, 35, 10]
print(lista)
min = min(lista)
max = max(lista)
i_min = lista.index(min)
i_max = lista.index(max)
lista[i_min] = max
lista[i_max] = min
print(lista)


#################### Wersja z pętlą for
print('-'*30)
i = 0
for index, wartosc in enumerate(lista):
    if i == 0:
        max_w = wartosc
        min_w = wartosc
        i_max_w = index
        i_min_w = index
        i = 7
    if wartosc > max_w:
        max_w = wartosc
        i_max_w = index
    if wartosc < min_w:
        min_w = wartosc
        i_min_w = index
lista[i_max_w] = min_w
lista[i_min_w] = max_w
print(lista)