'''
#jeżeli temperatura będzie dodatnia i będzie słonecznie, to...
#pójdziemy na spacer, a jeżeli nie to zostaniemy w domu

temperature = 12
is_sun_shining = False

if temperature > 0 and is_sun_shining: # True and False  --> False
    print("Idziemy na spacer")
else:
    print("Zostaniemy w domu")
'''



#jeżeli temperatura będzie dodatnia albo będzie słonecznie, to...
#pójdziemy na spacer, a jeżeli nie to zostaniemy w domu

temperature = 12
is_sun_shining = False

if temperature > 0 or is_sun_shining: # True or False  --> True
    print("Idziemy na spacer")
else:
    print("Zostaniemy w domu")


#jeżeli temperatura będzie ujemna albo będzie pochmurno, to...
#zostaniemy w domu, a jeżeli nie to pójdziemy na spacer

temperature = 12
is_sun_shining = False
jest_pochmurno = True

'''
if temperature < 0 or not is_sun_shining: # True or False  --> True
    print("Zostaniemy w domu")
else:
    print("Pójdziemy na spacer")
'''


# and - koniunkcja - czytamy jak "i"
# or - alternatywa - czytamy jak "lub"
# not - negacja - czytamy jak nie

# wyświetl cyfrę, chyba że...
# liczba parzysta lub liczba większa od 6 to wyświetl *

'''
for i in range(10):
    if i % 2 ==0 or i>6:
        print("*")
    else:
        print(i, "Drukuj " + str(i))
'''
