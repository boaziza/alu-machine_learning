# Convolutions and Pooling

Convolution and pooling on images implemented with NumPy only.

| File | Description |
|------|-------------|
| `0-convolve_grayscale_valid.py` | Valid convolution on grayscale images |
| `1-convolve_grayscale_same.py` | Same convolution on grayscale images |
| `2-convolve_grayscale_padding.py` | Convolution with custom zero padding |
| `3-convolve_grayscale.py` | Convolution with padding (`same` / `valid` / custom) and stride |
| `4-convolve_channels.py` | Convolution on images with channels |
| `5-convolve.py` | Convolution with multiple kernels |
| `6-pool.py` | Max / average pooling |

## Key ideas
- **Convolution**: slide a kernel over the image; at each position multiply element-wise and sum.
- **Kernel / filter**: a small matrix of weights that detects a feature (e.g. edges).
- **Padding**: zeros added around the image border.
  - **valid**: no padding, output shrinks to `h - kh + 1`.
  - **same**: pad so the output keeps the input size.
- **Stride**: how many pixels the kernel moves each step.
- **Channels**: depth of the image (e.g. 3 for RGB).
- **Max / average pooling**: downsample by taking the max or the mean of each window.

Output size: `floor((h + 2*ph - kh) / sh) + 1`
