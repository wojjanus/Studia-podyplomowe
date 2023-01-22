print("Podaj długości trzech odcinków (liczby całkowite)")

a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))

if (a + b > c and b + c > a and c + a > b):
    print("Z tych odcinków można zbudować trójkąt", end=" ")

    # Sprawdzamy długości boków trójkąta
    if a == b and b == c and c == b:
        print("równoboczny", end=" ")
    elif a == b or a == c or b == c:
        print("równoramienny", end=" ")
    else:
        print("różnoboczny", end=" ")


    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        print("prostokątny", end=" ")
    elif (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (a ** 2 + c ** 2 < b ** 2):
        print("rozwartokątny")
    else:
        print("ostrokątny")

else:
    print("Z tych odcinków nie powstanie trójkąt")
