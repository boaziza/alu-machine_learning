#!/usr/bin/env python3
"""Module that calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """Calculates a correlation matrix from a covariance matrix

    C: numpy.ndarray of shape (d, d)
    Returns: numpy.ndarray of shape (d, d) with the correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    std = np.sqrt(np.diag(C))
    return C / np.outer(std, std)
