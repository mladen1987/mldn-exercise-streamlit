# Libraries
import streamlit as st

# Modules
from services.authenticate import logout

from services.data_layer.read_tabs import (
    get_master_df,
    get_exercise_df
)

from ui_pages.modify_master_data import render_master_data_page
from ui_pages.add_exercise_session import render_exercise_session_page
from ui_pages.login_screen import render_login_page

# =========================
# AUTH GATE
# =========================
if not st.session_state.get("authenticated"):
    render_login_page()
    st.stop()

# =========================
# LOGOUT SIDEBAR
# =========================
with st.sidebar:

    st.success("Authenticated")

    if st.button("Logout"):
        logout()
        st.rerun()

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

