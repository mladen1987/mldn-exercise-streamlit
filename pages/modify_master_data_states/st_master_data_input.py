import streamlit as st

from services.data_layer.clear_caches import clear_master_data_cache

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

def render_master_data_input_state(master_data_df):

    # ===== MD_MAIN_STATE DEFINE - INPUT STATE =====
    if "md_main_state" not in st.session_state:
        st.session_state["md_main_state"] = "inpst_input"

    # ==== 1. INPUT STATE =====
    if st.session_state["md_main_state"] == "inpst_input":
        
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
                clear_master_data_cache()

                # Store success info
                st.session_state["md_rows_added"] = len(new_rows)

                # ===== MD_MAIN_STATE DEFINE - SUCCESS STATE =====
                st.session_state["md_main_state"] = "inpst_success"

                st.rerun()

    # ==== 2. SUCCESS STATE =====
    if st.session_state["md_main_state"] == "inpst_success":

        rows_added = st.session_state.get("md_rows_added", 0)

        st.success(
            f"✅ Successfully added {rows_added} exercise types and measurements!"
        )

        if st.button("Add More Master Data"):
            
            # ===== MD_MAIN_STATE DEFINE - INPUT STATE =====
            st.session_state["md_main_state"] = "inpst_input"
            st.session_state["md_rows_added"] = None

            st.rerun()
