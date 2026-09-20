#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix"""
determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Calculates the inverse of a matrix

    matrix: list of lists whose inverse should be calculated
    Returns: the inverse of matrix, or None if matrix is singular
    """
    adj = adjugate(matrix)
    det = determinant(matrix)
    if det == 0:
        return None
    return [[value / det for value in row] for row in adj]
