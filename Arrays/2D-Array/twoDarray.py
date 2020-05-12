import numpy as np
from scipy import signal


def hourglassSum(arr):
    kernel = np.array([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
    return np.amax(signal.convolve2d(arr, kernel, 'same'))


if __name__ == '__main__':
    arr = np.array([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
                   0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
    print(hourglassSum(arr))
