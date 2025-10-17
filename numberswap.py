a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

a, b, c = b, c, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)
print("c =", c)