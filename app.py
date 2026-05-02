# Libraries
import streamlit as st
import pandas as pd

# Functions
from services.master_data import get_master_data

st.title("📊 Exercise Tracker")

# Master Data
df = get_master_data()
st.subheader("Your Master Data")
st.dataframe(df)
