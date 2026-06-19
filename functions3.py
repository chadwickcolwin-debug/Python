"""Functions Exercise 2 - simple calculator function"""

def adder(x, y):
    return x+y
    
def subtracter(x, y):
    return x-y
    
def multiplier(x, y):
    return x*y
    
def divider(x, y):
    return x/y    
    
a = int(input("give me the first number: "))
b = int(input("give me the second number: "))

print("\n")
print(f"the sum of the two numbers is {adder(a,b)}")
print(f"the difference of the two numbers is {subtracter(a,b)}")
print(f"the product of the two numbers is {multiplier(a,b)}")
print(f"the quotient of the two numbers is {divider(a,b)}")

"""Check if the given numbers and the results are even"""
def is_even(z):
    remainder = z%2 
    if remainder==0:
        return True
    else:
        return False
        
print(f"the first number is even: {is_even(a)}")
print(f"the second number is even: {is_even(b)}")
print(f"the sum is even: {is_even(adder(a,b))}")
print(f"the difference is even: {is_even(subtracter(a,b))}")
print(f"the product is even: {is_even(multiplier(a,b))}")
print(f"the quotient is even: {is_even(divider(a,b))}")