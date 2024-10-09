# Set
mySet = {'barik', 27, 'abdul', 28, 'mahafuja', 22}
print(mySet)

# type
print(type(mySet))

# Length of a Set
print(len(mySet))

# Access Items
for item in mySet:
    print(item)
 
#  Check if anyvalue is present in the set:
print('barik' in mySet)   

# Add Items
mySet.add("maimuna")
print("add Item", mySet)


# To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# Remove Item
thisset.remove("banana")
print("Remove Item", thisset)

#  If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("apple")
print(thisset)

# The return value of the pop() method is the removed item.
print(thisset.pop())

# The clear() method empties the set:
print("clear method", thisset.clear())


# Loop Items
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(item)
    
    
# Join Sets
# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# You can use the | operator instead of the union() method, and you will get the same result.
set3 = set1 | set2
print(set3)

# Update
set1.update(set2)
print(set1)

# Intersection
print(set2)
set3 = set1.intersection(set2)
print(set3)
# You can use the & operator instead of the intersection() method, and you will get the same result.
set3 = set1 & set2
print(set3)

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
# You can use the - operator instead of the difference() method, and you will get the same result.
set3 = set1 - set2
print(set3)

# Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set3 = set1 ^ set2
print(set3)