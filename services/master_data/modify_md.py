# Libraries
import pandas as pd

def get_unique_categories(df):
    if df.empty:
        return []

    categories = (
        df["category"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return sorted(categories)

def get_unique_groups(df, category):
    groups = (
        df[df["category"] == category]["group"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return sorted(groups)

def get_unique_types(df, category, group):
    types = (
        df[(df["category"] == category) & (df["group"] == group)]["type"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return sorted(types)
