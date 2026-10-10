#!/usr/bin/env python3
"""Module that defines a Normal distribution"""


class Normal:
    """Represents a normal distribution"""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the distribution

        Args:
            data: list of the data used to estimate the distribution
            mean: mean of the distribution
            stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value

        Args:
            x: x-value

        Returns:
            The z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score

        Args:
            z: z-score

        Returns:
            The x-value of z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value

        Args:
            x: x-value

        Returns:
            The PDF value for x
        """
        exponent = -0.5 * (self.z_score(x) ** 2)
        coefficient = 1 / (self.stddev * ((2 * self.pi) ** 0.5))
        return coefficient * (self.e ** exponent)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value

        Args:
            x: x-value

        Returns:
            The CDF value for x
        """
        v = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf = (2 / (self.pi ** 0.5)) * (v - (v ** 3) / 3 + (v ** 5) / 10 -
                                        (v ** 7) / 42 + (v ** 9) / 216)
        return 0.5 * (1 + erf)
