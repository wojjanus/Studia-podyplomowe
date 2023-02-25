'''
Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
• pobrać kolejne elementy i zapisać je do listy,
• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.
'''

imie = []
liczba_imion = int(input("Podaj liczbę imion "))
for i in range(1, liczba_imion + 1):
    imie.append(input("Podaj " + str(i) + "imię: "))

print("Pobrano zbiór imion", imie)
