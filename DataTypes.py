# Built-in Data Types

# Text Type:	str
x = "barik"
print(type(x))

# Numeric Types:	int, float, complex
x = 10
print(type(x))
x =  10.10
print(type(x))
x = 10j
print(type(x))

# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(10)
print(type(x))

# Mapping Type:	dict
x = {"name" : "Barik", "age" : 27}
print(type(x))

# Set Types:	set, frozenset
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# Boolean Type:	bool
x = 10
y = 15
print(type(x > y))

# Binary Types:	bytes, bytearray, memoryview
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))

# None Type:	NoneType
x = None
print(type(x))