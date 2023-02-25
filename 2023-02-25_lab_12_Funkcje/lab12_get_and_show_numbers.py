'''
def show_message(number_no):
    print("Proszę podaj " + str(number_no) + " liczbę: ", end=" ")


print("Podaj liczbę: ")
a = int(input())
print("Podaj liczbę: ")
b = int(input())
print("Podaj liczbę: ")
c = int(input())

print("Pobrano liczby ", a, b, c)
'''

'''
show_message(1)
a = int(input())
show_message(2)
b = int(input())
show_message(3)
c = int(input())

print("Pobrano liczby ", a , b, c)
'''


########################################
'''
def get_number(number_no):
    print("Proszę podaj " + str(number_no) + " liczbę: ", end=" ")



print("Podaj liczbę: ")
a = int(input())
print("Podaj liczbę: ")
b = int(input())
print("Podaj liczbę: ")
c = int(input())

print("Pobrano liczby ", a , b, c)
'''

###################################################################
'''
def get_number(number_no):
    print("Proszę podaj " + str(number_no) + " liczbę: ", end=" ")
    return int(input())

a = get_number(1)
b = get_number(2)
c = get_number(3)

print("Pobrano liczby ", a, b, c)
'''
###################################################################
def get_number(number_no):
    print("Proszę podaj " + str(number_no) + " liczbę: ", end=" ")
    return int(input())

print("Pobrano liczby ", get_number(1), get_number(2), get_number(2))