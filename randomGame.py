import sys
from random import randint

min = 1
max = 20

def intro():
    print("Welcom to the Random Game")
    print("To play, enter a number from {} to {} when prompted. Thy goal is to guess the same number as the computer.".format(min, max))
    prompt()

def prompt():
    number = randint(min, max)
    usrStr = input("\nEnter your guess here: ")

    try:
        usrInt = int(usrStr)
    except:
        usrInt = min - 10
        print("You did not enter a valid answer. This will result in a incorrect guess.")

    if usrInt == number:
        repStr = input("Good job! You guessed the correct number! Wuold you like to play again? (y/n) ") 
    else:
        repStr = input("Oh No! You guessed the wrong number! Wuold you like to play again? (y/n) ")

    if repStr == 'y':
        prompt()
    else:
        outro()

def outro():
    print(" Thank you for playing! Have a nice day! :)")
    input("(press enter to exit)")
    sys.exit()

if __name__ == '__main__':
    intro()
