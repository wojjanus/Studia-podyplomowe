print(7 > 11)
a, b = 11, 9  # liczba a=11, liczba b=9

print(a > b)
print(2 == 2)
print(2 == 2.)
# print(2=2.0) wyrażenie nie może zawierać takiego operatora przypisania

number = 2 # zmiennej została przypisana wartość 2
if number > 3: #instrukcja warunkowa if, wyrażenie logiczne
    print("Liczba jest większa niż 3") # blok kodu który wykona się jeżeli warunek zostanie spełniony
    print("Hurra!")#blok kodu został pominięty ponieważ to jest błędne
print("Koniec")
'''
Wcięcia stosujemy konsekwentnie
za pomocą tabulatora (4 spacje)
za pomocą spacji (gdy zaczniemy miksować spacje i tabulatory to lipa)

liczba spacji musi być jednorodna w całym programie,
tabulator to najlepsza opcja stosowani wcięć
'''

number_1 = 0 # zmiennej została przypisana wartość 2
if number_1 > 0: #instrukcja warunkowa if, wyrażenie logiczne
    print("Liczba jest większa od zero")
else:
    print("Liczba mniejsza lub równa zero") #jeżeli to nie jest prawda to wyświetli się liczba mniejsza lub równa 0
print("Koniec")

number = 0
if number > 0:
    print("Liczba jest większa od zero")
elif number <0:
    print("Liczba mniejsza od zera")
else:
    print("Liczba równa 0")
print("Koniec")