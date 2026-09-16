#!/usr/bin/env python3
"""Performs element-wise addition, subtraction, multiplication, division."""


def np_elementwise(mat1, mat2):
    """Return the element-wise sum, difference, product, and quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
