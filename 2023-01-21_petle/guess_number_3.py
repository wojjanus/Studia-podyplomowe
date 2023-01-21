import random # liczby pseudolosowe

counter =1 # licznik
number = random.randint(1,10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1-10): "))# rzutowanie na liczbę

while number != guess: # dopuki nasza liczba wciąz jest inna niz podał użytkownik wykonaj petle
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter = counter + 1

print("Brawo! Udało Ci się za " + str(counter) + " razem")