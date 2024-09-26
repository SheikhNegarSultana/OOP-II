# Input range from the user
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Loop through the interval
for num in range(start, end + 1):
    if num > 1:  # Prime numbers must be greater than 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
