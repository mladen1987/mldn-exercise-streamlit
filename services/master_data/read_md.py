# Libraries
import pandas as pd

# Functions
from services.google_sheets import get_sheet

# Variables
from config import SK_MAIN_DATA, TB_MASTER_DATA


def get_master_data():
    # Load Master Data from Google Sheets
    sheet = get_sheet(SK_MAIN_DATA, TB_MASTER_DATA)
    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    return df

def get_unique_categories():
    df = get_master_data()

    if df.empty:
        return []

    categories = (
        df["category"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return sorted(categories)
