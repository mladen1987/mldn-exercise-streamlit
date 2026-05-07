import streamlit as st

from config import (
    # Column Names
    MEASUREMENT_COLUMN_MD,
    UOM_COLUMN_MD
)

def input_block_measurements(label="Measurements", state_key="measurements"):
    
    st.subheader(label)

    # Initialize session state
    if state_key not in st.session_state:
        st.session_state[state_key] = []

    # Add button
    if st.button("➕ Add Measurement"):
        st.session_state[state_key].append({
            MEASUREMENT_COLUMN_MD: "",
            UOM_COLUMN_MD: ""
        })

    # Render dynamic inputs
    for i, row in enumerate(st.session_state[state_key]):
        col1, col2 = st.columns(2)

        with col1:
            row[MEASUREMENT_COLUMN_MD] = st.text_input(
                f"Measurement {i+1}",
                value=row[MEASUREMENT_COLUMN_MD],
                key=f"{state_key}_m_{i}"
            )

        with col2:
            row[UOM_COLUMN_MD] = st.text_input(
                f"UOM {i+1}",
                value=row[UOM_COLUMN_MD],
                key=f"{state_key}_u_{i}"
            )

    return st.session_state[state_key]
