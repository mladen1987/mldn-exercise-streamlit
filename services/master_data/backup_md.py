def backup_master_data_to_sheet(client, backup_sheet_key, df, tab_name):
    from datetime import datetime

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

    return worksheet_name
