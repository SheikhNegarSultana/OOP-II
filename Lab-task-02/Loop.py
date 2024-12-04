# Range() function
for num in range(1, 11):
    print(num, end=" ")  
print()

for even in range(0, 20, 2):
    print(even, end=" ")  
print()

limit = 10
for count in range(limit):
    print(count, end=" ")  
print()


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")  
print()


user_input = input("Enter a string: ")
for char in user_input:
    print(char, end=" ")  # Prints each character of the string
print()


for fruit in fruits:
    print(fruit, end=" ")
    if fruit == "banana":
        break  
print()


for fruit in fruits:
    if fruit == "banana":
        continue 
    print(fruit, end=" ")
print()


for num in range(6):
    print(num, end=" ")
else:
    print("\nLoop completed successfully!")

for num in range(6):
    if num == 3:
        break  
    print(num, end=" ")
else:
    print("\nThis will not execute because the loop was interrupted.")
print()


attributes = ["red", "big", "tasty"]
for attribute in attributes:
    for fruit in fruits:
        print(f"{attribute} {fruit}", end="    ")
    print()

# Placeholder loop using pass
for _ in [0, 1, 2]:
    pass  # Prevents an error in an empty loop

# Demonstrating while loops
i = 1
while i < 6:
    print(i, end=" ")
    i += 1
print()

i = 1
while i < 6:
    print(i, end=" ")
    if i == 3:
        break  
    i += 1
print()

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skips the current iteration when i is 3
    print(i, end=" ")
print()

i = 1
while i < 6:
    print(i, end=" ")
    i += 1
else:
    print("\nLoop finished as i is no longer less than 6.")
