"""
File:    houses_and_people.py
Author:  Blossom Akpedeye
Date:    11/01/2020
Description: This file is to help students practice
             using classes and functions on the GL
             servers for CMSC 201
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.the_house = ''

    def go_in(self, house):
        if self.name not in house.occupants:
            house.occupants.append(self.name)
            self.the_house = house
        else:
            print(self.name + ' is already in house')

    def leave(self, house):
        if self.name in house.occupants:
            house.occupants.remove(self.name)
        else:
            print(self.name + ' is not in the house')


class House:
    def __init__(self, address):
        self.address = address
        self.occupants = []

    def display(self):
        print('The house is at: ' + self.address)
        for occupant in self.occupants:
            print('\t', occupant)


if __name__ == '__main__':
    # CODE BELOW BY ERIC HAMILTON
    print('The options are:\n\tcreate <person name>\n\tperson-name enter house-address\n\tperson-name exit house-address\n\tdisplay')
    in_string = input('What do you want to do? ')
    people_list = []
    house_list = []
    while in_string.strip().lower() not in ['quit', 'q']:
        enter_string = in_string.split('enter')
        exit_string = in_string.split('exit')
        if in_string.split()[0:2] == ['create', 'person']:
            people_list.append(Person(' '.join(in_string.split()[2:])))
            print('Person {} created'.format(people_list[-1].name))
        elif in_string.split()[0:2] == ['create', 'house']:
            house_list.append(House(' '.join(in_string.split()[2:])))
            print('House {} created'.format(house_list[-1].address))
        elif len(enter_string) == 2:
            if not any(enter_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(enter_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == enter_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == enter_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.go_in(the_house)
                else:
                    print('Something went wrong.  ')
        elif len(exit_string) == 2:
            if not any(exit_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(exit_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == exit_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == exit_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.leave(the_house)
                else:
                    print('Something went wrong.  ')
        elif in_string.lower().strip() == 'display':
            for house in house_list:
                house.display()
            print('These people aren\'t in a house')
            for person in people_list:
                if not person.the_house:
                    print(person.name)

        in_string = input('What do you want to do? ')
