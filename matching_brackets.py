"""
File:    matching_brackets.py
Author:  Blossom Akpedeye
Date:    11/01/2020
Description: This file is to help students practice
             using recursion with functions on the GL
             servers for CMSC 201
"""

START_BRACKET = '{'
END_BRACKET = '}'
CHARS = 'abcdefghijklmnopqrstuvwxyz'
QUIT_STRING = 'quit'


def match_brackets(bracket_string, count):
    """
    This is a recursive function to
    find whether a string contains matched brackets
    :param: bracket_string: a string containing brackets
    :param: count: count test value i.e. to test whether brackets
                   match or do not match
    """
    if len(bracket_string) == 0:
        if count == 0:
            return True
        else:
            return False
    elif count < 0:
        return False
    else:
        if bracket_string[0] == START_BRACKET:
            return match_brackets(bracket_string[1:], count + 1)
        elif bracket_string[0] in CHARS:
            return match_brackets(bracket_string[1:], count)
        elif bracket_string[0] == END_BRACKET:
            return match_brackets(bracket_string[1:], count - 1)


if __name__ == '__main__':
    string_input = ''
    while string_input != QUIT_STRING:
        string_input = input('Enter a string with brackets: ')
        print(match_brackets(string_input, count=0))
