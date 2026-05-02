# Libraries
import gspread
from google.oauth2.service_account import Credentials

# Variables
from config import SECRETS_PATH, SCOPES

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
def get_sheet(sheet_key, tab_name):
    client = get_client()
    return client.open_by_key(sheet_key).worksheet(tab_name)
