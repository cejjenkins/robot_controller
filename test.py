import sys
import unittest
from main import RobotController
from helpers import fix_input_grid, fix_input_start_pos, fix_input_moves

class TestRobot(unittest.TestCase):
    
    def test_1_test_input_start_pos(self):
        test_pos = fix_input_start_pos('0 0 E')
        self.assertEqual(type(test_pos[2]), str)

    def test_2_test_input_moves(self):
        test_moves = fix_input_moves('RFLFFLRF')
        self.assertEqual(test_moves, ['R', 'F', 'L', 'F', 'F', 'L', 'R', 'F'])

    def test_3_test_input_grid(self):
        test_grid = fix_input_grid('5 5')
        self.assertEqual(type(test_grid[0]), int)

    def test_3_test_robot_init(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('0 0 E'), fix_input_moves('RFLFFLRF'))
        self.assertEqual(test_bot.current_row, 0)
        self.assertEqual(test_bot.current_column, 0)
        self.assertEqual(test_bot.direction, 'E')
        self.assertEqual(test_bot.commands[-1], 'F')
    
    def test_4_turn_right(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('0 0 E'), fix_input_moves('RFLFFLRF'))
        test_bot.turn('R')
        self.assertEqual(test_bot.direction, 'S')

    def test_5_turn_left(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('0 0 E'), fix_input_moves('RFLFFLRF'))
        test_bot.turn('L')
        self.assertEqual(test_bot.direction, 'N')

    def test_7_move_horizontal_E(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('0 0 E'), fix_input_moves('RFLFFLRF'))
        test_bot.horizontal_move()
        self.assertEqual(test_bot.current_column, 1)

    def test_8_move_horizontal_W(self):
        test_bot = RobotController(fix_input_grid('5 5'),  fix_input_start_pos('2 0 W'), fix_input_moves('RFLFFLRF'))
        test_bot.vertical_move()
        self.assertEqual(test_bot.current_column, 2)

    def test_9_move_vertical_N(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('2 1 N'), fix_input_moves('RFLFFLRF'))
        test_bot.vertical_move()
        self.assertEqual(test_bot.current_row, 0)
    
    def test_10_move_vertical_S(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('3 3 S'), fix_input_moves('RFLFFLRF'))
        test_bot.vertical_move()
        self.assertEqual(test_bot.current_row, 4)
    
    def test_14_output(self):
        test_bot = RobotController(fix_input_grid('5 5'), fix_input_start_pos('0 0 E'), fix_input_moves('RFLFFLRF'))
        test_bot.make_your_moves()
        test_bot.new_position()
        self.assertEqual(test_bot.current_position, '3 1 E')
