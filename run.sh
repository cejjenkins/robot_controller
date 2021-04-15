#!/usr/bin/env python3.7
from main import RobotController
import sys

if __name__ == '__main__':
    print('Hi! Please enter the grid size')
    grid_size = input()
    print('Hi! Please enter the starting location')
    start_location = input()
    print('Hi! Please enter the moves you want me to make')
    moves = input()

    bot = RobotController(grid_size, start_location, moves)
    bot.make_your_moves()
    print(bot.new_position())
    sys.exit(0)
