"""loops"""

print("looping with index+value")

tasks = ["login", "checkout", "logout"]

for index, task in enumerate(tasks):
    print(index, task)


print("\n")


print("looping through dictionary keys, values and both")
user = {"name": "Chadwick", "role": "QA"}

for key in user:
    print("key",key)


print("\n")

for value in user.values():
    print("value", value)

print("\n")

for key, value in user.items():
    print("key:", key)
    print("value:", value)
    
    
"""Exercises"""

print("print numbers 1-20 using a for loop")

for i in range(20):
    print(i+1)
    
print("print numbers 1-20 using a while loop")

i=1
while i <= 20:
    print(i)
    i +=1
    
print("\nPrinting even numbers from 1 to 50 using a for loop")
for i in range(51):
    if i%2 == 0:
        print(i)
    
print("\nPrinting even numbers from 1 to 50 using using a while loop")

i=1
while i <= 50:
    if i%2 == 0:
        print(i)
    i +=1 
    
"""Looping through a list"""

print("give me five cities and I will print the names using a for loop")

"""creating a an empty list """
cities = [] 
i = 0

while i < 5:
    cities.insert(i, input("Give me a city name: "))
    i += 1

print("Here they are again. The cities are: ")

for x in cities:
    print(x)

    
"""countdown"""
countdown=5
while countdown<=5 and countdown>0:
    print(countdown)
    countdown -= 1

print("Blast Off!")    
    
print("\n\n\n\****************")
