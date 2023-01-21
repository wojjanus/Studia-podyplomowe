'''
Napisz program określający dziesiętną wartość liczby, która w systemie ósemkowym wynosi 777.
'''

print("Wartość dziesiętna to: " + str(0o777),sep="\n") # 7* 8**2 + 2*8**1 + 7*8**0 = 511
print("") # alternatywnie
print("Wartość dziesiętna to: " + str(7* (8**2) + 7*(8**1) + 7*(8**0)))