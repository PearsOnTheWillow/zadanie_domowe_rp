"""### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
​
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1,
wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
​
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz
założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
​
"""
while True:
    dzien_1 = int(input("podaj dzien w ktorym oddales buty (od 1 do 7): "))
    if 0 < dzien_1 < 8:
        break
    print("liczba od 1 do 7!!")
dlugos_naprawy = int(input("podaj ile dni bedzie trwac naprawa: "))

print(f'buty dostaniesz {(dzien_1 + dlugos_naprawy) % 7} dnia tygodnia')
