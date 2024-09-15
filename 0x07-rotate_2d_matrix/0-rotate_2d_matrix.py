#!/usr/bin/python3
"""
Rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotate the given n x n 2D matrix"""
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
