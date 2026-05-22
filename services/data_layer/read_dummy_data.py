import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # adjust if needed


def get_dummy_master_df():
    path = BASE_DIR / "dummy_data" / "exercise_master_data.csv"
    return pd.read_csv(path)


def get_dummy_exercise_df():
    path = BASE_DIR / "dummy_data" / "exercise_data.csv"
    return pd.read_csv(path)
