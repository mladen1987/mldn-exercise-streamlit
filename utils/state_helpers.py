import streamlit as st

def reset_exercise_flow():
    st.session_state["main_state"] = "data_input"
    st.session_state["selected_category"] = None
    st.session_state["selected_exercise_group"] = None
    