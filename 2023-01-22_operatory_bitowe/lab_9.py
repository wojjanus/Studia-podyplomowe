
a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))

for i in range(a,b+1):
    if i%3==0 or i%5==0 or i%7==0:
        print("i=" + str(i))
else:
    print("Kończymy na dziś")