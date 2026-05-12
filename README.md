# Exercise Tracker

## 📊 Overview

This is a learning project built with Streamlit to explore Python app development, state-driven UI design, modular architecture, and Google Sheets integration.

The app uses Google Sheets as a lightweight database and allows managing exercise master data and logging workout sessions.

---

## 🚀 Version

**v0.5.0 - Data Layer Caching + API Optimization Refactor**

---

## ✨ Current Features

### 🔗 Google Sheets Data Layer
- Google Sheets used as lightweight database
- Centralized read/write service architecture
- Cached data access with automatic invalidation
- Optimized to minimize API quota usage

---

### 🧩 Master Data Management
- Category → Group → Type → Measurement hierarchy
- Inline creation of new exercise structures
- Safe delete workflow with preview + backup
- Restore previous master data versions from backups

---

### 🏋️ Exercise Session Tracking
- State-driven workout logging flow
- Recommended workout groups based on history
- Dynamic exercise + measurement rendering
- Session preview before submission
- Google Sheets write-back with success-state handling

---

### 💾 Backup & Recovery
- Automatic timestamped backups
- Retention cleanup (latest 5 backups kept)
- Restore preview + overwrite protection

---

### 💾 Backup System

- Timestamped backups stored in separate Google Sheet
- Automatic retention (keeps latest 5 backups)
- Safe restore mechanism with preview

---

## 🧪 Tech Stack

- Streamlit
- Python
- Pandas
- Google Sheets API (`gspread`)
- Google Cloud Service Account Authentication

---

## 🚀 Roadmap

- [x] Project setup
- [x] Google Sheets integration
- [x] Master data CRUD system
- [x] Backup + restore system
- [x] Exercise session logging (state machine UI)
- [x] Modular page/state architecture
- [x] Shared cached data layer
- [x] API optimization + cache invalidation system
- [ ] Improve UI/UX
- [ ] Add per-exercise progression charts
- [ ] Add analytics
- [ ] Add authentication / multi-user support

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py