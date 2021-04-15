from exceptions import OutsideGridException, InvalidInputException, InvalidCommandException

class RobotController:
    
    def __init__(self, size_of_grid, location, commands):
        self.size_of_grid = size_of_grid
        self.current_row = int(location[1])
        self.current_column = int(location[0])
        self.direction = location[2]
        self.commands = commands
        self.elements = ['N', 'E', 'S', 'W']
    
    def turn(self, command):
        if self.direction not in self.elements:
            raise InvalidInputException("You're input doesn't look right, direction should be a direction.")
        movement = -1 if command == 'L' else 1
        self.direction = self.elements[(self.elements.index(self.direction) + movement)%4]
        
    def vertical_move(self):
        #add error if called when direction is EW
        if self.direction == 'N':
            self.current_row =  self.current_row - 1
            self.is_valid_movement()
        if self.direction == 'S':
            self.current_row = self.current_row + 1
            self.is_valid_movement
    
    def horizontal_move(self):
        #add error if called when direction is NS
        if self.direction == 'W':
            self.current_column = self.current_column - 1
            self.is_valid_movement()
        if self.direction == 'E':
            self.current_column = self.current_column + 1
            self.is_valid_movement()
    
    def is_valid_movement(self):
        #check to see if you can move, or if it's at the edge
        if (self.current_column < 0) or (self.current_row < 0):
            raise OutsideGridException("This move will take the robot outside the grid.")
        if (self.current_column > self.size_of_grid[0]) or (self.current_row > self.size_of_grid[1]):
            raise OutsideGridException("This move will take the robot outside the grid.")

        
    def is_valid_command(self, command):
        #check to see if the command is one of the three options
        if command not in ['L', 'R', 'F']:
            raise InvalidCommandException(f"Sorry {command} is not a valid command.")


    def new_position(self):
        self.current_position = f'{self.current_column} {self.current_row} {self.direction}'
        return self.current_position
     
    def make_your_moves(self):
        for i in self.commands:
            self.is_valid_command(i)
            if i in ['L', 'R']:
                self.turn(i)
            elif (i == 'F') and (self.direction in ['N', 'S']):
                self.vertical_move()
            elif (i == 'F') and (self.direction in ['W', 'E']):
                self.horizontal_move()