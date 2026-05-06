import pandas as pd
from turtle import st

# Modules
from services.google_sheets import (
    overwrite_sheet
)

from utils.data_type_helpers import ensure_list

# Variables
from config import SK_MAIN_DATA, TB_MASTER_DATA

def build_new_master_data_rows(category, group, type_, measurements):
    new_rows = []

    base_key = f"{category}_{group}_{type_}".lower().replace(" ", "-")

    for m in measurements:
        if m.get("measurement") and m.get("uom"):
            measurement = m["measurement"]
            uom = m["uom"]

            new_rows.append({
                "category": category,
                "group": group,
                "type": type_,
                "measurement": measurement,
                "uom": uom,
                "exercise_key": base_key,
                "exercise_measurement_key": f"{base_key}_{measurement}_{uom}"
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
        filtered_df = filtered_df[filtered_df["category"].isin(category)]

    if group:
        filtered_df = filtered_df[filtered_df["group"].isin(group)]

    if type_:
        filtered_df = filtered_df[filtered_df["type"].isin(type_)]

    if measurements:
        filtered_df = filtered_df[filtered_df["measurement"].isin(measurements)]

    return filtered_df

def remove_master_data_rows(rows_to_remove, df):
    
    if not rows_to_remove.empty:
        updated_master_data_df = df.drop(rows_to_remove.index)
    else:
        updated_master_data_df = df.copy()

    return updated_master_data_df 
