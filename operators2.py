"""Operators"""

"""Aritmetic operators"""

a = int(input("give me a number: "))
b = int(input("give me another number: "))

print("these are the values obtained when arithmetic operators are used on the two numbers.") 
print("Note: the first number will always come before the operator")
print(f"addition (+) {a + b}")   # addition
print(f"subtraction (-) {a - b}")   # subtraction
print(f"multiplication (*) {a * b}")   # multiplication
print(f"division (/) {a / b}")   # division (float)
print(f"floor division (//) {a // b}")  # floor division
print(f"modulus (%) {a % b}")   # modulus (remainder)
print(f"exponent (**) {a ** b}")  # exponent

"""Comparison Operators"""
print(a == b)   # equal
print(a != b)   # not equal
print(a > b)    # greater than
print(a < b)    # less than
print(a >= b)   # greater or equal
print(b <= a)   # less or equal


"""Logical operators"""

c = int(input("give me another number so I can do logical operations: "))

print("I will compare the value of the third number with the first two.")
print(c > 18 and c < 60)   # both must be true
print(c < 18 or c > 60)    # at least one true
print(not c > 18)            # negation

"""assignment operators - used to update the value of the same variable"""

x = a
print(f"the value of x is {x}")
x += 5   # x = x + 5
print(f"after x+= 5, the value of x is now {x}")
x -= 4   # x = x - 3
print(f"after x-= 3, the value of x is now {x}")
x *= 3   # x = x * 2
print(f"after x*= 3, the value of x is now {x}")
x /= 5   # x = x / 5
print(f"after x/= 5, the value of x is now {x}")


"""membership operators"""
print("membership operators")
tasks = ["login", "checkout", "logout"]

print("checking if login is in tasks ->","login" in tasks)       # True
print("checking if payment is not in tasks ->", "payment" not in tasks) # True
