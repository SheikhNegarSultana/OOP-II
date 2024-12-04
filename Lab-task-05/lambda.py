def lambda_fun(a):
    return lambda b: b**2

num = int(input("Enter a number : "))

square_function = lambda_fun(num)

print(square_function(num))