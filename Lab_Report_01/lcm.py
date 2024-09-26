import math

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)

# Calculate LCM using the formula
lcm = abs(num1 * num2) // gcd

# Print the result
print(f"The LCM of {num1} and {num2} is: {lcm}")
