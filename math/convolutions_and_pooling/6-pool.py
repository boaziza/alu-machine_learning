#!/usr/bin/env python3
"""Module that performs pooling on images"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Performs pooling on images

    images: numpy.ndarray of shape (m, h, w, c)
    kernel_shape: tuple of (kh, kw)
    stride: tuple of (sh, sw)
    mode: 'max' for max pooling or 'avg' for average pooling
    Returns: numpy.ndarray containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride
    oh = (h - kh) // sh + 1
    ow = (w - kw) // sw + 1
    output = np.zeros((m, oh, ow, c))
    for i in range(oh):
        for j in range(ow):
            x = i * sh
            y = j * sw
            window = images[:, x:x + kh, y:y + kw, :]
            if mode == 'max':
                output[:, i, j, :] = np.max(window, axis=(1, 2))
            else:
                output[:, i, j, :] = np.mean(window, axis=(1, 2))
    return output
