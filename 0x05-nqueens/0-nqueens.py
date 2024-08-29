#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].

    This function checks if there is any queen in the same column or in the
    diagonals that can attack the queen at (row, col).

    Parameters:
    board (list): The N x N chessboard represented as a 2D list.
    row (int): The row index where the queen is to be placed.
    col (int): The column index where the queen is to be placed.
    N (int): The size of the chessboard (N x N).

    Returns:
    bool: True if it's safe to place the queen at (row, col), False otherwise.
    """
    # Check the column for any queens
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem using backtracking.

    This function attempts to place N queens on an N x N chessboard such that
    no two queens threaten each other. It generates all possible valid
    solutions.

    Parameters:
    N (int): The size of the chessboard (N x N).

    Returns:
    list: A list of solutions, where each solution is represented as a list
          of (row, col) positions of the queens.
    """
    # Initialize the board with all zeros (no queens placed)
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []  # This will store the list of valid solutions

    def solve(row):
        """
        Recursive backtracking function to place queens row by row.

        Parameters:
        row (int): The current row where a queen needs to be placed.
        """
        # If all queens are placed successfully
        if row == N:
            solution = []
            # Store the positions of the queens in the current solution
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        # Try placing the queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row][col] = 1
                # Recur to place the rest of the queens
                solve(row + 1)
                # Backtrack: remove the queen from the current position
                board[row][col] = 0

    # Start the solving process from the first row
    solve(0)
    return solutions


def main():
    """
    Main function to handle input validation, argument parsing, and solving
    the N Queens problem.

    This function ensures that the program is used correctly, validates the
    input, and prints the solutions to the N Queens problem for the given N.
    """
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try to convert the argument to an integer
        N = int(sys.argv[1])
    except ValueError:
        # If the conversion fails, print an error message and exit
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_nqueens(N)

    # Print all the solutions, one per line
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
