# Local Scope
def MyFun():
    x = 10
    print(x)
MyFun()

# Function Inside Function
def MyFun():
    x = 20
    def  MyInnerFun():
        print(x)
    MyInnerFun()
        
MyFun()

# Global Scope
a = 200
def MyFun():
    print(a)
    def  MyInnerFun():
        print(a)
    MyInnerFun()
        
MyFun()

# Global Keyword

def MyFun():
    global y
    y = 250
    def  MyInnerFun():
        print(y)
    MyInnerFun()
        
MyFun()

print(y)