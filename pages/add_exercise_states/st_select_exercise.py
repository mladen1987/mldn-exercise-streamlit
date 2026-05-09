import streamlit as st

from services.master_data.read_md import (
    get_unique_categories,
    get_unique_groups
)

from services.add_session.read_exercise_data import (
    get_latest_exercise_dates,
    get_recommended_group
)

def render_state_select_exercise(master_data_df, exercise_data_df):
    
    # ===== 1.1 SE - Select Category =====
    categories = get_unique_categories(master_data_df)

    selected_category = st.selectbox(
        label="Select Exercise Category",
        options=categories
    )

    # ==== 1.2 SE - Recommendation Logic =====
    latest_dates_df = get_latest_exercise_dates(
        exercise_data_df
    )
 
    recommended_group = get_recommended_group(
        latest_dates_df,
        master_data_df,
        category_value=selected_category
    )
 
    exercise_groups = get_unique_groups(
        master_data_df,
        selected_category
    )
 
    st.info(f"⭐ Recommended next {selected_category} workout")
    
     # ===== 1.3 SE - Render Buttons =====
    cols = st.columns(max(len(exercise_groups), 1))
    
    for col, group in zip(cols, exercise_groups):
         with col:
            
            label = group
            
            if group == recommended_group:
                 label = f"⭐ {group}"
            
            if st.button(label):
                
                # Store Selections
                st.session_state["selected_category"] = selected_category
                st.session_state["selected_group"] = group
                
                # ===== MAIN STATE DEFINE - EXERCISE DATA INPUT =====
                st.session_state["main_state"] = "exercise_data_input"
                st.rerun()
