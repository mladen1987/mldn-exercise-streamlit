import pandas as pd

from services.google_sheets import get_sheet
from services.master_data.read_md import get_master_data

from config import (
    SK_MAIN_DATA,
    TB_MAIN_DATA,

    # Exercise Data columns
    EXERCISE_KEY_COLUMN,
    DATE_COLUMN,

    # Master Data columns
    EXERCISE_KEY_COLUMN_MD,
    GROUP_COLUMN_MD,
    CATEGORY_COLUMN_MD
)


def get_exercise_data():

    sheet = get_sheet(SK_MAIN_DATA, TB_MAIN_DATA)

    data = sheet.get_all_records()

    return pd.DataFrame(data)


def get_latest_exercise_dates(exercise_data_df):

    required_columns = [
        EXERCISE_KEY_COLUMN,
        DATE_COLUMN
    ]

    if not all(col in exercise_data_df.columns for col in required_columns):
        return pd.DataFrame()

    # Convert date column
    exercise_data_df[DATE_COLUMN] = pd.to_datetime(
        exercise_data_df[DATE_COLUMN]
    )

    # Latest date per exercise
    latest_dates_df = (
        exercise_data_df
        .groupby(EXERCISE_KEY_COLUMN)[DATE_COLUMN]
        .max()
        .reset_index()
    )

    return latest_dates_df


def get_recommended_group(latest_dates_df, master_data_df, category_value):

    # Filter category
    md_lookup = (
        master_data_df[
            master_data_df[CATEGORY_COLUMN_MD] == category_value
        ][[
            EXERCISE_KEY_COLUMN_MD,
            GROUP_COLUMN_MD
        ]]
        .drop_duplicates()
    )

    # Merge latest dates onto master data
    latest_dates_per_group = (
        md_lookup
        .merge(
            latest_dates_df,
            left_on=EXERCISE_KEY_COLUMN_MD,
            right_on=EXERCISE_KEY_COLUMN,
            how="left"
        )
        .groupby(GROUP_COLUMN_MD)[DATE_COLUMN]
        .max()
        .reset_index()
    )

    latest_dates_per_group[DATE_COLUMN] = (
        latest_dates_per_group[DATE_COLUMN]
        .fillna(pd.Timestamp("1900-01-01"))
    )
    
    if latest_dates_per_group.empty:
        return None
    
    # Oldest latest workout
    recommended_group = (
        latest_dates_per_group
        .sort_values(DATE_COLUMN, ascending=True)
        .iloc[0][GROUP_COLUMN_MD]
    )

    return recommended_group
