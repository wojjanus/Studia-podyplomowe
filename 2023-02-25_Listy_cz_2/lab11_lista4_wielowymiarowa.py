numbers = [1, 2, 3]
#l2 = numbers
#l2 = [numbers, numbers] # zagnieżdżenie listy w liście (zawiera listę, która ma w sobie listę)
matrix = [numbers[:], numbers[:]]
matrix[0][0] = 99

print(matrix)
