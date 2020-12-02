"""
Zadanie 1.7 | Liczenie cen (ok. 0,5 godz.)
​
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena.
Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
​
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
​
"""
nazwa = input("Co chcesz kupić?\n")
cena = float(input("Ile to kosztuje?\n"))
ilosc = float(input("Ile chcesz tego kupić?\n"))

print(f'Za {nazwa}, które chcesz kupić, zapłacisz {cena * ilosc:.2f}zł')