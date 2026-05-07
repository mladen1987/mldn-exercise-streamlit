import streamlit as st

from services.master_data.read_md import get_unique_groups

def render_gym_session_page(master_data_df):

    st.header("🏋️ Gym Session")

    # Get gym groups
    gym_groups = get_unique_groups(master_data_df, "Gym")

    st.subheader("Select Workout Group")

    # Render one button per group
    for group in gym_groups:

        if st.button(group):

            st.session_state["selected_gym_group"] = group
