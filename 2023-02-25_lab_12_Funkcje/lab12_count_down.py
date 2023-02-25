def count_down(whishes=True):
    print("Trzy....")
    print("Dwa....")
    print("Jeden....")

    if not whishes:
        return # ma wyjść
    print("Szczęśliwego Nowego Roku")


count_down(True)
count_down(whishes=True)
count_down(whishes=False)
