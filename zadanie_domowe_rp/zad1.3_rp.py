### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
"""​
Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników,
            proszę znaleźć samodzielnie).
​
"""

waga = float(input("Podaj mase ciała w kg: "))
wzrost = float(input("Poda wzrost w cm: "))
bmi = waga / (wzrost / 100)**2
if  18.5 <= bmi < 25:
    print(f'Twoje BMI wynosi {bmi:.2f}, jesteś idealny! ;)')
elif bmi <18.5:
    print(f'Twoje BMI wynosi {bmi:.2f}, masz niedowage ;(')
elif 25 <= bmi <30:
    print(f'Twoje BMI wynosi {bmi:.2f}, masz nadwage ;(')
else:
    print(f'Twoje BMI wynosi {bmi:.2f}, jesteś otyły ;((((((')
