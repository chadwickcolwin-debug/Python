"""FUNCTIONS"""
"""
Sample 

def login(driver, username, password):
    driver.find_element(...).send_keys(username)
    driver.find_element(...).send_keys(password)
    driver.find_element(...).click()

where 
 - login is the function name
 - (driver, username, password) are the parameters accepted by the function. If no parameters are defined, it is only ()
 - the indented section immediately after def is the block of code in the function

when calling a function, values must be provided for all defined parameters unless default values were supplied in the def

"""
"""this function prints names"""
def the_deets(name="chad", age="23"):
    print(name + " & " + age)
    
print(f"calling the function but not supplying a parameter value prints the default parameter value which are: ")
the_deets()
print ("\n")

print(f"calling the function and supplying a parameter value prints the supplied parameter value which are: ")
the_deets("Tess", "25")
print ("\n")

print("reprinting")
the_deets()
the_deets("Tess", "25")

"""ask the user for name and age"""
usn=input("what is your name? ")
usa=input("how old are you? ")

the_deets(usn, usa)
