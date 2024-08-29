#!/usr/bin/python3
"""N Queens Problem Solver Module."""

import sys

queen_positions = []
"""Stores all possible solutions for the N Queens problem."""

board_size = 0
"""Size of the N x N chessboard."""

possible_positions = None
"""Stores all potential positions on the chessboard."""


def validate_input():
    """Validates and retrieves the input size for the chessboard.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return size


def in_conflict(pos1, pos2):
    """Determines if two queens are in a position to attack each other.

    Args:
        pos1 (list or tuple): Position of the first queen.
        pos2 (list or tuple): Position of the second queen.

    Returns:
        bool: True if the queens can attack each other, otherwise False.
    """
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def solution_exists(current_group):
    """Checks if a given solution already exists in the list of solutions.

    Args:
        current_group (list of integers): A potential solution group.

    Returns:
        bool: True if the solution exists, otherwise False.
    """
    for sol in queen_positions:
        if all(pos in current_group for pos in sol):
            return True
    return False


def find_solutions(row, current_group):
    """Recursively finds all solutions for the N Queens problem.

    Args:
        row (int): The current row to place a queen.
        current_group (list of lists of integers):
            A group representing the current board configuration.
    """
    if row == board_size:
        if not solution_exists(current_group):
            queen_positions.append(current_group.copy())
    else:
        for col in range(board_size):
            index = (row * board_size) + col
            current_group.append(possible_positions[index].copy())
            if not any(
                in_conflict(possible_positions[index], pos)
                for pos in current_group[:-1]
            ):
                find_solutions(row + 1, current_group)
            current_group.pop()


def compute_solutions():
    """Initializes the positions and triggers the solution-building process."""
    global possible_positions
    possible_positions = [
        [i // board_size, i % board_size] for i in range(board_size**2)
    ]
    find_solutions(0, [])


# Main Execution
board_size = validate_input()
compute_solutions()
for sol in queen_positions:
    print(sol)
