# Libraries
import streamlit as st

# Modules
from services.master_data.read_md import (
    get_master_data,
)

from pages.master_data_input import render_master_data_input_page
from pages.master_data_remove import render_master_data_remove_page
from pages.restore_from_backup import render_restore_page
from pages.gym_session_add import render_gym_session_page

# ===============
# GET DATA
# ===============
master_data_df = get_master_data()

# ===============
# TABS
# ===============
tab_input, tab_remove, tab_restore, tab_gym_session = st.tabs([
    "➕ Add Exercise Type",
    "🗑️ Remove Exercise Type",
    "🔄 Restore from Backup",
    "🏋️ Add Gym Session"
])

# ===============
# MASTER DATA INPUT
# ===============
with tab_input:

    st.title("Add Exercise Type")

    render_master_data_input_page(master_data_df)

# ===============
# MASTER DATA REMOVE
# ===============
with tab_remove:

    st.title("Remove Exercise Type")

    render_master_data_remove_page(master_data_df)

# ===============
# RESTORE DATA FROM BACKUP
# ===============
with tab_restore:

    st.title("Restore Master Data")

    render_restore_page()

# ===============
# ADD GYM SESSION
# ===============
with tab_gym_session:

    st.title("Add Gym Session")

    render_gym_session_page(master_data_df)
