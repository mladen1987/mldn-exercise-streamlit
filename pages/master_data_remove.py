import streamlit as st    

from services.google_sheets import get_client

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

from config import SK_BACKUP_DATA, TB_MASTER_DATA


def render_master_data_remove_page(master_data_df):

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
            ["category",
             "group",
             "type",
             "measurement",
             "uom"
             ]
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

            st.success(f"✅ Successfully removed {len(df_rows_to_remove)} exercise types and measurements!")
            st.info(f"📁 Backup of original Master Data saved to sheet: {backup_name}")
