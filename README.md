# Exercise Tracker

## 📊 Overview

This is a learning project built with Streamlit to explore Python app development, state-driven UI design, and Google Sheets integration.

The app uses Google Sheets as a lightweight database and allows managing exercise master data and logging workout sessions.

---

## 🚀 Version

**v0.4.0 - Exercise Session State Machine + Modular UI Refactor**

---

## ✨ Current Features

### 🔗 Data Layer
- Connects to Google Sheets as primary data source
- Reads and writes structured exercise and master data
- Service-layer abstraction for all Google Sheets interactions

---

### 🧩 Master Data Management (CRUD)
- Category → Group → Type → Measurement hierarchy
- Add new exercise structures inline
- Remove entries with safe preview before deletion
- Writes updates back to Google Sheets

---

### 🏋️ Exercise Session Tracker (NEW)

State-driven workout logging system:
- Select exercise category and group
- Recommended workout group based on historical data
- Dynamic rendering of exercise types
- Expandable measurement inputs per exercise type
- Session preview before submission
- Google Sheets write-back per session

---

### 💾 Backup System
- Timestamped backups stored in separate Google Sheet
- Automatic retention (keeps latest 5 backups)
- Safe restore mechanism with preview

---

## 🧪 Tech Stack

- Streamlit
- Python
- Google Sheets API (gspread)
- Google Cloud Service Account Authentication
- Pandas

---

## ⚠️ Known Issues / Technical Notes

### Google Sheets API Quota Limitation

Occasionally the app may hit:

> **Error 429: Quota exceeded for quota metric 'Read requests'**

This happens when:
- Too many reads are triggered in short succession
- Streamlit reruns cause repeated sheet reads

#### Recommended fixes (future improvements):

- Add caching layer (`st.cache_data`)
- Reduce repeated calls to `get_master_data()`
- Batch Google Sheets reads where possible
- Introduce lightweight local session caching in `st.session_state`

---

## 🚀 Roadmap

- [x] Project setup
- [x] Google Sheets integration
- [x] Master data CRUD system
- [x] Backup + restore system
- [x] Exercise session logging (state machine UI)
- [ ] Add caching layer to reduce API calls (fix 429 errors)
- [ ] Improve UI UX (searchable dropdowns, keyboard flow)
- [ ] Add analytics dashboard (progress tracking)
- [ ] Add per-exercise progression charts

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py