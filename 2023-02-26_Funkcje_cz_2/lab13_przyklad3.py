'''
def scope_test():
    x=123 # zmienna lokalna
scope_test()
#print(x) # nie można się odwołać do zmiennej lokalnej, zmienna
#lokalna działa tylko w funkcji
print()
'''

'''
def scope_test():
    print("W środku funkcji: "+ str(x))

x=99 # zmienna globalna, jest widoczna w ciele funkcj
scope_test()
'''


'''
def scope_test(): # w ciele funkcji obowiązuje funkcja wewnętrzna,
    #przysłoniliśmy zmienną 99, zasięg lokalny
    x = 123
    print("W środku funkcji: " + str(x))


x = 99  # zmienna globalna, jest widoczna w ciele funkcj
#zasięg globalny
scope_test()
print("Na zewnątrz: " + str(x))
'''

def scope_test(): # w ciele funkcji obowiązuje funkcja wewnętrzna,
    #przysłoniliśmy zmienną 99, zasięg lokalny
    global x # to co się stało w środku funkcji zmienna globalna
    #została nadpisana
    x = 123
    print("W środku funkcji: " + str(x))

x = 99  # zmienna globalna, jest widoczna w ciele funkcj
#zasięg globalny
scope_test()
print("Na zewnątrz: " + str(x))