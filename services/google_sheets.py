# Libraries
import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# Variables
from config import SECRETS_PATH, SCOPES
# ===== GOOGLE SHEETS API =====
@st.cache_resource
def get_client(secrets_path=SECRETS_PATH):
    scope = SCOPES

    creds = Credentials.from_service_account_file(
        secrets_path,
        scopes=scope
    )
    client = gspread.authorize(creds)
    return client

# ===== GET SHEET =====
def get_sheet(sheet_key, tab_name):
    client = get_client()
    return client.open_by_key(sheet_key).worksheet(tab_name)

# ===== OVERWRITE SHEET =====
def overwrite_sheet(headers, data, sheet_key, tab_name):
    sheet = get_sheet(sheet_key, tab_name)
    sheet.resize(rows=len(data) + 1)
    sheet.clear()
    sheet.update([headers] + data)
