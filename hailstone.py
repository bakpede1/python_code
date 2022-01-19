# File:    hailstone.py
# Started: by Dr. Gibson
# Author:  Blossom Akpedeye
# Date:    11/04/20
# Description:
#   This file contains python code that implements the
#   "flight" of a hailstone, following the HOTPO rules
#   (also known as the Collatz Conjecture), recursively

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
# flight() recursively calculates the path of a hailstone
# Input:   the height of the hailstone
# Output:  a recursive call, which at the end returns 
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height):
    """This function counts the amount of steps it
    takes for the hailstone to get to the ground
    :param: height: the height of the hailstone"""
    if height <= 0:
        print('invalid')
        return 0
    elif height == 1:
        return 0
    else:
        print('Height of', height)
        if height % 2 == 0:
            number = 1 + flight(height // 2)
            return number
        elif height % 2 == 1:
            number = flight(height * 3 + 1)
            return number

          
    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0

    # stops when it reaches height of 1 (the ground)

    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2

    # if the current height is odd, multiply it by 3, then add 1

 
def main():
    """
    This function counts hailstone steps
    """
    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))

    # recursive call goes here
    steps = flight(startHeight)
    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")


main()
