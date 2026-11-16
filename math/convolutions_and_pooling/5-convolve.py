#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple kernels"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Performs a convolution on images using multiple kernels

    images: numpy.ndarray of shape (m, h, w, c)
    kernels: numpy.ndarray of shape (kh, kw, c, nc)
    padding: tuple of (ph, pw), 'same', or 'valid'
    stride: tuple of (sh, sw)
    Returns: numpy.ndarray containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride
    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant', constant_values=0)
    oh = (h + 2 * ph - kh) // sh + 1
    ow = (w + 2 * pw - kw) // sw + 1
    output = np.zeros((m, oh, ow, nc))
    for i in range(oh):
        for j in range(ow):
            for k in range(nc):
                x = i * sh
                y = j * sw
                window = padded[:, x:x + kh, y:y + kw, :]
                output[:, i, j, k] = np.sum(window * kernels[:, :, :, k],
                                            axis=(1, 2, 3))
    return output
