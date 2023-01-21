'''
Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3.
'''

#for i in range(1, 101):
#    if i % 3!=0:
#        print(i)


'''Zadanie numer 3
number = int(input("Podaj rozmiar "))
char = input("Podaj znak: ")

for i in range(number):
    for j in range(number):
        print(char, end=" ")
    print()
'''
#szachownica ma 64 pola
# 0 1 2 3 4
# 1 2 4 8 16 ... 2**i
sum = 0
for i in range(64):
    sum += 2**i
    print("Suma wszystkich ziaren zboża na szchownicy " + str(sum))

#1 ziarno to 0.4 mg
#1 ziarno to 0,0004 g
#1 ziarno to 0,0000004 kg
#1 ziarno to 0,0000000004

tons = int(sum*0.0004/1000/1000)
print(tons)

#produkcja przenicy na świecie to około 782 mln ton
year = int(tons/782000000)
print(year)
# pociąg może przetransportować 2200 ton
 trains = int(tons /2200)+1
 print(trains)
