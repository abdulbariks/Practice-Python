# While Loops
i = 1
while i <= 10:
    print(i)
    i=i+1
    
# The break Statement
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1
  
#   The continue Statement
i = 1
while i < 10:
    i +=1
    if i == 5:
        continue
    print(i)
    

# For Loops
person  = ["abdul", 'barik', 'mahaafuja']
for x in person:
    print(x)
    
# The break Statement
for x in person:
    # print(x)
    if x == 'barik':
        break
    print(x)
    
# The continue Statement
for x in person:
    if x == "barik":
        continue
    print(x)
    
# The range() Function
for x in range(10):
    print(x)
    
for x in range(10,15):
    print(x)
    
for x in range(2, 30, 3):
    print(x)
    
# Else in For Loop
for x in range(10):
    print(x)
else:
    print("finally done")
    
for x in range(10):
      if x == 5: break
      print(x)
else:
  print("Finally finished!")   
  
for x in range(10):
      if x == 5: continue
      print(x)
else:
  print("Finally finished!")  


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x ,y)