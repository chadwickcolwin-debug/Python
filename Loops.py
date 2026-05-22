"""Loops"""

"""For loop"""

i_for=int(input("how many times do you want to print 'i' using a For loop?"))
i_while=int(input("how many times do you want to print 'i' using a while loop?"))

print(f"Printing i {i_for} times using the For loop")
for i in range(i_for):
    print("i\n")

print("\n\n\n\n\n")
    
"""While loop"""
print(f"Printing i {i_while} times using the While loop")
count = 0
while count < i_while:
    print ("i\n")
    count += 1
    
    