import pandas as pd
from turtle import st

# Modules
from services.google_sheets import (
    overwrite_sheet
)

# Variables
from config import SK_MAIN_DATA, TB_MASTER_DATA

def build_new_master_data_rows(category, group, type_, measurements):
    """
    Converts UI inputs into master_data rows.
    """

    new_rows = []

    base_key = f"{category}_{group}_{type_}".lower().replace(" ", "_")

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
                    .replace(" ", "_")
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
