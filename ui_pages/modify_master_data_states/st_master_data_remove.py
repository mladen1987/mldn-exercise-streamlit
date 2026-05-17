import streamlit as st    

from services.google_sheets import get_client

from services.data_layer.clear_caches import clear_master_data_cache

from services.master_data.backup_md import backup_master_data_to_sheet

from services.master_data.read_md import (
    get_unique_categories,
    get_unique_groups,
    get_unique_types,
    get_unique_measurements
)

from services.master_data.write_md import (
    rows_to_remove,
    remove_master_data_rows,
    master_data_export
)

from utils.select_helpers import (
    select_or_all
)

from config import (
    SK_BACKUP_DATA,
    TB_MASTER_DATA,
    # Column Names
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD
)


def render_master_data_remove_state(master_data_df):

    # ===== MD_MAIN_STATE DEFINE - SELECT AND REMOVE STATE =====
    if "md_main_state" not in st.session_state:
        st.session_state["md_main_state"] = "rmvst_select_and_remove"

    # ==== 1. SELECT AND REMOVE STATE =====
    if st.session_state["md_main_state"] == "rmvst_select_and_remove":
    
        # ===== Select Category =====
        categories = get_unique_categories(master_data_df)

        selected_category = st.selectbox(
            label="Select Category",
            options=categories,
            key="md_remove_category"
        )

        # ===== Select Group =====
        if selected_category:
            groups = get_unique_groups(master_data_df, selected_category)

            selected_group = select_or_all(
                label="Select Group",
                options=groups,
                all_label="✅ Select All Groups",
                key = "md_remove_group"
            )

        else:
            selected_group = None
        
        # ===== Select Type =====
        if selected_group:
            types = get_unique_types(master_data_df, selected_category, selected_group)

            selected_type = select_or_all(
                label="Select Type",
                options=types,
                all_label="✅ Select All Types",
                key="md_remove_type"
            )

        else:
            selected_type = None

        # ===== Select Measurement =====
        if selected_type:
            measurements = get_unique_measurements(master_data_df, selected_category, selected_group, selected_type)
        
            selected_measurement = select_or_all(
                label="Select Measurement",
                options=measurements,
                all_label="✅ Select All Measurements",
                key="md_remove_measurement"
            )

        else:
            selected_measurement = None

        # ===== Data to Remove =====
        if selected_group:
            df_rows_to_remove = rows_to_remove(
                df=master_data_df,
                category=selected_category,
                group=selected_group,
                type_=selected_type,
                measurements=selected_measurement
            )

            st.write(f"To Remove: {len(df_rows_to_remove)}")
            st.dataframe(df_rows_to_remove[
                [CATEGORY_COLUMN_MD,
                GROUP_COLUMN_MD,
                TYPE_COLUMN_MD,
                MEASUREMENT_COLUMN_MD,
                UOM_COLUMN_MD]
            ])

            if st.button("Confirm Remove"):
                backup_name = backup_master_data_to_sheet(
                    client=get_client(),
                    backup_sheet_key=SK_BACKUP_DATA,
                    df=master_data_df,
                    tab_name=TB_MASTER_DATA
                )
                
                updated_master_data_df = remove_master_data_rows(df_rows_to_remove, master_data_df)
                
                master_data_export(updated_master_data_df)

                # 🔥 invalidate cached data
                clear_master_data_cache()

                # Store success info
                st.session_state["removed_rows_count"] = len(df_rows_to_remove)
                st.session_state["backup_name"] = backup_name

                # ===== MD_MAIN_STATE DEFINE - SUCCESS STATE =====
                st.session_state["md_main_state"] = "rmvst_success_state"

    # ===== 2. SUCCESS STATE =====
    if st.session_state["md_main_state"] == "rmvst_success_state":

        rows_removed = st.session_state.get("removed_rows_count", 0)
        backup_name = st.session_state.get("backup_name", "Unknown")

        # ===== GUEST MODE - EXTRA MESSAGE =====
        if st.session_state.get("guest_mode", False): # Return false if guest_mode not defined
            st.info("Guest mode enabled — session not saved.")

        st.success(
            f"✅ Successfully removed {rows_removed} rows!"
        )

        st.info(
            f"📁 Backup saved to sheet: {backup_name}"
        )
        
        if st.button("Remove More Master Data"):

            st.session_state["md_main_state"] = "rmvst_select_and_remove"
            st.session_state["removed_rows_count"] = None
            st.session_state["backup_name"] = None
            
            # Clear selections
            st.session_state["md_remove_category"] = None
            st.session_state["md_remove_group"] = None
            st.session_state["md_remove_type"] = None
            st.session_state["md_remove_measurement"] = None

            st.rerun()
