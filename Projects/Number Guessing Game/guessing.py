import random

randomNumber = random.randrange(1,5)
userInput = int(input("Guess The Number:"))

if userInput > randomNumber:
    print(randomNumber)
    print("The Number is to High")
elif randomNumber > userInput:
    print(randomNumber)
    print("The Number is to Low")
else:
    print(randomNumber)
    print("The Number is Match")
    