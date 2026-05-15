import streamlit as st
from services.authenticate import check_password, login_success


def render_login_page():

    st.title("🔐 Login")

    password = st.text_input("Enter password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if check_password(password):
                login_success()
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Incorrect password")

    with col2:
        if st.button("Continue as Guest"):
            st.session_state["authenticated"] = True
            st.session_state["guest_mode"] = True
            st.rerun()
