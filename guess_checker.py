"""
File: guess_checker.py
Author: Blossom Akpedeye
Date: 09/30/20
Description: This file is to help students practice using 
             for and while loops on the UMBC GL servers
"""
## CODE BY ERIC HAMILTON ##
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])
###########################

if __name__ == "__main__":
    loop = True
    random_num = randint(1, 100)
    user_guess = " "
    guess_count = 0
    
    # This while loop takes a user's guess
    # and checks if its the same as the random_num generator
    # and gives the user hints  until they get it right
    while loop:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if 0 < user_guess < 100:
            if user_guess < random_num:
                print("Your number is too low.")
                guess_count += 1
            elif user_guess > random_num:
                print("Your number is too high")
                guess_count += 1
            elif user_guess == random_num:
                guess_count += 1
                print("You guessed the value!  It took you", guess_count, "steps.")
                loop = False
        else:
            loop = False
