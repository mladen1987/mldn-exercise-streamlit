# ===== Google Sheets =====
SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

# ===== SHEET INFO =====
# Sheet Key
SK_MAIN_DATA = "14PK-dHt-rGaxKuO2TabNJIN8HPMONzRyFg0ANtg8fB8"
SK_BACKUP_DATA = "1wBGpo6nj2cnbXLfW_n5fdJu4qe4g9VLTXDSFsTGi9Yk"

# Tab Containing Main Data
TB_MAIN_DATA = "exercise_data"
# Tab Containing Master Data
TB_MASTER_DATA = "exercise_master_data"


# ===== COLUMN NAMES =====
PK_COLUMN = "primary_key"
SESSION_KEY_COLUMN = "session_key"
EXERCISE_KEY_COLUMN = "exercise_key"
EXERCISE_MEASUREMENT_KEY_COLUMN = "exercise_measurement_key"
DATE_COLUMN = "date"
VALUE_COLUMN = "value"

# ===== MASTER DATA COLUMN =====
CATEGORY_COLUMN_MD = "category"
GROUP_COLUMN_MD = "group"
TYPE_COLUMN_MD = "type"
MEASUREMENT_COLUMN_MD = "measurement"
UOM_COLUMN_MD = "uom"
EXERCISE_KEY_COLUMN_MD = "exercise_key"
EXERCISE_MEASUREMENT_KEY_COLUMN_MD = "exercise_measurement_key"

# ===== APP LOGIC =====
MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 30
