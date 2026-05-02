# Libraries
import pandas as pd

# Functions
from services.google_sheets import get_sheet

# Variables
from config import SK_MAIN_DATA, TB_MASTER_DATA

# ===== READ MASTER DATA =====
def get_master_data():
    # Load Master Data from Google Sheets
    sheet = get_sheet(SK_MAIN_DATA, TB_MASTER_DATA)
    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    return df
