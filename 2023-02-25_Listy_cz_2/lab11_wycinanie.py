list_1 = [9]
list_2 = list_1[:]  # skopiuj całą listę, przez ten wycinek

# list_2 = [list_1] -- dziwne xD

list_2[0] = 13
print(list_2)
print(list_1)

