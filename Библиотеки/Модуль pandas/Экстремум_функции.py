from typing import Hashable

import pandas as pd
import numpy as np


def values(func: callable, start: float, end: float, step: float) -> pd.Series:

    func_values = {value: func(value) for value in np.arange(start, end + step, step)}
    return pd.Series(func_values)


def min_extremum(df: pd.Series) -> Hashable:

    return df.idxmin()


def max_extremum(df: pd.Series) -> Hashable:
    return df.idxmax()


data = values(lambda x: x**2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
