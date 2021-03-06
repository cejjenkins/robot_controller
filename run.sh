#!/usr/bin/env python3
import sys

from exceptions import InvalidInputException, InvalidCommandException
from helpers import fix_input_grid, fix_input_start_pos, fix_input_moves
from main import RobotController

if __name__ == '__main__':
    print('Hi! Please enter the grid size')
    grid_size = fix_input_grid(input())
    if len(grid_size) != 2:
        raise InvalidInputException("Your input doesn't look right, you need two numbers separated by a space.")
    print('Hi! Please enter the starting location')
    start_location = fix_input_start_pos(input())
    if len(start_location) != 3:
        raise InvalidInputException("Your input doesn't look right, you need two numbers and a direction a separated by spaces.")
    print('Hi! Please enter the moves you want me to make')
    moves = fix_input_moves(input())

    bot = RobotController(grid_size, start_location, moves)
    bot.move()
    print(bot.position())
    sys.exit(0)
