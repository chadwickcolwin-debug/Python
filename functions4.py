"""Functions Exercise 4 - Which number is the greatest or least in the list"""
"""
numbers = []
items = int(input("how many numbers do you want to compare?"))

for i in range(0, items+1):
    numbers[i] = int(input("give me a number "))

def greatest(a):
    for b in range(0,items+1):
        if numbers[b] >= numbers[b+1]:
            largest = numbers[b]
        
        

greatest(numbers)"""

numbers=[19, 17, 2]

def greatest():
    if numbers[0]>=numbers[1]:
        largest = numbers[0]
    elif numbers[1]>=numbers[2]:
        largest = numbers[1]
    elif numbers[1]>=numbers[2]:
        largest = numbers[2]
    return largest
    
print(greatest())

numbers = []
items = int(input("how many numbers do you want to compare?"))

for i in range(items):
    numbers.append(int(input("give me a number: ")))
    
for a in numbers:
    print(a)
    
numbers.sort()

print(f"The smallest number is: {numbers[0]}")
print(f"The largest number is: {numbers[items-1]}")