# Libraries
import pandas as pd

from utils.data_type_helpers import (
    ensure_list
)

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
    category = ensure_list(category)

    if category:
        groups = (
            df[df["category"].isin(category)]["group"]
            .dropna()
            .astype(str)
            .str.strip()
            .unique()
            .tolist()
        )

        return_val = sorted(groups)
    
    else:
        return_val = []
    
    return return_val

def get_unique_types(df, category, group):
    category = ensure_list(category)
    group = ensure_list(group)

    if category and group:
        types = (
            df[
                (df["category"].isin(category))
                & (df["group"].isin(group))
            ]["type"]
            .dropna()
            .astype(str)
            .str.strip()
            .unique()
            .tolist()
        )

        return_val = sorted(types)

    else:
        return_val = []
    
    return return_val

def get_unique_measurements(df, category, group, type):
    category = ensure_list(category)
    group = ensure_list(group)
    type = ensure_list(type)

    if category and group and type:
        measurements = (
            df[
                (df["category"].isin(category))
                & (df["group"].isin(group))
                & (df["type"].isin(type))
            ]["measurement"]
            .dropna()
            .astype(str)
            .str.strip()
            .unique()
            .tolist()
        )

        return_val = sorted(measurements)

    else:
        return_val = []

    return return_val
