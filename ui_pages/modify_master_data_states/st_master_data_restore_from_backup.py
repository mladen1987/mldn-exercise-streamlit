import streamlit as st


from services.google_sheets import (
    get_client,
    overwrite_sheet
)

from services.restore_backup import (
    list_backups,
    get_backup_data
)

from services.restore_backup_guest import (
    list_backups_guest_mode,
    get_backup_data_guest
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

def render_master_data_restore_from_backup_state():
    
    if st.session_state.get("guest_mode", False):
        backups = list_backups_guest_mode()
    else:
        backups = list_backups(get_client(), SK_BACKUP_DATA)

    selected_backup = st.selectbox(
        "Select Master Data",
        options=list(backups.keys()),
        format_func=lambda key: backups[key]
    )

    # Load backup (button OR auto-load)
    if st.button("Show Backup Data"):
        if st.session_state.get("guest_mode", False):
            backup_df = get_backup_data_guest(selected_backup)
        else:
            backup_df = get_backup_data(selected_backup, SK_BACKUP_DATA)

        st.session_state["selected_backup_df"] = backup_df

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

            # ===== GUEST MODE - EXTRA MESSAGE =====
            if st.session_state.get("guest_mode", False): # Return false if guest_mode not defined
                st.info("Guest mode enabled — session not saved.")

            st.success("✅ Master Data restored from backup")
