a = 5
b = 3

# koniunkcja bitowa
print(a, "^", b, "=", a ^ b)

print(bin(a))
print(bin(b))

print("{:08b}".format(a))  # na ośmiu bitach
print("{:08b}".format(b))  # na ośmiu bitach
print("-" * 8)
print("{:08b}".format(a ^ b))  # na ośmiu bitach