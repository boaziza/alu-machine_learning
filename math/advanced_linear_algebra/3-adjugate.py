#!/usr/bin/env python3
"""Module that calculates the adjugate matrix of a matrix"""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix

    matrix: list of lists whose adjugate matrix should be calculated
    Returns: the adjugate matrix of matrix
    """
    c = cofactor(matrix)
    n = len(c)
    return [[c[j][i] for j in range(n)] for i in range(n)]
