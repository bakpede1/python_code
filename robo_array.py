"""
File: robo_array.py
Author: Blossom Akpedeye
Date: 10/15/2020
"""

DOT = '.'
EMPTY = '' 

def print_robo_array(room):
    for row in room:
        for x in row:
            if not x:
                print(DOT.ljust(3), end=' ')
            else:
                print(str(x).ljust(3), end=' ')
        print()
    print()


def robo_vac(room, starting_y, starting_x):
    """
    Compute a path through the room for the robot vacuum.

    :param room: a 2d-grid representing the room,
                '' blank strings are open spaces
    :param starting_y: starting row (first index)
    :param starting_x: starting column (second index)
    :return: the updated room with the numbers.
    """
    row = starting_y
    col = starting_x
    count = int(1)
    loop = True
    room[row][col] = count
    while loop:
        if 0 <= col + 1 < len(room[0]) and room[row][col + 1] == EMPTY:
            count += 1   
            col += 1
            room[row][col] = count
        elif 0 <= row + 1 < len(room) and room[row + 1][col] == EMPTY:
            count += 1 
            row += 1
            room[row][col] = count
        elif 0 <= col - 1 < len(room[0]) and room[row][col - 1] == EMPTY:
            count += 1
            col -= 1
            room[row][col] = count
        elif 0 <= row - 1 < len(room) and room[row - 1][col] == EMPTY:
            count += 1
            row -= 1
            room[row][col] = count
        else:
            loop = False

    return room


if __name__ == '__main__':
    my_room = [['' for _ in range(6)] for _ in range(6)]
    print_robo_array(robo_vac(my_room, 0, 0))
    my_room_with_obstacles = [['' for _ in range(6)] for _ in range(6)]

    for i in range(3, 5):
        for j in range(3, 5):
            my_room_with_obstacles[i][j] = 'x'
    print_robo_array(robo_vac(my_room_with_obstacles, 0, 0))

    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 0))
    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 2))

    another_room = [
        ['', 'x', '', '', '', '', '', ''],
        ['', 'x', 'x', '', 'x', '', 'x', ''],
        ['', 'x', '', '', 'x', 'x', '', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', '', '', '', '', '', '']
    ]
    print_robo_array(robo_vac(another_room, 0, 0))
