from config import (
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD,
    EXERCISE_KEY_COLUMN_MD,
    EXERCISE_MEASUREMENT_KEY_COLUMN_MD
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
