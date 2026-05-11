# Libraries
import pandas as pd
import streamlit as st

# Functions
from services.google_sheets import get_sheet

from utils.data_type_helpers import ensure_list

# Variables
from config import (
    SK_MAIN_DATA,
    TB_MASTER_DATA,
    # Column Names
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD
)

# ===== READ MASTER DATA =====
@st.cache_data(ttl=300)
def get_master_data():
    # Load Master Data from Google Sheets
    sheet = get_sheet(SK_MAIN_DATA, TB_MASTER_DATA)
    
    values = sheet.get_all_values()
    headers = values[0]
    rows = values[1:]

    df = pd.DataFrame(rows, columns=headers)

    return df

def get_unique_categories(df):
    if df.empty:
        return []

    categories = (
        df[CATEGORY_COLUMN_MD]
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
            df[df[CATEGORY_COLUMN_MD].isin(category)][GROUP_COLUMN_MD]
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
                (df[CATEGORY_COLUMN_MD].isin(category))
                & (df[GROUP_COLUMN_MD].isin(group))
            ][TYPE_COLUMN_MD]
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

def get_unique_measurements(df, category, group, type_):
    category = ensure_list(category)
    group = ensure_list(group)
    type_ = ensure_list(type_)

    if category and group and type_:
        measurements = (
            df[
                (df[CATEGORY_COLUMN_MD].isin(category))
                & (df[GROUP_COLUMN_MD].isin(group))
                & (df[TYPE_COLUMN_MD].isin(type_))
            ][MEASUREMENT_COLUMN_MD]
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
