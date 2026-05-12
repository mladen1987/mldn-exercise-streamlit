import streamlit as st
import pandas as pd

from services.google_sheets import get_client
from config import SK_MAIN_DATA, TB_MASTER_DATA, TB_MAIN_DATA


@st.cache_data(ttl=300)
def get_all_tabs_raw():
    client = get_client()
    sheet = client.open_by_key(SK_MAIN_DATA)

    return {
        "master": sheet.worksheet(TB_MASTER_DATA).get_all_values(),
        "exercise": sheet.worksheet(TB_MAIN_DATA).get_all_values()
    }


def parse_tab(values):
    headers = values[0]
    rows = values[1:]
    return pd.DataFrame(rows, columns=headers)


@st.cache_data(ttl=300)
def get_master_df():
    data = get_all_tabs_raw()["master"]
    return parse_tab(data)


@st.cache_data(ttl=300)
def get_exercise_df():
    data = get_all_tabs_raw()["exercise"]
    return parse_tab(data)
