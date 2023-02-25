# przesunięcie bitowe w lewo
print(a, "<<", 2, "=", a << 2)

print(bin(a))
print(bin(b))

print("{:08b}".format(a<<2))  # na ośmiu bitach
print("-" * 8)
print("{:08b}".format(a << 2))  # na ośmiu bitach