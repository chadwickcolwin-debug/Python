"""functions are reusable blocks of code"""

def greet(name):
    print("function greet() accepts parameter name")
    print("Hello", name)

def add(a, b):
    return a + b
    
def multiply(a, b):
    return a * b

def subt(a, b):
    return a - b
        
def div(a, b):
    return a / b

greet("Chad")

a = (int(input("what is the value of a? ")))

b = (int(input("what is the value of b? ")))

result_add =  add(a, b)
result_multiply =  multiply(a, b)
result_subt =  subt(a, b)
result_div =  div(a, b)

print("a+b = ", result_add)
print("a*b = ", result_multiply)
print("a-b = ", result_subt)
print("a/b = ", result_div)

"""this function has a default parameter value"""

def def_value(def_value="DEFAULT VALUE"):
    print("The " + def_value + " is " + def_value)

"""Keyword Arguments - You can specify parameter names when calling: """

print("the same functions called earlier with user inputs were called again with new parameters specified during the call")
result_add =  add(a=5, b=4)
result_multiply =  multiply(a=9, b=3)
result_subt =  subt(a=555, b=55)
result_div =  div(a=363, b=11)

print("a+b = ", result_add)
print("a*b = ", result_multiply)
print("a-b = ", result_subt)
print("a/b = ", result_div)

"""function to check if number a is divisible by number b"""

def is_divisible(a, b):
    return a % b

c = is_divisible(a, b)

if c == 0:    
    print("a is divisible by b")
else:    
    print("a is not divisible by b")