'''
Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
ilość razy, w poziomie lub w pionie.
'''

#domyślnie będziemy drukować znaczki w poziomie
def dowolny_znak(znak="*", rep=10, vertical = False):
    for i in range(rep):
        if vertical:
            print(znak)
        else:
            print(znak + " ",end="")
    if not vertical:
        print()
    print()
    #pass

dowolny_znak()
dowolny_znak("+", 5, True)
dowolny_znak("^", 7, False)

