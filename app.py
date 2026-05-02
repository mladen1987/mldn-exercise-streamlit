import streamlit as st
import pandas as pd
from services.google_sheets import get_sheet

from config import SK_MAIN_DATA, TB_MASTER_DATA

st.title("📊 Exercise Tracker")

# Load data
sheet = get_sheet(SK_MAIN_DATA, TB_MASTER_DATA)
data = sheet.get_all_records()

# Convert to DataFrame
df = pd.DataFrame(data)

# Display
st.subheader("Your Data")
st.dataframe(df)
