import streamlit as st
import pandas as pd
from services.google_sheets import get_sheet

st.title("📊 Exercise Tracker")

# Load data
sheet = get_sheet()
data = sheet.get_all_records()

# Convert to DataFrame
df = pd.DataFrame(data)

# Display
st.subheader("Your Data")
st.dataframe(df)
