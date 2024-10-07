x = 10   # x is of type int
print(x)
print(type(x))

y = "barik" # y is  of type str
print(y)
print(type(y))

z = 15.50  # z is  of type float
print(z)
print(type(z))


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x, y, z)
print(x + " " + y +" "+ z)


# Global Variables
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
print(x)
myfunc()

print("Python is " + x)
