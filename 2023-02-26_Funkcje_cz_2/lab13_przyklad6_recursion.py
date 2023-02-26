def recursion(number):
    if number == 20:
        return  # wyjdź z funkcji
    print(number)
    number += 1
    recursion(number)


'''
def recursion(10):
    if number == 20:
        return  # wyjdź z funkcji
    print(10)
    number += 1
    recursion(11)
'''

'''
def recursion(11):
    if number == 20:
        return  # wyjdź z funkcji
    print(11)
    number += 1
    recursion(12)
    .
    .
    .
  def recursion(19):
    if number == 20:
        return  # wyjdź z funkcji
    print(19)
    number += 1
    recursion(20)  
'''