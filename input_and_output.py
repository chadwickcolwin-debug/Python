"""Testing inputs and outputs"""


"""This section asks for three inputs then displays them in one line"""
name = input("Tell me your name: ")
age = int(input("Your age? "))
city = input("Where do you live? ")

print(f"Hi, {name} from {city}! How does it feel to be {age} years old?\n\n")

"""This section asks for 2 numerical input, then performs the basic operations on them"""

num1 = float(input("Now, give me a decimal number: "))
num2 = float(input("and another one, s'il vous plait "))

print(f"sum num1+num2: {num1+num2}")
print(f"difference num1-num2: {num1-num2}")
print(f"product num1*num2: {num1*num2}")
print(f"quotient a/b: {num1/num2}")

print("\n\n\n")

"""This section asks for a to-do list and stores it in a list-type variable"""

task_count=int(input("How many to-do items do you have? "))

i = 0
task_item = ["item1"]
while i < task_count:
    entry=input("what is one to-do item?")
    task_item.append(entry)
    i += 1
    
"""Then prints the list"""
i = 0   
for i in range(task_count):
    print(f"Task {i+1} is {task_item[i+1]}")