#!/usr/bin/env python3
"""Module that calculates the minor matrix of a matrix"""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculates the minor matrix of a matrix

    matrix: list of lists whose minor matrix should be calculated
    Returns: the minor matrix of matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError('matrix must be a list of lists')
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')
    if n == 1:
        return [[1]]
    result = []
    for i in range(n):
        result_row = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            result_row.append(determinant(sub))
        result.append(result_row)
    return result
