from services.data_layer.read_tabs import get_exercise_df
import streamlit as st
import pandas as pd

from services.add_session.write_session_data import build_session_preview_df
from services.add_session.write_exercise_data import write_session_to_sheet

from config import SK_MAIN_DATA, TB_MAIN_DATA

def render_state_preview():
    
    types = st.session_state.get("session_types")
    session_rows = st.session_state.get("session_rows")

    # Safety Check - No Session Data Found
    if not session_rows:
        st.warning("No session data found. Please go back.")
        st.stop()
    
    preview_df = build_session_preview_df(types, session_rows)
    
    st.subheader("📊 Session Preview")
    
    st.dataframe(preview_df)
    
    # Confirm the preview to submit
    confirmed = st.checkbox("✅ Confirm session data")
    
    if confirmed:
        # On Button Press
        if st.button("Submit Session Data"):
            try:
                # Write session data to Google Sheet
                write_session_to_sheet(SK_MAIN_DATA, TB_MAIN_DATA, pd.DataFrame(session_rows))
                
                # 🔥 invalidate cached data
                get_exercise_df.clear()
                
                # ===== MAIN STATE DEFINE - WRITE SUCCESS =====
                st.session_state["main_state"] = "write_success"
                st.rerun()
            except Exception as e:
                st.error(f"Error submitting session data: {e}")
