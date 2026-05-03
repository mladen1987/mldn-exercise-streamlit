import streamlit as st

def select_or_create(
    label,
    options,
    new_label="➕ Add New",
):

    options_with_new = [new_label] + options

    selection = st.selectbox(label, options_with_new)

    if selection == new_label:
        new_value = st.text_input(f"Enter new {label.lower()}")

        if new_value:
            new_value = new_value.strip()

            if new_value in options:
                st.warning(f"{label} already exists")
                return None

            return new_value

        return None

    return selection

def select_or_all(
    label,
    options,
    all_label="✅ Select All",
):
    """
    Multi-select with 'Select All' option.
    Returns a list of selected values.
    """

    options_with_all = [all_label] + options

    selection = st.multiselect(
        label,
        options_with_all
    )

    # If user selects "Select All"
    if all_label in selection:
        return options

    return selection
