import random

numbers = [] # pusta lista

for i in range(10):
    number = random.randint(1,100)
    numbers.append(number)
print(numbers)

print()

fruits = ["banan", "jabłko", "czereśnia"]
for i in range(len(fruits)):
    print(i, fruits[i])

print()

for f in fruits:
    print(f)
