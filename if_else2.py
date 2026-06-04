"""Ask user for a number"""

x = int(input("give me a number "))

"""evaluate if number is odd or even"""
if x%2==0:
    print("the numer is even")
else:
    print("the number is odd")
    
"""Grade checker"""
if x>= 90:
    print("if that number was a score, your grade would A")
elif x>=80 and x<=90:
    print("if that number was a score, your grade would B")
elif x>=70 and x<=79:
    print("if that number was a score, your grade would C")
elif x>=60 and x<=69:
    print("if that number was a score, your grade would D")
elif x<60:
    print("if that number was a score, your grade would F")
    
    
"""Login simulation"""

"""allowed usernames"""
username = ["chad","tess","ella"]

"""allowed passwords"""
password = ["apple","orange","banana"]


print("\n\n")
usn = input("username: ")
pwd = input("password: ")

if usn in username and pwd in password:
    print("login successful")
else:   
    print("login failed")