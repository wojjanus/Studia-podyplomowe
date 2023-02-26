# Przykład 1
'''
def sum_numbers(numbers):
    sum = 0
    for element in numbers:
        sum +=element
    return sum
sum_numbers([1,2,3])
print(sum_numbers([1,2,3]))
'''

#Przykład 2
def sum_numbers(numbers):
    sum = 0
    for element in numbers:
        sum +=element
    return sum
numbers = [1,2,3]
result = sum_numbers(numbers)
print(result)

# Jeżeli podstawimy wartość wyskoczy type error
sum_numbers(99) # po liczbie nie iterujemy
