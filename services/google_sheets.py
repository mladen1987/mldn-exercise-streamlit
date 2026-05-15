# Libraries
import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# Variables
from config import SCOPES
# ===== GOOGLE SHEETS API =====
@st.cache_resource
def get_client():
    
    service_account_info = st.secrets["gcp_service_account"]
    
    creds = Credentials.from_service_account_info(
        service_account_info,
        scopes=SCOPES
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
