import pandas as pd


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}


def update(df: pd.DataFrame) -> pd.DataFrame:

    filtered_df = df.copy()
    filtered_df["average"] = filtered_df.iloc[:, 1:].mean(axis=1)
    filtered_df.sort_values(
        by=["average", "name"], inplace=True, ascending=[False, True]
    )

    return filtered_df


journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
