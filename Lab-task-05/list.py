# Creating a list of fruits
fruits = ["apple","banana","cherry","kiwi","mango"]

# Empty list to store fruits that contain the letter "a"
new_list=[]
for x in fruits :
    if "a" in x:
        new_list.append(x)


print(new_list)

# Creating a list of numbers
a=[1,3,6,8,2]
# Empty list to store even numbers
b=[]

for i in a :
    if i%2==0 :
        b.append(i)

print(b)