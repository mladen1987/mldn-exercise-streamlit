from services.data_layer.read_tabs import (
    get_master_df,
    get_exercise_df,
    get_all_tabs_raw
)

def clear_master_data_cache():
    get_master_df.clear()
    get_all_tabs_raw.clear()


def clear_exercise_data_cache():
    get_exercise_df.clear()
    get_all_tabs_raw.clear()


def clear_all_data_cache():
    get_master_df.clear()
    get_exercise_df.clear()
    get_all_tabs_raw.clear()
    