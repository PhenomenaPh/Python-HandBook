import numpy as np


def make_board(n):
    array = np.zeros((n, n), dtype="int8")

    array[1::2, 1::2] = 1
    array[::2, ::2] = 1

    return array


print(make_board(4))
