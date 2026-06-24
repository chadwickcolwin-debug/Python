#Dictionaries

#Creating a dictionary

person = {"name":"Arthur Cross","age":35,"city":"Surrey","job":"ballpen pusher",}

#Adding a new key to the dictionary

person["country"] = "United Kingdom"

#Updating values
person["city"] = "Newstardom"

#Printing all keys and values
for x, y in person.items():
    print(x, y)
    
#creating a list of dictionaries
product = [
    {"product_name": "Fazz", "price":12.50},
    {"product_name": "Fezz", "price":13.50},
    {"product_name": "Fizz", "price":11.50},
    {"product_name": "Fozz", "price":17.50},
    {"product_name": "Fuzz", "price":5.50}
]

#printing the dictionary

for item in product:
    print(item["product_name"], item["price"])
    
for item in product:
    print(item)