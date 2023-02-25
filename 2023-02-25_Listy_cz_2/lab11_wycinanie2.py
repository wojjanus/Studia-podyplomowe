numbers = [10, 8, 6, 4, 2]
#new_numbers = numbers[1:3] # pamiętamy, że lista new_numbers to odzielne miejsce i nie wpływa na listę numbers
#new_numbers = numbers[-4:-2]
#new_numbers = numbers[-4:3]
#new_numbers = numbers[4:3] # pusta lista
#new_numbers = numbers[:] # cała lista
print(len(numbers))
new_numbers = numbers[0:len(numbers)] # cała lista
print(new_numbers)
print(numbers)