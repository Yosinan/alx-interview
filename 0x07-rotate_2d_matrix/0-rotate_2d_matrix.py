#!/usr/bin/python3
"""
rotating a matrix
"""


def rotate_2d_matrix(matrix):
    """rotate by transposing and reversing the cols and rows"""
    matrix[:] = [[row[i] for row in reversed(matrix)] for i in range(len(matrix[0]))]

