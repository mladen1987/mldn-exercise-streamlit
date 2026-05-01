import gspread
from google.oauth2.service_account import Credentials
from config import SECRETS_PATH, SCOPES, SHEET_KEY, TAB_NAME

# Google Sheets API client setup
def get_client(secrets_path=SECRETS_PATH):
    scope = SCOPES

    creds = Credentials.from_service_account_file(
        secrets_path,
        scopes=scope
    )
    client = gspread.authorize(creds)
    return client

# Get data from a specific sheet
def get_sheet():
    client = get_client()
    return client.open_by_key(SHEET_KEY).worksheet(TAB_NAME)
