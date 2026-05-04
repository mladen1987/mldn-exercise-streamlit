def render_master_data_remove_page(master_data_df):
    
    import streamlit as st

    from services.master_data.modify_md import (
        get_unique_categories,
        get_unique_groups,
        get_unique_types,
        get_unique_measurements
    )

    from utils.select_helpers import (
        select_or_all
    )

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
