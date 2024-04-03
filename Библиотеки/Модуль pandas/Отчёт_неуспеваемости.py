import pandas as pd


def need_to_work_better(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df.copy()
    filtered_df = filtered_df.loc[
        (df["maths"] == 2) | (df["physics"] == 2) | (df["computer science"] == 2)
    ]
    return filtered_df
