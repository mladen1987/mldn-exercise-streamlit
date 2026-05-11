import pandas as pd
import streamlit as st

from datetime import datetime

from utils.data_source_helpers import extract_timestamp

from services.google_sheets import get_sheet

def list_backups(client, backup_sheet_key):
    spreadsheet = client.open_by_key(backup_sheet_key)
    worksheets = spreadsheet.worksheets()

    backup_items = []

    # Get Title and Timestamp for backup sheets
    for ws in worksheets:
        if ws.title.startswith("backup_"):
            try:
                raw_ts = extract_timestamp(ws.title)
                dt = datetime.strptime(raw_ts, "%Y%m%d_%H%M%S")

                backup_items.append((ws.title, dt))
            except:
                continue
    
    # Sort by Timestamp (newest first)
    backup_items.sort(key=lambda x: x[1], reverse=True)
    
    return {
        title: dt.strftime("%Y-%m-%d %H:%M:%S")
        for title, dt in backup_items
    }

@st.cache_data(ttl=1800)
def get_backup_data(tab_name, backup_sheet_key):
    
    # Load Master Data from Google Sheets
    sheet = get_sheet(backup_sheet_key, tab_name)
    
    values = sheet.get_all_values()
    headers = values[0]
    rows = values[1:]

    df = pd.DataFrame(rows, columns=headers)

    return df
