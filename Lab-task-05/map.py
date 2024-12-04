# Defining a function my_cal that takes a string x and returns its length
def my_cal(x):
    return len(x)
print("The Length Of The String :",list(map(my_cal , ("Sheikh","Negar","Sultana"))))


''' Defining a function make_cube that takes a single number x and returns its cube'''
def make_cube(x):
    return x**3

print("Cube :",list(map(make_cube,(1,3,4,5))))


# Defining a function make_cube that takes two numbers x and y and returns x to the power of y
def make_cube(x,y):
    return x**y

print("Cube :",list(map(make_cube,(2,3,4,5),(7,4,3,2))))