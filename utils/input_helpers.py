import streamlit as st

def input_block_measurements(label="Measurements", state_key="measurements"):
    
    st.subheader(label)

    # Initialize session state
    if state_key not in st.session_state:
        st.session_state[state_key] = []

    # Add button
    if st.button("➕ Add Measurement"):
        st.session_state[state_key].append({
            "measurement": "",
            "uom": ""
        })

    # Render dynamic inputs
    for i, row in enumerate(st.session_state[state_key]):
        col1, col2 = st.columns(2)

        with col1:
            row["measurement"] = st.text_input(
                f"Measurement {i+1}",
                value=row["measurement"],
                key=f"{state_key}_m_{i}"
            )

        with col2:
            row["uom"] = st.text_input(
                f"UOM {i+1}",
                value=row["uom"],
                key=f"{state_key}_u_{i}"
            )

    return st.session_state[state_key]
