# a_1 = 1, a_2 =1, a_3 = a_1+a_2, a_4=a_2+a_3,

def fib(n):
    if n < 1:
        return None
    if n < 3:  # jeżeli jest mniejsze od 3
        return 1  # zwróć 1
    if n >= 3:
        a_1 = a_2 = 1
        sum = 0  # zmienna pomocnicza
        for i in range(3, n + 1):
            sum = a_1 + a_2
            a_1, a_2 = a_2, sum
        return sum
for n in range(1,101):
    print(n,"-->", fib(n))

print("Wyświetl element piąty: ", fib(5))
print("Wyświetl element ósmy: ", fib(8))

