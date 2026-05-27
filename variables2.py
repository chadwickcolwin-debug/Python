"""trying data types"""

"""list"""

variable_list = ["apple","banana","carrot", "durian"]

print("list item 1: ", variable_list[0])
print("list item 2: ", variable_list[1])
print("list item 3: ", variable_list[2])

"""dictionary"""

user = {
    "name": "Chad",
    "role": "QA",
    "city": "Surrey"
    }
    
print(user["city"])

print("what is the variable type of user? ", type(user))

"""other variables"""

is_string = "Chad is my name"
is_int = 24
is_float = 44.44
is_boolean = True
is_nonetype = None

print("Variable is_string is of type ", type(is_string))
print("Variable is_int is of type ", type(is_int))
print("Variable is_float is of type ", type(is_float))
print("Variable is_boolean is of type ", type(is_boolean))
print("Variable variable_list is of type ", type(variable_list))
print("Variable user is of type ", type(user))

"""Converting variable type"""

"""String to integer"""
Z = input("give me a number ")
print("Z is type ", type (Z))

Z = int(Z)

print("Z is now type ", type (Z))

Z = str(Z)

print("Z is now type ", type (Z))

Z = float(Z)

print("Z is now type ", type (Z))

variable_list2 = ["ant","ant","beetle","crab","doh", "doh"]

print(f"Printing the contents of variable_list2")
for i in range(len(variable_list2)):
    print(variable_list2[i])
    
print("converting variable_list2 to a set then printing its contents")
variable_list3 = set(variable_list2)
for value in variable_list3:
    print(value)