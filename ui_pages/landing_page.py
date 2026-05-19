import streamlit as st

from utils.visualizations import (
    render_contribution_heatmap
)

def render_landing_page(exercise_data_df):

    st.caption(
        "Exercise sessions over the last year."
    )

    render_contribution_heatmap(exercise_data_df)
