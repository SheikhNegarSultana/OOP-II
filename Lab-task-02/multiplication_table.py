def multiplication_table(number):
    for i in range(1, 11):
        if i == 4:
            continue  # Skip when i is 4
        print(f"{number} x {i} = {number * i}")
        if i == 8:
            break  # Stop when i is 8

# Get user input and display the multiplication table
num = int(input("Enter a number: "))
multiplication_table(num)
