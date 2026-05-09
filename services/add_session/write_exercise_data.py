from services.google_sheets import get_sheet

def write_session_to_sheet(sheet_key, tab_name, df):
    sheet = get_sheet(sheet_key, tab_name)

    sheet.append_rows(df.values.tolist())
