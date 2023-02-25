#name = input()
name = input("Jak masz na imię?")
print(("Witaj" + name + "!") * 100, end="")
print()

def introduce(first_name, last_name):
    print("Cześć jestem", first_name, last_name)

introduce("Jan", "Kowalski")
introduce( "Kowalski", "Jan")
#jawnie wskazaliśmy
introduce(first_name= "Jan", last_name="Kowalski")
#błędny kod introduce(first_name= "Jan", "Jan")
print("raz", "dwa", "trzy", sep=" - ")


def introduce(first_name= "Jan", last_name="Kowalski"):
    print("Cześć jestem", first_name, last_name)
introduce("Marcin", "Kowalski")
introduce(last_name="Nowak")

def introduce(first_name= "Jan", last_name="Kowalski"):
    print("Cześć jestem", first_name, last_name)
    return None # mogę tutaj zwrócić dowolną wartość np. 12
print(introduce())

#########################################################

def my_fun():
    #TODO
    pass
if my_fun() == None:
    print("Funkcja na razie nic nie zwraca")


    def my_fun():
        # TODO
        return 123
    if my_fun() == None:
        print("Funkcja na razie nic nie zwraca")