'''
Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
• zapytaj użytkownika o wzrost i wagę,
• stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
• stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
otyłość) na podstawie wskaźnika BMI,
• zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.
'''

def kalkulator_bmi(waga_w_kg,wzrost_w_m):
    return waga_w_kg/wzrost_w_m **2

def wskaznik_bmi_kategoria(bmi):
    if bmi<18.5:
        return "niedowaga"
    elif bmi<25:
        return "waga prawidłowa"
    elif bmi< 30:
        return "nadwaga"
    else:
        return "otyłość"

print("Obliczanie wskaźnika BMI!")
waga_w_kg = float(input("Podaj swoją wagę (kg)"))
wzrost_w_cm = float(input("Podaj swój wzrost (cm)"))

bmi = kalkulator_bmi(waga_w_kg,wzrost_w_cm * 1/100)
kategoria = wskaznik_bmi_kategoria(bmi)

print("Pokaż wskaźnik ", bmi)
print("Kategoria:", kategoria)




