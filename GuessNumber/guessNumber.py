import random

secretNumber = random.randint(1,10)
print('Welcome to the game, guess the number')
print('I thinked a number between 1 and 10')
print('You have 5 attempts. Good Luck!')

attempts = 1

while attempts <= 5:
    print ("attempt:", attempts)
    userInput = int(input())

    if userInput == secretNumber:
        print("Congrats, you won!")
        print("Attempts made: ", attempts)
        quit()
    elif userInput < secretNumber:
        print("Too low, try again: ")
        userInput
        attempts+=1
    elif userInput > secretNumber:
        print("Too high, try again: ")
        userInput
        attempts+=1
    else:
        print("invalid input")

    if attempts >= 6:
        print("You lost. The number was: ", secretNumber)
        

    



