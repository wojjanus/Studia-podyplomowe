'''
Napisz skrypt wyświetlający na ekranie dowolną liczbę dowolnych znaków. Liczbę oraz znak pownien określić użytkownik podczas uruchomienia programu.
'''
print()
znak = input("Podaj znak: ")
liczba_znakow = int(input("Podaj liczbę znakow: "))
print("Wyświetla liczbę podanych znaków: " + str(znak * liczba_znakow))
