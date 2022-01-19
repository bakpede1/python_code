"""
File:    the_third_degree.py
Author:  Blossom Akpedeye
Date:    11/01/2020
Description: This file is to help students practice
             using recursion in functions on the GL
             servers for CMSC 201
"""


def the_third_degree(n):
    """This is a recursive function to find the
    third degree of any set of numbers
    :param: n: a number
    :return: the third degree answer
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 5
    else:
        return 3 * (the_third_degree(n - 1)) + 2 * (the_third_degree(n - 2)) + (the_third_degree(n - 3))


if __name__ == '__main__':
    for i in range(10):
        print(the_third_degree(i))
