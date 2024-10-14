mytuple  = ('abdul', 'barik', 'mahafuja', 'maimuna')
print(mytuple)
# All these objects have a iter() method which is used to get an iterator:
myier = iter(mytuple)
print(next(myier))
print(next(myier))
print(next(myier))


# Create an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 2
        return self
    
    def __next__(self):
        x = self.a
        self.a +=2
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stop Iteration
class MyNumbers:
    def __iter__(self):
        self.a = 2
        return self
    
    def __next__(self):
        if self.a <=20:
          x = self.a
          self.a +=2
          return x
        else:
            raise StopIteration
            
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
