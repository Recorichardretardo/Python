import random

friends = ["Rolf","Bob","Jen"]
print("Jen" in friends)

number = random.randint(2,9)	
user_input = input("Enter 'y' if you would like to play: ")
if user_input in ("y","Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("you guessed correctly!")
    else:
        print("Sorry, it's wrong!")