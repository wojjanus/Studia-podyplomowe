numbers = [4, 5, 2, 1, 3, 7, 9, 11, 12, 13, 100, 99, 87, 101, -2]

# numbers = [4,5,2,1]
# numbers = [4,2,1,5]
# numbers = [2,1,4,5]
# numbers = [1,2,4,5]

# czy była zamiana
swapped = True

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)
