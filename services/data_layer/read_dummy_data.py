import pandas as pd

def get_dummy_master_df():
    return pd.read_csv(
        "dummy_data/exercise_master_data.csv"
    )


def get_dummy_exercise_df():
    return pd.read_csv(
        "dummy_data/exercise_data.csv"
    )
