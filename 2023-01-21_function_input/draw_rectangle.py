'''
Napisz skrypt rysujący na ekranie prostokąt
zbudowany ze znaku jak i wymiarów określonych
przez użytkownika, np..:
'''
symbol = input("Podaj symbol: ")
liczba_kolumn = int(input("Podaj liczbę kolumn: "))
liczba_wierszy = int(input("Podaj liczbę wierszy: "))

print((symbol * liczba_kolumn + "\n") * liczba_wierszy + "\n")
