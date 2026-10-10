#!/usr/bin/env python3
"""Module that defines a Binomial distribution"""


class Binomial:
    """Represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the distribution

        Args:
            data: list of the data used to estimate the distribution
            n: number of Bernoulli trials
            p: probability of a "success"
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - variance / mean
            self.n = int(round(mean / p))
            self.p = float(mean / self.n)

    @staticmethod
    def factorial(x):
        """Calculates the factorial of a non-negative integer

        Args:
            x: non-negative integer

        Returns:
            The factorial of x
        """
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes

        Args:
            k: number of "successes"

        Returns:
            The PMF value for k
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        combinations = self.factorial(self.n) // (
            self.factorial(k) * self.factorial(self.n - k))
        return combinations * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes

        Args:
            k: number of "successes"

        Returns:
            The CDF value for k
        """
        k = int(k)
        if k < 0:
            return 0
        if k > self.n:
            k = self.n
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
