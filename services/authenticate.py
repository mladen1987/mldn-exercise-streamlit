import streamlit as st
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password: str) -> bool:
    return hash_password(input_password) == st.secrets["authentication"]["app_password"]

def is_authenticated() -> bool:
    return st.session_state.get("authenticated", False)

def login_success():
    st.session_state["authenticated"] = True

def logout():
    st.session_state.clear()
