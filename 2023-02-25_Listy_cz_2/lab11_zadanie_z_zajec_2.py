#random_three_out_of_ten

import random

random_numbers = []
counter = 3
while counter > 0: # losuj do...
    number = random.randint(1,10)
    if number not in random_numbers:
        random_numbers.append(number)
        counter -=1 # counter = counter -1
random_numbers.sort()
print(random_numbers)

