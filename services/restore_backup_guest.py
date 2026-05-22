import os
import pandas as pd
from datetime import datetime
from pathlib import Path

def list_backups_guest_mode(client=None, backup_sheet_key=None):

    backup_dir = Path(__file__).resolve().parent.parent / "dummy_data"
        
    files = [
        f.name for f in backup_dir.glob("backup_exercise_master_data_*.csv")
    ]

    backup_items = []

    for f in files:
        try:
            raw_ts = f.replace("backup_exercise_master_data_", "").replace(".csv", "")
            dt = datetime.strptime(raw_ts, "%Y%m%d_%H%M%S")
            backup_items.append((f, dt))
        except:
            continue

    backup_items.sort(key=lambda x: x[1], reverse=True)

    return {
        title: dt.strftime("%Y-%m-%d %H:%M:%S")
        for title, dt in backup_items
    }

def get_backup_data_guest(tab_name, backup_sheet_key=None):

    # remove .csv if it exists
    base_name = tab_name.replace(".csv", "")
    
    # Map tab_name → CSV file
    file_path = f"dummy_data/{base_name}.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing dummy backup file: {file_path}")

    return pd.read_csv(file_path)
