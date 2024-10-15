# Class Polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(self.brand, self.model)

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(self.brand, self.model)

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()
  
#   Inheritance Class Polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("vehical Brand:", self.brand, "Vehical Model:", self.model)

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print(self.brand, self.model)

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") 
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()