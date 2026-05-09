import streamlit as st

from services.master_data.read_md import (
    get_unique_categories,
    get_unique_groups
)

from services.add_session.read_exercise_data import (
    get_latest_exercise_dates,
    get_recommended_group
)

from services.add_session.read_session_data import (
    get_types_for_group,
    group_measurements_by_type
)

def render_exercise_session_page(master_data_df, exercise_data_df):

    # ===== Select Category =====
    categories = get_unique_categories(master_data_df)

    selected_category = st.selectbox(
        label="Select Exercise Category",
        options=categories
    )

    # ===== Reset Group When Category Changes =====
    if (
        "previous_category" not in st.session_state
        or st.session_state["previous_category"] != selected_category
    ):

        st.session_state["selected_exercise_group"] = None
        st.session_state["previous_category"] = selected_category

    latest_dates_df = get_latest_exercise_dates(
        exercise_data_df
    )

    recommended_group = get_recommended_group(
        latest_dates_df,
        master_data_df,
        category_value=selected_category
    )

    # ===== Exercise Groups =====
    exercise_groups = get_unique_groups(
        master_data_df,
        selected_category
    )

    st.info(f"⭐ Recommended next {selected_category} workout: {recommended_group}")

    # ===== Render Buttons =====
    cols = st.columns(max(len(exercise_groups), 1))

    for col, group in zip(cols, exercise_groups):

        with col:

            label = group

            if group == recommended_group:
                label = f"⭐ {group}"

            if st.button(label):
                st.session_state["selected_exercise_group"] = group

    # ===== Display Exercise Types for Selected Group =====
    if st.session_state.get("selected_exercise_group"):

        types = get_types_for_group(
            master_data_df,
            selected_category,
            st.session_state["selected_exercise_group"]
        )

        # ===== Group Measurements by Type =====
        # Display all measurements for each type together under an expander
        grouped_types = group_measurements_by_type(types)

        for type_name, measurements in grouped_types.items():

            with st.expander(type_name):
            
                for measurement in measurements:

                    label = (
                        f"{measurement['measurement']} "
                        f"({measurement['uom']})"
                    )

                    st.number_input(
                        label,
                        key=measurement["exercise_measurement_key"],
                        placeholder="Enter value",
                    )
