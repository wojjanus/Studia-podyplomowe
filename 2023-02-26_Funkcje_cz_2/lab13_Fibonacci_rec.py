# a_1 = 1, a_2 =1, a_3 = a_1+a_2, a_4=a_2+a_3,

def fib(n):
    if n < 1:
        return None
    if n < 3:  # jeżeli jest mniejsze od 3
        return 1  # zwróć 1
    return fib(n-1) + fib(n-2)
for n in range(1,10):
    print(n,"-->", fib(n))

