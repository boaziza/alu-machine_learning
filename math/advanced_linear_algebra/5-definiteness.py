#!/usr/bin/env python3
"""Module that calculates the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix

    matrix: numpy.ndarray of shape (n, n) whose definiteness is calculated
    Returns: 'Positive definite', 'Positive semi-definite',
             'Negative semi-definite', 'Negative definite' or 'Indefinite',
             or None if matrix is not a valid (square, symmetric) matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError('matrix must be a numpy.ndarray')
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or
            matrix.shape[0] == 0):
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)
    tol = 1e-10 * max(1.0, np.max(np.abs(eigenvalues)))
    if np.all(eigenvalues > tol):
        return 'Positive definite'
    if np.all(eigenvalues >= -tol):
        return 'Positive semi-definite'
    if np.all(eigenvalues < -tol):
        return 'Negative definite'
    if np.all(eigenvalues <= tol):
        return 'Negative semi-definite'
    return 'Indefinite'
