# Input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Make sure a is greater than b
if a < b:
    a, b = b, a

# Use Euclidean algorithm to find HCF
while b != 0:
    a, b = b, a % b

# Print the result
print("The HCF is:", a)
