#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island represented by 1s."""

# Initialize total perimeter
    total_perimeter = 0

    # Loop through each row in the matrix
    for row in range(len(grid)):
        # Loop through each cell in the current row
        for col in range(len(grid[row])):
            # If the cell represents land (1)
            if grid[row][col] == 1:
                # Check the neighboring cells and boundaries

                # Check above
                if row == 0 or grid[row - 1][col] == 0:
                    total_perimeter += 1
                # Check below
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    total_perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    total_perimeter += 1
                # Check right
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    total_perimeter += 1

    # Return the calculated perimeter
    return total_perimeter
