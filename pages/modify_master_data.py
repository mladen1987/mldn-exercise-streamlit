import streamlit as st

from pages.modify_master_data_states.st_master_data_input import render_master_data_input_state
from pages.modify_master_data_states.st_master_data_remove import render_master_data_remove_state
from pages.modify_master_data_states.st_master_data_restore_from_backup import render_master_data_restore_from_backup_state

def render_master_data_page(master_data_df):

    # ===== MD MAIN STATE SET - DEFAULT =====
    if "md_main_state" not in st.session_state:
        st.session_state["md_main_state"] = "default"

    # ===== 1. DEFAULT STATE =====
    if st.session_state["md_main_state"] == "default":
        col1, col2, col3 = st.columns(3)

        with col1:
            # ===== MD MAIN STATE SET - INPUT STATE - INPUT =====
            st.markdown("#### ➕ Create")
            if st.button("Add Exercise Types", use_container_width=True):
                st.session_state["md_main_state"] = "inpst_input"
                st.rerun()
                st.rerun()

        with col2:
            # ===== MD MAIN STATE SET - REMOVE STATE - SELECT AND REMOVE =====
            st.markdown("#### 🗑 Delete")
            if st.button("Remove Exercise Types", use_container_width=True):
                st.session_state["md_main_state"] = "rmvst_select_and_remove"
                st.rerun()

        with col3:
            # ===== MD MAIN STATE SET - RESTORE FROM BACKUP STATE =====
            st.markdown("#### ♻️ Recover")
            if st.button("Restore Older Version", use_container_width=True):
                st.session_state["md_main_state"] = "bckp_state"
                st.rerun()

    # ===== 1. INPUT STATE =====
    elif st.session_state["md_main_state"].startswith("inpst"):

        render_master_data_input_state(master_data_df)

        st.divider()
        
        # ===== MD MAIN STATE SET - DEFAULT =====
        if st.button("⬅ Back"):
            st.session_state["md_main_state"] = "default"
            st.rerun()

    # ===== 2. REMOVE STATE =====
    elif st.session_state["md_main_state"].startswith("rmvst"):

        render_master_data_remove_state(master_data_df)

        st.divider()

        # ===== MD MAIN STATE SET - DEFAULT =====
        if st.button("⬅ Back"):
            st.session_state["md_main_state"] = "default"
            st.rerun()

    # ===== 3. RESTORE STATE =====
    elif st.session_state["md_main_state"].startswith("bckp"):

        render_master_data_restore_from_backup_state()

        st.divider()

        # ===== MD MAIN STATE SET - DEFAULT =====
        if st.button("⬅ Back"):
            st.session_state["md_main_state"] = "default"
            st.rerun()
