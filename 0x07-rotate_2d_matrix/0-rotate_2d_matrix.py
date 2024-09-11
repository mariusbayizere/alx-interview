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

    for xx in range(len(matrix)):
        for yy in range(len(matrix)):
            if xx < yy:
                matrix[xx][yy], matrix[yy][xx] = (
                    matrix[yy][xx],
                    matrix[xx][yy],
                )


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
