'''
Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.
'''


def power(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

print(power([1, 2, 3], 2))

def power2(numbers,k):
    result = []
    for i in numbers:
        result.append(i**k)
    return result
print(power2([1, 2, 3], 2))


def power3(liczba, potega):
    return [x**potega for x in liczba]
print(power3([1, 2, 3], 2))

