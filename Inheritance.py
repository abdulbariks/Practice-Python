# Create a Parent Clas
class Person:
    name = "barik"
    age = 28
    address = "dhaka"
    def myname(self):
      print("my name:", self.name)

x = Person()
x.myname()
# Create a Child Class
class Person1(Person):
    salary= 5000
    def   myfun(self):
        print(self.name, self.age, self.address, self.salary)
y = Person1()
y.myfun()

class Animal:
    aname ="dog"        
    
class Person2(Person1, Animal):
    def myfun(self):
        print(self.aname, self.age, self.address, self.salary)
        
z = Person2()
z.myfun()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
  def  myfun(self):
        print('my first name:', self.firstname, "my Last name:", self.lastname)
        

x = Student("Mike", "Olsen")
x.printname()
x.myfun()