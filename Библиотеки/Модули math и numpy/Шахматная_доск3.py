import numpy as np


def snake(m, n, direction: str = "H"):
    matrix = np.arange(1, m * n + 1, dtype="int16")

    if direction == "H":
        matrix = matrix.reshape(n, m)
        matrix[1::2, ::] = matrix[1::2, ::-1]

    elif direction == "V":
        matrix = matrix.reshape(m, n).T
        matrix[:, 1::2] = np.flip(matrix[:, 1::2], axis=0)

    return matrix


print(snake(5, 3, direction="V"))
