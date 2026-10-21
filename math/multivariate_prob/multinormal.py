#!/usr/bin/env python3
"""Module that defines the MultiNormal class"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Class constructor

        data: numpy.ndarray of shape (d, n)
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point

        x: numpy.ndarray of shape (d, 1)
        Returns: the value of the PDF
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        diff = x - self.mean
        exponent = -0.5 * np.matmul(np.matmul(diff.T, inv), diff)
        coef = 1 / np.sqrt(((2 * np.pi) ** d) * det)
        return coef * np.exp(exponent[0][0])
