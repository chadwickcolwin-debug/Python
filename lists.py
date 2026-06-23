"""LIST"""

"""Creating a list of 5 cities"""

city = ["Atlanta","Kansas","Metropolis","Gotham","Star City"]

print(f"City #1: {city[0]}")
print(f"City #5: {city[4]}")
print(f"city list length is {len(city)} items")

print("Original order")
for name in city:
    print(name)
print("\n")    

city.sort()
print("Sorted order")
for name in city:
    print(name)
print("\n")    
    
city.reverse()
print("Reverse sorted order")
for name in city:
    print(name)
print("\n")

"""Adding two more cities"""

"""by append() -- adds to the end of the list"""
city.append("Emerald")

print("City list with appended item is now:")
for name in city:
    print(name)
print(f"city list length is {len(city)} items")
print("\n")

"""by insert() -- adds to the end of the list"""
city.insert(3,"Cartouche")

print("City list with item inserted in position 3 is now:")
for name in city:
    print(name)
print(f"city list length is {len(city)} items")
print("\n")

"""Replacing item number 4"""
city[3] = "Wildfell"

print("City list is now:")
for index, name in enumerate(city):
    print(index,name)
    
    
    
"""Creating a list of dictionaries of city names and population"""

city_pop = [
    {"name":"Atlanta", "pop":"263785"},
    {"name":"Kansas", "pop":"97632"},
    {"name":"Metropolis", "pop":"3456753"},
    {"name":"Gotham", "pop":"34577"},
    {"name":"Star City", "pop":"4326"}
]

for city_name in city_pop:
    print(city_name["name"]+ " " +  city_name["pop"])