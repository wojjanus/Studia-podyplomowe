# konkatenacja
print(2 + 2)
print('2+2')
print("2" + "2")

# print("2"+2) #nie możesz łączyć str z liczbą
print("2" + "3")

# print("Jak masz na imię?")
# name = input()
# print("Witaj " + name + "! Jak Ci minął dzień?")

number_1 = int("2")
print(number_1 * 5)

number_2 = "2"
print(number_2 * 5)  # błąd znaczeniowy trudny do wykrycia

temp = float("36.6")
print(temp)

'''
age = 24
print("Mam", age, "lata.")  # separator jest ustawiony domyślnie na spację
print("Mam " + str(age) + " lata")
'''

'''
string_number = input("Podaj liczbę całkowitą: ") # czyli to co się wyświetli do wpisania
multipierl = 9
result =multipierl * int(string_number)
print("Gdy liczbę " + string_number + " pomnożymy przez " + str(multipierl) + " to otrzymamy " + str(result) + ".")
'''

'''
a = float(input("Podaj długość przyprostokątnej: "))
b = float(input("Podaj długość przyprostokątnej "))
c = (a ** 2 + b ** 2) ** .5 
print("Długość przeciwprostokatnej wynosi " + str(c))
'''

print(" Ala " * 3)  # komukatywny (można używać przemiennie)
print(3 * " Ala ")

# print("Ala" * "Ala")  # wyrzuci błąd
# print("Ala" * -4)  # pusty string (nie zreplikuje się)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|" + "\n") * 5, end="")
print("+" + 10 * "-" + "+")

'''
Napisz skrypt rysujący na ekranie prostokąt
zbudowany ze znaku jak i wymiarów określonych
przez użytkownika, np..:

symbol = input("Podaj symbol: ")
liczba_kolumn = int(input("Podaj liczbę kolumn: "))
liczba_wierszy = int(input("Podaj liczbę wierszy: "))

print((symbol * liczba_kolumn + "\n") * liczba_kolumn)

'''

'''
Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje: 
dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo. 
Wyświetl rezultat na ekranie.

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b
modulo = a % b


print("Wynik dodawania to: " + str(suma) + "\n", "Wynik odejmowania to: " + str(roznica) + "\n",sep="",end="")
print("Wynik mnożenia to: " + str(iloczyn) + "\n", "Wynik modulo to: " + str(modulo) + "\n", sep="", end="")
print("Wynik dzielenia to: + str(iloraz) + "\n")
'''

'''
Za pomocą jednej instrukcji wyświetl na ekranie 
następującą figurę
'''

print( ("+" + "-") * 9 + "+" + "\n" + ("|" + " ") * 10 + "\n" + ("+" + "-") * 9 + "+")
