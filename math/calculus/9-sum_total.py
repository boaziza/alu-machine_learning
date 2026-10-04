#!/usr/bin/env python3
"""Module that computes the sum of squares from 1 to n"""


def summation_i_squared(n):
    """Return the sum of i^2 for i from 1 to n, or None if n is invalid"""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
