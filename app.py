import streamlit as st

st.title("🚀 My First Streamlit App")

st.write("Hello! This is a bare-bones demo.")

name = st.text_input("What's your name?")

if name:
    st.success(f"Nice to meet you, {name} 👋")
