# wskazuje gdzie leży lista z elementem 9, odwołanie do miejsca gdzie mamy obiekt z tą wartości
list_1 = [9]
list_2 = list_1 #w tym miejscu te dwie nazwy wskazują na ten sam obszar pamięci (dwie nazwy jedna lista, lista zmieniona)

list_2[0] = 13 #zmodyfikowaliśmy jedną listę i te nazwy które wskazywały na tę listę dalej wskazują na listę ale zmienioną
print(list_2)
print(list_1)
