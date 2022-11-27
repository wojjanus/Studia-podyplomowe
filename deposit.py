'''
Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
• inwestowane środki 46 567,00 zł
• stałe oprocentowanie roczne 7.5%
• coroczna kapitalizacja odsetek
• w obliczeniach zastosuj złożony operator przypisania
'''

# K_n=K*(1+r)^{n}

# K_n=
# K=46576.00
# r=0.075
# n=3

# print("Zysk z 3-letniej lokaty to: K_n =", round(((K*(1+r)**n)-K),2))

K = 46576.00
K = K * 1.075
K *= 1.075

print(K-46576.00)
