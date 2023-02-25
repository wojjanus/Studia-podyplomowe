counter=0
for i in range(1,101):
    if i>90 and i%2 ==0:
        counter+=1
        print(i)
    elif not i%2==0 and i%9==0:
        print(i)
        counter+=1
else:
    print(counter)
    print("Koniec dowodu")