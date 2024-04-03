import numpy as np


def multiplication_matrix(n: int):
    matrix = np.arange(1, n + 1)
    new_matrix = np.outer(matrix, matrix)

    return new_matrix


print(multiplication_matrix(3))
