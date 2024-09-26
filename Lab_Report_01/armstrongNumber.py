# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert number to string to iterate over each digit
    num_str = str(number)
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
