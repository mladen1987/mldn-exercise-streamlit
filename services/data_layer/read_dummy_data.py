from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

def get_dummy_master_df():
    path = BASE_DIR / "dummy_data" / "exercise_master_data.csv"
    return pd.read_csv(path)


def get_dummy_exercise_df():
    path = BASE_DIR / "dummy_data" / "exercise_data.csv"
    return pd.read_csv(path)