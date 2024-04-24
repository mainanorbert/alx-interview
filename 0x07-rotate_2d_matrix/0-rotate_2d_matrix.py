#!/usr/bin/python3
"""module to rotate 2D a matrix"""


def rotate_2d_matrix(matrix):
    """function to rotate a matrix"""
    mat = transpose(matrix)
    return [mat[::-1] for row in mat]


def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
