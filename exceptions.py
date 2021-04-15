class InvalidInputException(Exception):
    """Raises Exception when input is incorrect."""
    pass 

class InvalidCommandException(Exception):
    """Raises Exception when the command is incorrect."""
    pass 

class OutsideGridException(Exception):
    """Raises Exception the move would take the robot outside the grid."""
    pass 