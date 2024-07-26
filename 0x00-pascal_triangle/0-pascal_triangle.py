#!/usr/bin/python3
"""
this module is Responsible to make pascal Triangle
"""


def pascal_triangle(n):
    """
    Function to return Pascal's triangle
    :param n: number of rows in the triangle
    :return: list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []

    for row_number in range(n):
        # Start the row with a '1'
        row = [1]

        # Each triangle element (except the first and last of each row)
        # is equal to the sum of the elements above-and-to-the-left and
        # above-and-to-the-right.
        if row_number > 0:
            for col in range(1, row_number):
                row.append(
                    triangle[row_number - 1][col - 1] +
                    triangle[row_number - 1][col])
            row.append(1)

        triangle.append(row)

    return triangle
