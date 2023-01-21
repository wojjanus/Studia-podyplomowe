'''
Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
otrzymanych punków z kolokwium:
• ocena bardzo (5,0) dobra, jeżeli student otrzymał 95 lub więcej punktów,
• jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra
(4,5),
• ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
• jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra
(3,5),
• ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale
powyżej 50 punktów,
• wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej
(2.0)
'''

pkt = int(input("Podaj liczbę punktów od 0 do 100 "))
print("Twoja ocena jest", end=" ")
if pkt >= 95:
    print("bardzo dobra (5.0)")
elif pkt < 95 and pkt > 84:
    print("ponad dobra (4.5)")
elif pkt >= 70 and pkt <= 80:
    print("dobra (4.0)")
elif pkt > 60 and pkt < 70:
    print("dość dobra (3.5)")
elif pkt <= 60 and pkt > 50:
    print("dostateczna (3.0)")
else:
    print("niedostateczna (2.0)")
print("Koniec programu")
