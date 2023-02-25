'''
i=0 # zmienna dotyczy całego skryptu ( w lini pierwszej wartość 0)
while i <10: # jeżeli i jest mniejsze od 10 to wykona się linia
    print(i, end=" ")
    i=i+1 #zwiększamy i o 1, aż osiągnie 9

'''

#for i in range(0,10): # od zera do 10-1, czy i <10
#    print(i, end=" ")

# funkcję range można użyć z jednym argumentem

#for i in range(0,10,5): # range(0,10,1) # ostatnia liczba oznacza, że przeskoczymy co 2
#    print(i

#początek to jest i=2, dopóki nasze i<10 i skaczemy co 3 (i=i+3)
#for i in range(2,10,3):# czy dwa jest miniejsze od 10 tkw wiec wykonaj, itd. 11 jest większe od 10 nie, wiec wyjdz z petli
#    print(i)

for i in range(9,-1,-1):# zmniejszamy o 1 za każdym razem
    print(i)

for i in range(-9,-10,-1):# zmniejszamy o 1 za każdym razem
    print(i)


#start i =9
#i>6
# skok o -1

#for i in range(9,6,-1):
#    print(i)

for i in range(float(6.3), 10, -1): # zwraca błąd

    print(i)