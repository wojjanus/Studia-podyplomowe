'''
Ile jest liczb w przedziale 1-300, które dzielą się przez 3 i 7 jednocześnie
'''

numbers = [i for i in range(1, 301) if (i % 3 == 0 and i % 7 == 0)]
print(numbers)
print(len(numbers))
