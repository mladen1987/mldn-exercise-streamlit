import streamlit as st

from utils.visualizations import (
    render_contribution_heatmap,
    render_progress_charts
)

def render_landing_page(master_data_df, exercise_data_df):

    render_contribution_heatmap(exercise_data_df)

    render_progress_charts(master_data_df, exercise_data_df)
