f = open("demofile.txt", "r")
# print(f.read())
print(f.readline())
f.close()
# print(f.read(5))

# for x in f:
#   print(x)

# "a" - Append - will append to the end of the file
f = open("demofile2.txt", "a")
f.write("\nNow my age is 28")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# "w" - Write - will overwrite any existing content
f = open("demofile3.txt", "w")
f.write("my age is 28")
f.close()

f = open("demofile3.txt", "r")
print(f.read())


# Check if File exist:
import os
if os.path.exists("demofiles.txt"):
  os.remove("demofiles.txt")
else:
  print("The file does not exist")
  
# Delete Folder
# import os
# os.rmdir("myfolder")