salaries = [5, 10, 15, 20]

try:
    for amount in salaries:
        try:
            user_input = int(input("Provide a number: "))
            result = amount / user_input
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero value.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
        except TypeError:
            print("Invalid operation! Please check your inputs.")
except NameError:
    print("A variable was not properly defined.")
except IndexError:
    print("An error occurred with list indexing.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("All operations completed successfully.")
finally:
    print("Program execution completed.")
