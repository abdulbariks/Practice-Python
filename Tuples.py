# Tuples

myTuple = ("barik", 5, 10, 'abdul')
print(myTuple)

# Tuple Type
print(type(myTuple))

# Tuple Length
print(len(myTuple))

# Access Tuple Items
print(myTuple[0])

# Check if Item Exists
if 'barik' in myTuple:
    print("yes")

# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x =('abdul', 'Barik')
y = list(x)
y[1]= 'mahafuja'
x = tuple(y)
print(x)

# Add Items
x =('abdul', 'Barik')
y = list(x)
y.append('maimuna')
print(tuple(y))

# Remove Items
x =('abdul', 'Barik')
y = list(x)
y.remove('Barik')
print(tuple(y))

# Unpacking a Tuple
x =('Abdul', 'Barik')
(abdul, barik) = x
print(abdul)
print(barik)

# Using Asterisk*
x =('Abdul', 'Barik', 'mahafuja', 'maimuna')
(abdul, *name)=x
print(name)

# Loop Through a Tuple
for i in x:
    print(i)

# Use the range() and len() functions to create a suitable iterable.
for j in range(len(x)):
    print(x[j])

# Using a While Loop
k =0
while k < len(x):
    print("while loop using:", x[k])
    k=k+1

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)