import numpy as np


def stairs(array):
    return np.concatenate([np.roll(array, i) for i in range(len(array))]).reshape(
        -1, len(array)
    )


print(stairs(np.arange(3)))
print(stairs(np.arange(5)))
