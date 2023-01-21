'''
Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
pobranej od użytkownika jest także liczbą całkowitą
'''

a = int(input("Podaj liczbę całkowitą "))
sqrt = round(a ** (1 / 2),2)
if sqrt % 1 == 0:
    print("Jest liczbą całkowitą " + str(sqrt))
else:
    print("Jest liczbą niewymierną " + str(float((sqrt))))
print("Koniec programu")
