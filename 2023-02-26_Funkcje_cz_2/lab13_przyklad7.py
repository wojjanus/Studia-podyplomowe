# sposób przekazywania argumentów pozycyjnie
def my_func(*args):
    for el in args:
        print(el)
my_func(1,2,3,4,5,6,7,8)


# sposób przekazywania argumentów pozycyjnie
def my_func(**args):
    for el in args.items():
        print(el)
my_func(val1="raz", val2=999)
