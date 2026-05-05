def extract_timestamp(sheet_name):
    try:
        parts = sheet_name.split("_")
        return parts[-2] + "_" + parts[-1]  # YYYYMMDD_HHMMSS
    except:
        return ""
