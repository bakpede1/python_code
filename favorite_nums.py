"""
File: favorite_nums.py
Author: Blossom Akpedeye
Date: 10/21/2020
Description: This file is to help students practice using
             dictionaries on the UMBC GL servers
"""


def print_favorite_numbers(who, favorites):
    """
    This function prints favorite numbers 
    
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """
    if who not in favorites:
        print(who, 'wasn\'t in fsvorites')
    else:
        print(favorites[who])



def add_favorite_number(who, number, favorites):
    """
    This function add a person's favorite numbers
    
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """
    unique = True
    for the_key in favorites:
        if number in favorites[the_key]:
            print(number, 'was found in', the_key,'\'s', 'favorites')
            unique = False
    if unique:
        if who in favorites:
            favorites[who].append(number)
        else:
            favorites[who] = []
            favorites[who].append(number)
        print(number, 'added to', who,'\'s', 'favorites')



if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            who, num = in_string.split()
            num = int(num)
            add_favorite_number(who, num, favorites)

        in_string = input('What do you want to do (add favorite number), or quit? ')
