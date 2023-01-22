'''
Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
wyświetli poniższe informacje:
• zestaw wylosowanych wyników,
• wyrzucaną wartość za 8 razem,
• liczbę wyrzuconych szóstek,
• maksymalną liczbę wyrzuconych tych samych wartości pod rząd
'''

import random
liczba_losowan = 16

rzut = []
for i in range(liczba_losowan):
    rzut.append(random.randint(1,6))

print("Zbiór wyników", liczba_losowan, rzut)

