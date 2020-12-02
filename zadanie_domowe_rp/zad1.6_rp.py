"""​
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i
ich wyświetlenie zrealizuj za pomocą konsoli.
​
"""

wiek = int(input("Podaj wiek: "))
ilosc = int(input("Podaj liczbę biletów: "))

if wiek < 7:
    print("Mosz za friko!")
elif 6 < wiek < 18:
    print(f'Za {ilosc} biletów zapłacisz {ilosc * 2.28:.2f}złociszczy')
elif 17 < wiek < 65:
    print(f'Za {ilosc} biletów zapłacisz {ilosc * 3.8:.2f}złociszczy')
else:
    print(f'Za {ilosc} biletów zapłacisz {ilosc * 1.9:.2f}złociszczy')