# Libraries
import streamlit as st

# Modules
from services.data_layer.read_tabs import (
    get_master_df,
    get_exercise_df
)

from pages.modify_master_data import render_master_data_page
from pages.add_exercise_session import render_exercise_session_page
from pages.login_screen import render_login_page

# =========================
# AUTH GATE
# =========================
if not st.session_state.get("authenticated"):
    render_login_page()
    st.stop()

# ===============
# GET DATA
# ===============
master_data_df = get_master_df()
exercise_data_df = get_exercise_df()

# ===============
# TABS
# ===============
tab_exercise_session, tab_master_data = st.tabs([
    "🏋️ Exercise Session",
    "🧩 Master Data Manager"
])

# ===============
# EXERCISE SESSION
# ===============
with tab_exercise_session:

    st.title(f"🏋️ Add Exercise Session")

    render_exercise_session_page(master_data_df, exercise_data_df)

# ===============
# MASTER DATA TAB
# ===============
with tab_master_data:

    st.title("Master Data Manager")

    render_master_data_page(master_data_df)

