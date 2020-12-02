"""## Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)
​
Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
​
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków
i ile kilo chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
​
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy
i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie, za co
trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
​"""

cena_ziemniakow = float(input("Podaj ile kosztuje kg ziemniaków: "))
print(f'5kg ziemniaków kosztuje {cena_ziemniakow*5}zł')

waga_ziemniakow = float(input("podaj ile chcesz kupic ziemniakow: "))
print(f'{waga_ziemniakow:.2f}kg kosztuje {waga_ziemniakow*cena_ziemniakow}zł')

cena_bananow = float(input("Podaj ile kosztuje kg bananow: "))
waga_bananow = float(input("podaj ile chcesz kupic bananow: "))

print(f'Za wszystko zapłacisz:{cena_ziemniakow * waga_ziemniakow + cena_bananow * waga_bananow}zł')

if cena_bananow*waga_bananow > cena_ziemniakow*waga_ziemniakow:
    print("Za bananay zapłacisz więcej")
elif cena_bananow*waga_bananow < cena_ziemniakow*waga_ziemniakow:
    print("za ziemniaki zapłacisz więcej")
else:
    print("zapłacisz tyle samo za obydwa produkty")
