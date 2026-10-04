#!/usr/bin/env python3
"""Module that computes the derivative of a polynomial"""


def poly_derivative(poly):
    """Return the derivative of a polynomial given as a coefficient list"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)) or isinstance(coef, bool):
            return None
    derivative = [poly[i] * i for i in range(1, len(poly))]
    if len(derivative) == 0 or all(c == 0 for c in derivative):
        return [0]
    return derivative
