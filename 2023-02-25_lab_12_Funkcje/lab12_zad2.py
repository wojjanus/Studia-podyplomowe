'''
Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
prostokątów o następujących długościach boków:
• 4 i 5,
• 2678 i 5678,
• 344555 i 788998.
'''


def obw(a, b):
    return 2 * a + 2 * b

def pole(a, b):
    return a * b

def dl_przekatnej(a, b):
    return (a ** 2 + b ** 2) ** (1 / 2)

def pokaz_wynik(a, b):
    print("Prostokąt o bokach", a,"i", b)
    print("Obwód:", obw(a, b))
    print("Pole prostokata: ", pole(a,b))
    print("Długość przekatnej:", dl_przekatnej(a,b))
    print()

pokaz_wynik(4,5)
pokaz_wynik(2678,5678)
pokaz_wynik(344555,7888998)