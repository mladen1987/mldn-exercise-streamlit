import streamlit as st, hashlib, time

from config import MAX_ATTEMPTS, LOCKOUT_SECONDS

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

def handle_login(input_password: str):
    now = time.time()

    # initialize state
    if "login_attempts" not in st.session_state:
        st.session_state["login_attempts"] = 0

    if "lock_until" not in st.session_state:
        st.session_state["lock_until"] = 0

    # check lockout - if lock_until is 0 this returns false
    if now < st.session_state["lock_until"]:
        remaining = int(st.session_state["lock_until"] - now)
        st.error(f"Too many attempts. Try again in {remaining}s")
        return

    # validate password
    if check_password(input_password):
        st.session_state["authenticated"] = True
        st.session_state["login_attempts"] = 0
        st.session_state["lock_until"] = 0
        st.rerun()

    # wrong password
    st.session_state["login_attempts"] += 1

    remaining_attempts = MAX_ATTEMPTS - st.session_state["login_attempts"]

    if remaining_attempts > 0:
        st.error(f"Wrong password. {remaining_attempts} attempts left.")
    else:
        st.session_state["lock_until"] = now + LOCKOUT_SECONDS
        st.session_state["login_attempts"] = 0
        st.error(f"Too many attempts. Locked for {LOCKOUT_SECONDS}s")
