persons ={
    "name" : "Abdul",
    "age":27,
    "address": "dhaka"
}

print(persons)
print(type(persons))
print(len(persons))

# Accessing Items
print(persons["name"])
# There is also a method called get() that will give you the same result:
print(persons.get("age"))
# Get Keys
print(persons.keys())
# add item
persons["phone"] = 28012587
print(persons.keys())

# Get Values
print(persons.values())

# Get Items
print(persons.items())

# Check if Key Exists
if "phone" in persons:
    print("yes phone is here")
    
# Change Values
persons["address"] = "rangpur"
print(persons.items())

# Update Dictionary
persons.update({"name" :"BArik"})
print(persons.items())

# Removing Items
persons.pop('age')
print(persons)
# The popitem() method removes the last inserted item
persons.popitem()
print(persons)
# The del keyword removes the item with the specified key name:
del persons["name"]
print(persons)
# The clear() method empties the dictionary:
persons.clear()
print(persons)

# Loop Dictionaries
persons ={
    "name" : "Abdul",
    "age":27,
    "address": "dhaka"
}
 
for x in persons:
     print(x)
     
for y in persons:
    print(persons[y])
    
for z in persons.values():
    print(z)
    
for i in persons.keys():
    print(i)
#  Loop through both keys and values, by using the items() method:
for j, k in persons.items():
    print(j,k)   

# Copy a Dictionary
percopy = persons.copy()
print(percopy)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(myfamily["child1"])
print(myfamily["child2"]['name'])

# Loop Through Nested Dictionaries
for x , obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])