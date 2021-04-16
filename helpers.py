"""A few helper functions."""

from exceptions import InvalidInputException, InvalidCommandException


def fix_input_grid(s: str):
    """Splits the input for initial position and grid size."""
    return [int(i) for i in s.split(" ")]


def fix_input_start_pos(s: str):
    """Splits the input for initial position and grid size."""
    return [i for i in s.split(" ")]


def fix_input_moves(s: str):
    """Splits the input for moves."""
    return list(s)
