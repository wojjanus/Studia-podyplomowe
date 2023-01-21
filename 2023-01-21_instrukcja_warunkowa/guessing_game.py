'''
Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
o parzystości zgadywanej liczby itp.
'''

import random

number = random.randint(1, 10)  # specjalny rodzaj funkcji
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10): "
guess = int(input(msg))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejną szansę,...."
    if number % 2 == 0
        msg = msg + "parzysta"
    else:
        msg = msg + "nieparzysta"
        guess = int(input(msg))
        if guess == number
            print("Brawo udało się odgadnąć za drugim razem")
        else:
            msg = "Masz kolejną szansę,...."
            if number >5
                msg = msg + "większa"
            else:
                msg = msg + "mniejsza lub równa"
            msg = msg + "od liczby 5"
                guess = int(input(msg))
