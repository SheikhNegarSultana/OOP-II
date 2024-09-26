# Input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary, octal, and hexadecimal
binary_number = bin(decimal_number)[2:]  # Remove the '0b' prefix
octal_number = oct(decimal_number)[2:]   # Remove the '0o' prefix
hexadecimal_number = hex(decimal_number)[2:].upper()  # Remove the '0x' prefix and convert to uppercase

# Print the results
print(f"Binary representation: {binary_number}")
print(f"Octal representation: {octal_number}")
print(f"Hexadecimal representation: {hexadecimal_number}")
