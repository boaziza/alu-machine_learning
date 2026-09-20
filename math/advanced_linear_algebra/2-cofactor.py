#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix"""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix

    matrix: list of lists whose cofactor matrix should be calculated
    Returns: the cofactor matrix of matrix
    """
    m = minor(matrix)
    return [[(-1) ** (i + j) * m[i][j] for j in range(len(m))]
            for i in range(len(m))]
