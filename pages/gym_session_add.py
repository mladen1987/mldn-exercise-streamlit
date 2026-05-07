import streamlit as st

from services.master_data.read_md import (
    get_master_data,
    get_unique_groups
)

from services.add_session.read_exercise_data import (
    get_exercise_data,
    get_latest_exercise_dates,
    get_recommended_group
)

from config import CATEGORY_GYM

def render_gym_session_page(master_data_df):

    # ===== Load Data =====
    exercise_data_df = get_exercise_data()

    master_data_df = get_master_data()

    latest_dates_df = get_latest_exercise_dates(
        exercise_data_df
    )

    recommended_group = get_recommended_group(
        latest_dates_df,
        master_data_df,
        category_value=CATEGORY_GYM
    )

    # ===== Gym Groups =====
    gym_groups = get_unique_groups(
        master_data_df,
        CATEGORY_GYM
    )

    st.info(f"⭐ Recommended next {CATEGORY_GYM} workout: {recommended_group}")

    # ===== Render Buttons =====
    cols = st.columns(len(gym_groups))

    for col, group in zip(cols, gym_groups):

        with col:

            label = group

            if group == recommended_group:
                label = f"⭐ {group}"

            if st.button(label):
                st.session_state["selected_gym_group"] = group
