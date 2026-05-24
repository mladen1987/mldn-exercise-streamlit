# Exercise Tracker

> *v1.1.0*

A simple Streamlit app for exercise logging and master data management.

## What it does

- Connects to Google Sheets for data storage.
- Stores per-session exercise values in `exercise_data`.
- Stores exercise definitions and measurements in `exercise_master_data`.
- Supports editing master data and inputting exercise session values.
- Visualizes exercise progress and history.

## Tech stack

- Python
- Streamlit
- Pandas
- Altair
- gspread
- google-auth
- google-auth-oauthlib
- requests
- streamlit-autorefresh

## Guest Mode

Select **Continue as Guest** on the login page to test the app without a a Google Sheets connection.

You can do so on the stremlit cloud deployed version [here](https://mldn-exercise-app-huybu2hxh9x6iwtavmcorw.streamlit.app/).

Or by running the app locally:

- Uses local CSV files under `dummy_data/`
- No external credentials required
- Functional UI for testing and demo

## Using with own data:

If you find the app interesting, here are basic instructions about setting it up with own data.

You would need to create a google service account key, via the google cloud console. You can find instructions [here](https://docs.cloud.google.com/iam/docs/keys-create-delete).

Once you have the key, follow the steps below.

1. Create `.streamlit/secrets.toml` locally with:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
auth_uri = "your_auth_uri"
token_uri = "your_token_uri"
auth_provider_x509_cert_url = "your_auth_provider_x509_cert_url"
client_x509_cert_url = "your_client_x509_cert_url"
universe_domain = "your_universe_domain"

[authentication]
app_password = "your_password"
```

- `gcp_service_account` information can be found in the downloaded google service account key `.json` file.
- `app_password` should be a SHA256 hash.
- Generate it using `utils/hash_password.py`.

2. Create the Google Sheets:

- Main sheet with tabs `exercise_data` and `exercise_master_data`
- Backup sheet for copies of `exercise_master_data` when rows are removed

> *Use the sample schema in `dummy_data/exercise_data.csv` and `dummy_data/exercise_master_data.csv`.*

3. Update `config.py`:

```python
SK_MAIN_DATA = "google_sheet_key_for_your_main_data_here"
SK_BACKUP_DATA = "google_sheet_key_for_your_master_data_backup_here"
```

4. Run locally:

```bash
# On first use
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

# Subsequent uses
source venv/bin/activate
streamlit run app.py
```

## Notes

- `exercise_data` contains per-session values.
- `exercise_master_data` contains exercise definitions and measurement metadata.
- Backup sheet stores removed master data entries for recovery.
