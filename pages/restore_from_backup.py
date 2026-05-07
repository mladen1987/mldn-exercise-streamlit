import streamlit as st

from services.google_sheets import (
    get_client,
    overwrite_sheet
)

from services.restore_backup import (
    list_backups,
    get_backup_data
)

from config import (
    SK_BACKUP_DATA,
    SK_MAIN_DATA,
    TB_MASTER_DATA,
    # Column Names
    CATEGORY_COLUMN_MD,
    GROUP_COLUMN_MD,
    TYPE_COLUMN_MD,
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD
)

def render_restore_page():
    backups = list_backups(get_client(), SK_BACKUP_DATA)

    selected_backup = st.selectbox(
        "Select Master Data",
        options=list(backups.keys()),
        format_func=lambda key: backups[key]
    )

    # Load backup (button OR auto-load)
    if st.button("Show Backup Data"):
        st.session_state["selected_backup_df"] = get_backup_data(
            selected_backup,
            SK_BACKUP_DATA
        )

    # Display if loaded
    if "selected_backup_df" in st.session_state:

        backup_df = st.session_state["selected_backup_df"]

        st.subheader("Preview Backup Data")

        st.dataframe(backup_df[
            [CATEGORY_COLUMN_MD, GROUP_COLUMN_MD, TYPE_COLUMN_MD, MEASUREMENT_COLUMN_MD, UOM_COLUMN_MD]
        ])

        # Restore section
        st.warning("⚠️ This will overwrite current Master Data")

        confirm = st.checkbox("I understand and want to restore this backup")

        if confirm and st.button("♻️ Restore Backup"):

            overwrite_sheet(
                headers=backup_df.columns.tolist(),
                data=backup_df.values.tolist(),
                sheet_key=SK_MAIN_DATA,
                tab_name=TB_MASTER_DATA
            )

            st.success("✅ Master Data restored from backup")
