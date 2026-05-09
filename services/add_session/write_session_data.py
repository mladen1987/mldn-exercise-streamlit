import streamlit as st
import pandas as pd

from datetime import date

from config import (
    EXERCISE_KEY_COLUMN_MD,
    EXERCISE_MEASUREMENT_KEY_COLUMN_MD
)

def build_session_rows(type_rows):

    session_rows = []

    today = date.today().strftime("%Y-%m-%d")
    today_key = date.today().strftime("%Y%m%d")

    for row in type_rows:

        measurement_key = row[
            EXERCISE_MEASUREMENT_KEY_COLUMN_MD
        ]

        value = st.session_state.get(measurement_key)

        # Skip empty inputs
        if value in [None, ""]:
            continue

        exercise_key = row[
            EXERCISE_KEY_COLUMN_MD
        ]

        session_rows.append({

            "primary_key":
                f"{measurement_key}_{today_key}",

            "session_key":
                f"{exercise_key}_{today_key}",

            "exercise_key":
                exercise_key,

            "exercise_measurement_key":
                measurement_key,

            "date":
                today,

            "value":
                value
        })

    return session_rows

def build_session_preview_df(type_rows, session_rows):

    # Lookup entered values
    value_lookup = {
        row["exercise_measurement_key"]: row["value"]
        for row in session_rows
    }

    preview_data = []

    for row in type_rows:

        measurement_key = row[
            "exercise_measurement_key"
        ]

        if measurement_key not in value_lookup:
            continue

        preview_data.append({

            "type":
                row["type"],

            "measurement":
                f"{row['measurement']} ({row['uom']})",

            "value":
                value_lookup[measurement_key]
        })

    return pd.DataFrame(preview_data)
