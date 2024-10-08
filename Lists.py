namelist  = ['barik', 'abdul', 'mahafuja']
print(namelist)

# List Length
print(len(namelist))

 # List type
namelist  = ['barik', 'abdul', 'mahafuja', "cherry", "orange", "kiwi", "melon", "mango"]
print(type(namelist))
numberlist = [1,2,5,8]
print(type(numberlist))

# Access Items
print(namelist[1])
print(namelist[2:5])
print(namelist[:4])
print(namelist[2:])

# Change Item Value
namelist[2] = "tiger"
print(namelist)

# Insert Items
namelist.insert(2, 'maimuna')
print(namelist)

# Append Items
namelist.append('karim')
print(namelist)

# Remove Specified Item
namelist.remove("abdul")
print(namelist)

# Remove Specified Index
namelist.pop(5)
print(namelist)

# Clear the List
# namelist.clear()
# print(namelist)


# Loop Lists
for x in namelist:
    print(x)


# Loop Through the Index Numbers
for i in range(len(namelist)):
    print(namelist[i])

# List Comprehension
newNamelist = [x for x in namelist if "a" in x]
print(newNamelist)


# Sort Lists
namelist.sort()
print(namelist)


# Copy Lists
copynamelist = namelist.copy()
print(copynamelist)

# Join Lists
namelist.extend(copynamelist)
print(namelist)