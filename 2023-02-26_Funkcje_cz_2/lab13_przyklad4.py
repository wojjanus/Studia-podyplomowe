# Funkcja której zadaniem będie zmiana wartości

'''
def change_value(n):
    print("Przed zmianą: ", n)
    n += 1
    print("Po zmianie: ", n)

val = 7
change_value(val)
print(val)
'''


'''
def change_value(n):  # n=val
    print("Przed zmianą: ", n)
    n = [0, 0] #pod n podstawiliśmy nowy obiekt za pomocą przypisania
    print("Po zmianie: ", n)  # n=[0,0]


val = [1, 2]
change_value(val)
print(val)

'''

def change_value(n):  # n=val
    print("Przed zmianą: ", n)
    n = "OK" #pod n podstawiliśmy nowy obiekt za pomocą przypisania
    print("Po zmianie: ", n)  # n=[0,0]


val = [1, 2]
change_value(val)
print(val)
