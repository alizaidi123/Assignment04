# User Guessing Comp's Number

import random as rd
def gmn():
    num = rd.randint(0,99)
    for i in range(1):
        print("You Have 5 Turns to Guess my Number")
        for i in range(5):
            user = int(input("Guess my number"))
            if user == num:
                print("You Won!, Your guess is Correct!")
                break
            elif user > num:
                print("Oh No!, Guess a lower number")
            elif user < num:
                print("Oh No!, Guess a higher number")
        print("Game Over! Better Luck Next Time ")



gmn()
