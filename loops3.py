"""loops - triangle : make a pyramid of asterisks"""


r = 10

for i in range(1, r + 1):
    spaces = r - i
    stars = "* " * i
    print(" " * spaces + stars)

   
print("\n\n\n\n")
print("-------------")

r=10
i=1
while i <= r:
    spaces = r - i
    stars = "8 " * i
    print(" " * spaces + stars)
    i+=1    