a = 50
b = 30
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#   Ternary Operators,
  print("A") if a > b else print("=") if a == b else print("B")
  
#   Nested If
x = 36
if x > 20:
    print("above 20")
    if x > 40:
        print("above 40")
    else:
        print("not above 60")
        
else:
    print("not above 70")