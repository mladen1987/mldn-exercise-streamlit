import pandas as pd

from config import (
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD,
    EXERCISE_KEY_COLUMN_MD,
    EXERCISE_MEASUREMENT_KEY_COLUMN_MD,
    EXERCISE_MEASUREMENT_KEY_COLUMN,
    DATE_COLUMN
)

def get_types_for_group(
    master_data_df,
    category,
    group
):

    types = (
        master_data_df[
            (master_data_df[CATEGORY_COLUMN_MD] == category)
            & (master_data_df[GROUP_COLUMN_MD] == group)
        ][[
            TYPE_COLUMN_MD,
            MEASUREMENT_COLUMN_MD,
            UOM_COLUMN_MD,
            EXERCISE_KEY_COLUMN_MD,
            EXERCISE_MEASUREMENT_KEY_COLUMN_MD
        ]]
        .drop_duplicates()
        .sort_values([TYPE_COLUMN_MD, MEASUREMENT_COLUMN_MD])
        .to_dict(orient="records")
    )

    return types

def group_measurements_by_type(type_rows):

    grouped = {}

    for row in type_rows:

        type_name = row[TYPE_COLUMN_MD]

        if type_name not in grouped:
            grouped[type_name] = []

        grouped[type_name].append(row)

    return grouped

def get_recent_measurement_history(
    master_data_df,
    exercise_data_df,
    category,
    group,
    limit=5
):

    # ===== Get relevant master data rows =====
    md_filtered = (
        master_data_df[
            (master_data_df[CATEGORY_COLUMN_MD] == category)
            & (master_data_df[GROUP_COLUMN_MD] == group)
        ][[
            EXERCISE_MEASUREMENT_KEY_COLUMN_MD,
            TYPE_COLUMN_MD,
            MEASUREMENT_COLUMN_MD,
            UOM_COLUMN_MD
        ]]
        .drop_duplicates()
    )

    if md_filtered.empty:
        return pd.DataFrame()

    measurement_keys = (
        md_filtered[EXERCISE_MEASUREMENT_KEY_COLUMN_MD]
        .dropna()
        .unique()
        .tolist()
    )

    # ===== Filter exercise history =====
    history_df = (
        exercise_data_df[
            exercise_data_df[EXERCISE_MEASUREMENT_KEY_COLUMN]
            .isin(measurement_keys)
        ]
        .copy()
    )

    if history_df.empty:
        return pd.DataFrame(columns=[
            TYPE_COLUMN_MD,
            MEASUREMENT_COLUMN_MD,
            UOM_COLUMN_MD,
            DATE_COLUMN,
            "value"
        ])

    # ===== Convert date =====
    history_df[DATE_COLUMN] = pd.to_datetime(
        history_df[DATE_COLUMN]
    )

    # ===== Merge labels (INCLUDING UOM) =====
    history_df = history_df.merge(
        md_filtered,
        left_on=EXERCISE_MEASUREMENT_KEY_COLUMN,
        right_on=EXERCISE_MEASUREMENT_KEY_COLUMN_MD,
        how="left"
    )

    # ===== Sort newest first =====
    history_df = history_df.sort_values(
        [EXERCISE_MEASUREMENT_KEY_COLUMN, DATE_COLUMN],
        ascending=[True, False]
    )

    # ===== Keep latest N per measurement key =====
    history_df = (
        history_df
        .groupby(EXERCISE_MEASUREMENT_KEY_COLUMN)
        .head(limit)
        .copy()
    )

    # ===== Final columns =====
    history_df = history_df[[
        TYPE_COLUMN_MD,
        MEASUREMENT_COLUMN_MD,
        UOM_COLUMN_MD,
        DATE_COLUMN,
        "value"
    ]]

    return history_df
