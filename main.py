from helpers import fix_input_moves, fix_input_start

class RobotController:
    
    def __init__(self, size_of_grid, location, commands):
        self.size_of_grid = fix_input_start(size_of_grid)
        self.init_location = fix_input_start(location)
        self.current_row = int(self.init_location[1])
        self.current_column = int(self.init_location[0])
        self.direction = self.init_location[2]
        self.commands = fix_input_moves(commands)
        self.elements = ['N', 'E', 'S', 'W']
    
    def turn(self, command):
        movement = -1 if command == 'L' else 1
        self.direction = self.elements[(self.elements.index(self.direction) + movement)%4]
        
    def vertical_move(self):
        #add error if called when direction is EW
        if self.direction == 'N':
            self.current_row =  self.current_row - 1
        if self.direction == 'S':
            self.current_row = self.current_row + 1
    
    def horizontal_move(self):
        #add error if called when direction is NS
        if self.direction == 'W':
            self.current_column = self.current_column - 1
        if self.direction == 'E':
            self.current_column = self.current_column + 1
    
#     def is_valid_movement(self):
        #check to see if you can move, or if it's at the edge
        
#     def is_valid_command(self):
#         #check to see if the command is one of the three options

    def new_position(self):
        self.current_position = f'{self.current_column} {self.current_row} {self.direction}'
        return self.current_position
     
    def make_your_moves(self):
        for i in self.commands:
            if i in ['L', 'R']:
                self.turn(i)
            elif (i == 'F') and (self.direction in ['N', 'S']):
                self.vertical_move()
            elif (i == 'F') and (self.direction in ['W', 'E']):
                self.horizontal_move()