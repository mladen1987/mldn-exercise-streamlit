import streamlit as st

from services.add_session.read_session_data import (
    get_types_for_group,
    group_measurements_by_type
)

from services.add_session.write_session_data import build_session_rows

def render_state_exercise_data_input(master_data_df):
    
    # No Selections Made - Safety Check
    if not st.session_state.get("selected_group") or not st.session_state.get("selected_category"):
        st.warning("Missing selections. Please go back.")
        st.stop()
 
    # Get types for selected category and group
    types = get_types_for_group(
        master_data_df,
        st.session_state.get("selected_category"),
        st.session_state.get("selected_group")
    )
 
    # Group all measruements by type for rendering
    grouped_types = group_measurements_by_type(types)
 
    st.subheader(
        f"{st.session_state.get('selected_category')} - "
        f"{st.session_state.get('selected_group')}"
    )
 
    # Render all measurements for each type together under an expander
    for type_name, measurements in grouped_types.items():
        
        with st.expander(type_name):
            
            for m in measurements:
                
                label = f"{m['measurement']} ({m['uom']})"
                
                # Take a number input for each measurement
                st.number_input(
                    label=label,
                    key=m["exercise_measurement_key"]
                )
 
    if st.button("End Session"):
        session_rows = build_session_rows(types)
        
        st.session_state["session_types"] = types
        st.session_state["session_rows"] = session_rows
        
        # ===== MAIN STATE DEFINE - PREVIEW OUTPUT =====
        st.session_state["main_state"] = "preview_output"
        
        st.rerun()
