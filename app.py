# Libraries
import streamlit as st

# Modules
from services.master_data.read_md import (
    get_master_data,
)

from services.master_data.modify_md import (
    get_unique_categories,
    get_unique_groups,
    get_unique_types,
    get_unique_measurements
)

from services.master_data.write_md import (
    build_new_master_data_rows,
    append_new_master_data_rows,
    master_data_export
)

from utils.select_helpers import (
    select_or_create,
    select_or_all
)

from utils.input_helpers import (
    input_block_measurements,
)

# ===============
# GET DATA
# ===============
master_data_df = get_master_data()

# ===============
# TABS
# ===============
tab_input, tab_remove = st.tabs([
    "➕ Add Exercise Type",
    "🗑️ Remove Exercise Type"
])

# ===============
# MASTER DATA INPUT
# ===============
with tab_input:

    # ===== Select Category =====
    categories = get_unique_categories(master_data_df)

    selected_category = select_or_create(
        label="Select or Create Category",
        options=categories,
        new_label="➕ Add New Category"
    )

    # ===== Select Group =====
    if selected_category:

        groups = get_unique_groups(master_data_df, selected_category)

        selected_group = select_or_create(
            label="Select or Create Group",
            options=groups,
            new_label="➕ Add New Group"
        )

    else:
        selected_group = None

    # ===== Select Type =====
    if selected_group:
        types = get_unique_types(master_data_df, selected_category, selected_group)

        selected_type = select_or_create(
            label="Select or Create Type",
            options=types,
            new_label="➕ Add New Type"
        )

    else:
        selected_type = None

    # ===== Add Measurement =====
    if selected_type:
        measurements = input_block_measurements()

    else:
        measurements = None

    # ===== Submit New Values =====
    if selected_category and selected_group and selected_type and measurements:
        # Write to master data
        if st.button("Submit"):
            new_rows = build_new_master_data_rows(
                selected_category,
                selected_group,
                selected_type,
                measurements
            )

            master_data_df = append_new_master_data_rows(new_rows, master_data_df)

            master_data_export(master_data_df)

            st.success(f"✅ Successfully added {len(new_rows)} exercise types and measurements!")

# ===============
# MASTER DATA REMOVE
# ===============
with tab_remove:
    
    # ===== Select Category =====
    categories = get_unique_categories(master_data_df)

    selected_category = st.selectbox(
        label="Select Category",
        options=categories
    )

    # ===== Select Group =====
    if selected_category:
        groups = get_unique_groups(master_data_df, selected_category)

        selected_group = select_or_all(
            label="Select Group",
            options=groups,
            all_label="✅ Select All Groups"
        )

    else:
        selected_group = None
    
    # ===== Select Type =====
    if selected_group:
        types = get_unique_types(master_data_df, selected_category, selected_group)

        selected_type = select_or_all(
            label="Select Type",
            options=types,
            all_label="✅ Select All Types"
        )

    else:
        selected_type = None

    # ===== Select Measurement =====
    if selected_type:
        measurements = get_unique_measurements(master_data_df, selected_category, selected_group, selected_type)
    
        selected_measurement = select_or_all(
            label="Select Measurement",
            options=measurements,
            all_label="✅ Select All Measurements"
        )

    else:
        measurements = None
