import pandas as pd
import streamlit as st

from ui_pages.add_exercise_states.st_select_exercise import render_state_select_exercise
from ui_pages.add_exercise_states.st_exercise_data_input import render_state_exercise_data_input
from ui_pages.add_exercise_states.st_preview import render_state_preview

from config import SK_MAIN_DATA, TB_MAIN_DATA

HIDE_BACK_BUTTON_STATES = {"select_exercise", "write_success"}

def reset_exercise_flow():
    st.session_state["main_state"] = "select_exercise"
    st.session_state["selected_category"] = None
    st.session_state["selected_group"] = None
    st.session_state["selected_exercise"] = None

def render_exercise_session_page(master_data_df, exercise_data_df):

    # ===== MAIN STATE DEFINE - SELECT EXERCISE =====
    if "main_state" not in st.session_state:
        st.session_state["main_state"] = "select_exercise"

    # ==== 1. SELECT EXERCISE STATE =====
    if st.session_state["main_state"] == "select_exercise":

        render_state_select_exercise(master_data_df, exercise_data_df)

    # ==== 2. EXERCISE DATA INPUT STATE =====
    if st.session_state.get("main_state") == "exercise_data_input":

        render_state_exercise_data_input(master_data_df, exercise_data_df)

    
    # ==== 3. PREVIEW OUTPUT STATE =====
    if st.session_state.get("main_state") == "preview_output":
        
        render_state_preview()
    

    # ==== 4. WRITE SUCCESS STATE =====
    if st.session_state.get("main_state") == "write_success":
    
        st.session_state["session_types"] = None
        st.session_state["session_rows"] = None

        st.success("Session successfully written 🚀")

        # ===== GUEST MODE - EXTRA MESSAGE =====
        if st.session_state.get("guest_mode", False): # Return false if guest_mode not defined
            st.info("Guest mode enabled — session not saved.")
    
        if st.button("Add Another Session"):
            
            reset_exercise_flow()
            st.rerun()

    # =====================================================
    # GLOBAL BACK BUTTON - ANY STATE APART FROM SELECT EXERCISE
    # =====================================================
    if st.session_state.get("main_state") not in HIDE_BACK_BUTTON_STATES:

        st.divider()

        if st.button("⬅ Back"):

            reset_exercise_flow()
            st.rerun()
