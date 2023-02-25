'''
Napisz progran który rozszyfruje poniższą wiadomość
Xq|`gf(bm{|(nibfq)
dla każdego znaku zmienniono 4 bit na przeciwny
(bity liczymy od najmniej znaczącego i to nie jest indeks bitu tylko faktycznie bit)
4 bit->indeks 3
'''

# print(ord("c")) # znaki reprezentowane są przez wartości liczbowe
# print(bin(ord("c")))

# print("{:08b}".format(ord("c")))

# 01100011 - nasza liczba
# 00001000 - maska
# 01100011 - używamy XORa (alternatywa rozłączna) daje nam zamianę bitów na przeciwne gdy wskażemy za pomocą maski

# print("{:08b}".format(ord("c") ^ (1 << 3)))

# print(chr(ord("c")) ^ (1 << 3))

msg = "Xq|`gf(bm{|(nibfq)"
for c in msg:
    #print(ord(c) ^ (1 << 3), end=" ")

print(chr(ord(c) ^ (1 << 3), end=" ")

