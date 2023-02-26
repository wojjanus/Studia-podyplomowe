def change_value(n):  # n=val
    print("Przed zmianą: ", n) # drukujemy [1,2]
    n[0] = 999 # zmień (indeks 0) jeden element w tej liście na 999, czyli [999,2]
    print("Po zmianie: ", n)  # n=[0,0]

val = [1, 2]
change_value(val)
print(val)
