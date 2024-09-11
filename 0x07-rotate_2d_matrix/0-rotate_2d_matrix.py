#!/usr/bin/python3
"""0x07. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix) -> None:
    """
    0x07. Rotate 2D Matrix

    args:
        matrix: matrix to rotate

    return: none
    """
    matrix.reverse()

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if row < column:
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
