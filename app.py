# Libraries
import streamlit as st

# Modules
from services.master_data.read_md import get_unique_categories

# Data Input
categories = get_unique_categories()

category_options = categories + ["➕ Add New Category"]

selected_category = st.selectbox(
    "Select Category",
    category_options
)

if selected_category == "➕ Add New Category":
    new_category = st.text_input("Enter new category name")

    if new_category:
        new_category = new_category.strip()

        if new_category in categories:
            st.warning("Category already exists")
            category = None
        else:
            category = new_category
    else:
        category = None
