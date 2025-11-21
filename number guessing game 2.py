# Number guessing game
import random
name= input("Please enter your name: ")
print(f"Welcome to the game,Dear {name}")
print("These are the rules of the game",
      "You will need to guess a number between 1 and 100 ")
number= random.randrange(0,100)
tupleLevels=(1,2,3)

level=input("Please select the level you want to play: Enter 1 for hard, 2 for medium and 3 for easy: ")
try:
    level=int(level)
    if level==1:
        print("➡Your chose hard and your have 3 chances :")
    elif level==2:
        print("➡➡Your chose medium level and your have 5 chances :")
    elif level == 3:
        print("➡➡➡Your chose easy and your have 10 chances")
    elif level not in (1,2,3):
        print("Please a number between 1 and 3")
except ValueError:
    print("You entered an invalid choice💔,Please Enter a valid level")

if level==1:
    count=3
    times=0
    while count>0:
        userInput= int(input("please enter your guess: "))
        count = count - 1
        times+=1
        if userInput==number:
            print(f"Your are the best amigo, your got it in{times} attempts")
            break
        elif userInput>number:
            print("Your guess is greater than the number ")
        elif userInput<number:
            print("Your guess is less than the number")

elif level==2:
    count = 5
    times=0
    while count > 0:
        userInput = int(input("please enter your guess: "))
        count = count - 1
        times+=1
        if userInput == number:
            print(f"Your are the best amigo, your got it in{times} attempts")
            break
        elif userInput > number:
            print("Your guess is greater than the number ")
        elif userInput < number:
            print("Your guess is less than the number")

elif level==3:
    count = 10
    times=0
    while count > 0:
        userInput = int(input("please enter your guess: "))
        count = count - 1
        times+=1
        if userInput == number:
            print(f"Your are the best amigo, your got it in{times} attempts")
            break
        elif userInput > number:
            print("Your guess is greater than the number ")
        elif userInput < number:
            print("Your guess is less than the number")

