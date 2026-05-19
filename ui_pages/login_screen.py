import streamlit as st
from services.authenticate import handle_login


def render_login_page():

    password = st.text_input("Enter password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            handle_login(password)

    with col2:
        if st.button("Continue as Guest"):
            st.session_state["authenticated"] = True
            st.session_state["guest_mode"] = True
            st.rerun()
