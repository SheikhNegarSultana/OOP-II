#Writing First Program
print("Practicing Python")

#Python Comment + Using String
name = "Negar Sultana"
print(name)

# An integer assignment
age = 45
print(age)

# A floating point
salary = 1456.8
print(salary)

# complex
x = 3j 
print(x) 

# bool
y = True  
print(y)

#Input and Output
val = input("Enter your value: ") 
print(val)

#Arithmetic Operators
print(10 + 5) # Addition
print(10 - 5) # Subtraction
print(10 * 5) # Multiplication
print(10 / 5) # Division
print(10 % 5) # Modulus
print(10 ** 5) # Exponentiation

#Logical Operators
a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 

# Python If Else
num = 10
if (num < 15): 
    print("num is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("num is greater than 15") 
    print("i'm in else Block") 
    
# Python if-elif-else ladder
p = 18
if (p == 10): 
    print("p is 10") 
elif (p == 15): 
    print("p is 15") 
elif (p == 20): 
    print("p is 20") 
else: 
    print("p is not present") 
    
#Python For Loop  
for m in range(0, 10, 2): 
    print(m)   
    
#Python While Loop
count = 0
while (count < 3): 
    count = count + 1
    print("Negar Sultana")
 
#Python function 
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

#Calling the function
evenOdd(2)
evenOdd(7) 