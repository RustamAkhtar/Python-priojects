# Fibonacci Series up to n terms

# take input from the user
n = int(input("Enter the number of terms: "))

# first two terms
a, b = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term
        count += 1
