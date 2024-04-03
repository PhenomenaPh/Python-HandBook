import pandas as pd


left_upper = tuple(map(int, input().split()))
right_lower = tuple(map(int, input().split()))


df = pd.read_csv("data.csv")

df = df.loc[
    (df["x"] >= left_upper[0])
    & (df["x"] <= right_lower[0])
    & (df["y"] <= left_upper[1])
    & (df["y"] >= right_lower[1])
]

print(df)
