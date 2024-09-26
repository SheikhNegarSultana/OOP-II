# Function to print Fibonacci sequence up to n terms
def print_fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # for newline

# Input from the user
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
print_fibonacci(num_terms)
