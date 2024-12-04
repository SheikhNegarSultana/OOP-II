# Create a dictionary to store information about an employee
emp = {
    "name" : "Negar",
    "age" : 21 ,
    "type1" : {
        "developer" : ["ios","android"]  # List of developer types
    } ,
    "permanent" : True ,
    "salary" : 40000 ,
    100 : (1,2,3) ,  # Tuple
    4.8 : {5,6,True,7,1} ,  # Set
    True : 1  # Boolean key
}

# Printing the type of the emp dictionary
print("type :",type(emp))  

# Printing the number of key-value pairs in the dictionary
print("Length :",len(emp))  

# Printing the dictionary for employee type
print(emp["type1"])  

# Printing the employee age
print(emp["age"])  

# Printing the set with unknown purpose
print(emp[4.8])  

# Printing the list of developer types
print(emp["type1"]["developer"])  

# Printing the second element of the developer types list
print(emp["type1"]["developer"][1])

emp["permanent"]=False  # Updating the value of 'permanent' key

# Printing the updated dictionary
print(emp)

emp["gender"] = "Female"  # Adding a new key-value pair

# Printing the updated dictionary
print(emp)

emp.pop("age")  # Removing the 'age' key-value pair

# Printing the updated dictionary
print("After removing age: ", emp)

for x in emp.keys():  # Iterating over the keys
    print(x)  # Printing each key

for x,y in emp.items():  # Iterating over the key-value pairs
    print(x,y)  # Printing each key-value pair

for x in emp.values():  # Iterating over the values
    print(x)  # Printing each value


# Creating a nested dictionary to store Bangladeshi food items along with price
menu = {
    "item1": {
        "name": "Biriyani",
        "price": 150
    },
    "item2": {
        "name": "Hilsa Curry",
        "price": 300
    },
    "item3": {
        "name": "Panta Bhat",
        "price": 50
    }
}

# Updating the name and adding a rating for each food item
menu["item1"]["name"] = "Kacchi Biriyani"  
menu["item1"]["rating"] = 4.9  
menu["item2"]["name"] = "Smoked Hilsa Curry" 
menu["item2"]["rating"] = 4.8  
menu["item3"]["name"] = "Panta Bhat with Ilish Fry" 
menu["item3"]["rating"] = 4.7  

# Printing the updated nested dictionary
print(menu)
