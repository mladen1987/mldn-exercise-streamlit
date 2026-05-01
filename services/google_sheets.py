import gspread
from google.oauth2.service_account import Credentials

def get_client(secrets_path="secrets.json"):
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "secrets/secrets.json",
        scopes=scope
    )
    client = gspread.authorize(creds)
    return client


def get_sheet():
    client = get_client()
    return client.open("exercise-data").open("exercise-data")
