# Create a Class
class myClass:
    number = 10
    
# Create Object
number1 = myClass()
print(number1.number)

# Object Methods
class Perion:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
        
    def myfunction(self):
        print("my name is :", self.name)
        print("my name is :", self.age)
person = Perion("abdul", 28)
person.myfunction()


