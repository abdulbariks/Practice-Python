# Creating a Function
def myFunction():
    print("My Function")

# Calling a Function
myFunction()

# Arguments
def myFunction(name):
    print("my name is: ", name)
myFunction("abdul")
myFunction("barik")

def myFunction(fname, lname):
    print("My first name:", fname, "last name :", lname)
myFunction("abdul", "barik")

# Arbitrary Arguments, *args
def myfunction(*names):
    print("name is:", names[1])
myfunction("barik", "mahafuja", "abdul")

# Default Parameter Value
def myfunction(name = "abdul"):
    print("name is:", name)
myfunction("barik")
myfunction()
myfunction("barik")

# Passing a List as an Argument
def myFunction(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
myFunction(fruits)

# Return Values
def myfunction(x):
    return 2 * x
print(myfunction(2))
print(myfunction(6))


# Lambda
# A lambda function is a small anonymous function
# Syntax
# lambda arguments : expression
x = lambda number  : number + 5
print(x(4))

x = lambda number1, number2  : number1 * number2
print(x(4,5))

# Use Lambda Functions
def  myfunction(args):
    return lambda a : a + args
number = myfunction(5)
number1 = myfunction(10)
print(number(10))
print(number(15))
print(number1(20))
    