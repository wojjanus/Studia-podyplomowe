'''
Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje:
dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo.
Wyświetl rezultat na ekranie.
'''
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b
modulo = a % b


print("Wynik dodawania to: " + str(suma) + "\n")
print("Wynik odejmowania to: " + str(roznica) + "\n",sep="",end="")
print("Wynik mnożenia to: " + str(iloczyn) + "\n")
print("Wynik modulo to: " + str(modulo) + "\n", sep="", end="")
print("Wynik dzielenia to: " + str(iloraz) + "\n")