import streamlit as st
import pandas as pd
from datetime import datetime

from utils.visualize_helpers import render_spark_bar

from services.add_session.read_session_data import (
    get_types_for_group,
    group_measurements_by_type,
    get_recent_measurement_history
)

from services.add_session.write_session_data import build_session_rows

def render_state_exercise_data_input(master_data_df, exercise_data_df):

    # ===== TIMER STATE =====
    if "timer_running" not in st.session_state:
        st.session_state["timer_running"] = False

    if "timer_start" not in st.session_state:
        st.session_state["timer_start"] = None
    
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
 
    historical_data_df = get_recent_measurement_history(
            master_data_df,
            exercise_data_df,
            st.session_state.get("selected_category"),
            st.session_state.get("selected_group"),
            5
    )

    # ===== STOPWATCH STATE LOGIC =====
    st.divider()
    st.subheader("⏱ Stopwatch")

    col1, col2, col3 = st.columns([1,1,2])

    with col1:
        if st.button("▶ Start"):

            st.session_state["timer_running"] = True
            st.session_state["timer_start"] = datetime.now()

            st.rerun()

    with col2:
        if st.button("🔄 Reset"):

            st.session_state["timer_running"] = False
            st.session_state["timer_start"] = None

            st.rerun()

    # ===== STOPWATCH VISUALIZE =====
    if (
        st.session_state["timer_running"]
        and st.session_state["timer_start"] is not None
    ):

        elapsed = datetime.now() - st.session_state["timer_start"]

        total_seconds = int(elapsed.total_seconds())

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        st.success(f"⏱ {minutes:02}:{seconds:02}")

    else:
        st.info("Timer not running")
    
    # Render all measurements for each type together under an expander
    for (sub_group, type_name), measurements in grouped_types.items():
    
        with st.expander(f"{sub_group} · {type_name}"):

            for m in measurements:

                label = f"{m['measurement']} ({m['uom']})"

                measurement_history = historical_data_df[
                    (historical_data_df["type"] == type_name)
                    & (historical_data_df["measurement"] == m["measurement"])
                ].sort_values("date", ascending=False)

                if not measurement_history.empty:

                    values = measurement_history["value"].astype(float).tolist()
                    bars = render_spark_bar(values)

                    for (_, row), bar in zip(measurement_history.iterrows(), bars):

                        date_str = pd.to_datetime(row["date"]).strftime("%Y-%m-%d")

                        st.caption(
                            f"{date_str}: "
                            f"{row['value']} {row['uom']}  "
                            f"{bar}"
                        )

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
