#!/usr/bin/env python3
"""Module that performs a same convolution on grayscale images"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images

    images: numpy.ndarray of shape (m, h, w)
    kernel: numpy.ndarray of shape (kh, kw)
    Returns: numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph = max((kh - 1) // 2, kh // 2)
    pw = max((kw - 1) // 2, kw // 2)
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                    mode='constant', constant_values=0)
    output = np.zeros((m, h, w))
    for i in range(h):
        for j in range(w):
            window = padded[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(window * kernel, axis=(1, 2))
    return output
