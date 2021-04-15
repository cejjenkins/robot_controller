def fix_input_start(s):
    """Splits the input for initial position and grid size."""
    return [i for i in s.split(" ")]

def fix_input_moves(s):
    """Splits the input for moves."""
    return list(s)