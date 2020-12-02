### Zadanie 2.6 Zliczanie znaków w napisie
"""
​
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
4
​
​
1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam czy:
      - mam zliczac
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam
"""

napis = "Ala ma <kota>, a kto ma kompilator"
if napis.count('<') != 1 or napis.count('>') != 1:
    exit("Niewłaściwa liczba nawiasów <>")

przelacznik = 0
i = 0
for litera in napis:
    if litera == '>':
        przelacznik = 0
    if przelacznik == 1:
        i += 1
    if litera == '<':
        przelacznik = 1
print(f'Pomiędzy nawiasami <> występują {i} znaki')
