import streamlit as st

from services.data_layer.read_tabs import (
    get_all_tabs_raw,
    get_master_df
)

from services.master_data.read_md import (
    get_unique_categories,
    get_unique_groups,
    get_unique_types,
)

from services.master_data.write_md import (
    build_new_master_data_rows,
    append_new_master_data_rows,
    master_data_export
)

from utils.select_helpers import (
    select_or_create,
)

from utils.input_helpers import (
    input_block_measurements,
)

def render_master_data_input_page(master_data_df):

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
            
            # 🔥 invalidate cached data
            get_master_df.clear()
            get_all_tabs_raw.clear()
            
            st.success(f"✅ Successfully added {len(new_rows)} exercise types and measurements!")

            st.rerun()
