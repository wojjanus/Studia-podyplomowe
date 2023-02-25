#random_three_out_of_ten

import random

numbers = [i for i in range(1,11)]
random_numbers = random.sample(numbers,3)
random_numbers.sort()

print(random_numbers)