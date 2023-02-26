#Funkcja do generowania listy z losowymi liczbami z zakresu od 1 do 99
import random

def generate_numbers(total_numbers):
    numbers =[]
    for i in range(total_numbers):
        numbers.append(random.randint(1,99))
    return numbers #zwraca listę numbers
print(generate_numbers((10))) # wylosuj 10 iczb i pokaż na ekranie
print(generate_numbers(100))
print(generate_numbers(23423))

def power(n)
    n=[]
