# Libraries
import streamlit as st

# Modules
from services.authenticate import logout

from services.data_layer.read_tabs import (
    get_master_df,
    get_exercise_df
)

from ui_pages.landing_page import render_landing_page
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
## For Guests, the app loads dummy csv files
if st.session_state.get("guest_mode"):

    from services.data_layer.read_dummy_data import (
        get_dummy_master_df,
        get_dummy_exercise_df
    )

    master_data_df = get_dummy_master_df()
    exercise_data_df = get_dummy_exercise_df()

else:
## For the user loads Google Sheets
    from services.data_layer.read_tabs import (
        get_master_df,
        get_exercise_df
    )

    master_data_df = get_master_df()
    exercise_data_df = get_exercise_df()

# ===============
# TABS
# ===============
tab_landing_page, tab_exercise_session, tab_master_data = st.tabs([
    "🏠 Home",
    "🏋️ Exercise Session",
    "🧩 Master Data Manager"
])

# ===============
# DASHBOARD TAB
# ===============
with tab_landing_page:

    st.title(f"🏠 Home")

    render_landing_page(exercise_data_df)

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

