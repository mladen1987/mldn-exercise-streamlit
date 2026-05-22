import pandas as pd

# Modules
from services.google_sheets import (
    overwrite_sheet
)

from utils.data_type_helpers import ensure_list

# Variables
from config import (
    SK_MAIN_DATA,
    TB_MASTER_DATA,
    # Column Names
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    SUB_GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD,
    EXERCISE_KEY_COLUMN_MD,
    EXERCISE_MEASUREMENT_KEY_COLUMN_MD
)

def build_new_master_data_rows(category, group, sub_group, type_, measurements):
    new_rows = []

    base_key = f"{category}_{group}_{type_}".lower().replace(" ", "-")

    for m in measurements:
        if m.get(MEASUREMENT_COLUMN_MD) and m.get(UOM_COLUMN_MD):
            measurement = m[MEASUREMENT_COLUMN_MD]
            uom = m[UOM_COLUMN_MD]

            new_rows.append({
                CATEGORY_COLUMN_MD: category,
                GROUP_COLUMN_MD: group,
                SUB_GROUP_COLUMN_MD: sub_group,
                TYPE_COLUMN_MD: type_,
                MEASUREMENT_COLUMN_MD: measurement,
                UOM_COLUMN_MD: uom,
                EXERCISE_KEY_COLUMN_MD: base_key,
                EXERCISE_MEASUREMENT_KEY_COLUMN_MD: f"{base_key}_{measurement}_{uom}"
                    .lower()
                    .replace(" ", "-")
            })

    return new_rows

def append_new_master_data_rows(new_rows, df):
    
    if new_rows:
        new_rows_df = pd.DataFrame(new_rows)
        updated_master_data_df = pd.concat([df, new_rows_df], ignore_index=True)

    return updated_master_data_df

def master_data_export(df):
    data = df.fillna("").values.tolist()
    headers = df.columns.tolist()

    overwrite_sheet(
        headers=headers,
        data=data,
        sheet_key=SK_MAIN_DATA,
        tab_name=TB_MASTER_DATA
    )

def rows_to_remove(df, category, group, type_, measurements):
    filtered_df = df.copy()

    category = ensure_list(category)
    group = ensure_list(group)
    type_ = ensure_list(type_)
    measurements = ensure_list(measurements)

    # Apply filters only if values exist
    if category:
        filtered_df = filtered_df[filtered_df[CATEGORY_COLUMN_MD].isin(category)]

    if group:
        filtered_df = filtered_df[filtered_df[GROUP_COLUMN_MD].isin(group)]

    if type_:
        filtered_df = filtered_df[filtered_df[TYPE_COLUMN_MD].isin(type_)]

    if measurements:
        filtered_df = filtered_df[filtered_df[MEASUREMENT_COLUMN_MD].isin(measurements)]

    return filtered_df

def remove_master_data_rows(rows_to_remove, df):
    
    if not rows_to_remove.empty:
        updated_master_data_df = df.drop(rows_to_remove.index)
    else:
        updated_master_data_df = df.copy()

    return updated_master_data_df 
