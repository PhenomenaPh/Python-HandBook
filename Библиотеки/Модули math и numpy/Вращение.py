import numpy as np


def rotate(matrix, rotation):
    rotates = rotation // 90
    return np.rot90(matrix, k=-rotates)


print(rotate(np.arange(12).reshape(3, 4), 90))
