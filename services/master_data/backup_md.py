import streamlit as st

from datetime import datetime

from utils.data_source_helpers import extract_timestamp

def cleanup_old_backups(backup_spreadsheet, keep_last_n=5):
    
    worksheets = backup_spreadsheet.worksheets()

    # Keep only backup sheets
    backup_sheets = [
        ws for ws in worksheets if ws.title.startswith("backup_")
    ]

    # Sort by timestamp (newest first)
    backup_sheets_sorted = sorted(
        backup_sheets,
        key=lambda ws: extract_timestamp(ws.title),
        reverse=True
    )

    # Identify sheets to delete
    sheets_to_delete = backup_sheets_sorted[keep_last_n:]

    # Delete oldest
    for ws in sheets_to_delete:
        backup_spreadsheet.del_worksheet(ws)

def backup_master_data_to_sheet(client, backup_sheet_key, df, tab_name):
    
    # ===== GUEST MODE GUARD =====
    if st.session_state.get("guest_mode", False):
        st.info("Guest mode enabled — backup skipped.")
        return None

    # Open backup spreadsheet
    backup_spreadsheet = client.open_by_key(backup_sheet_key)

    # Create timestamped worksheet name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    worksheet_name = f"backup_{tab_name}_{timestamp}"

    # Create worksheet
    worksheet = backup_spreadsheet.add_worksheet(
        title=worksheet_name,
        rows=str(len(df) + 10),
        cols=str(len(df.columns) + 5)
    )

    # Prepare data
    data = df.fillna("").values.tolist()
    headers = df.columns.tolist()

    # Write data
    worksheet.update([headers] + data)

    # Limit number of backups
    cleanup_old_backups(backup_spreadsheet, keep_last_n=5)
    
    return worksheet_name
