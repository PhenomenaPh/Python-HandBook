import pandas as pd


def best(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df.copy()
    filtered_df = filtered_df.loc[
        (df["maths"] >= 4) & (df["physics"] >= 4) & (df["computer science"] >= 4)
    ]
    return filtered_df


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
