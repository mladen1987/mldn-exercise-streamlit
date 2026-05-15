# Exercise Tracker

## 📊 Overview

A Streamlit-based learning project exploring state-driven UI design, modular Python architecture, and Google Sheets as a lightweight database.

The app manages exercise master data and logs workout sessions with a structured, scalable workflow.

---

## 🚀 Version

**v0.5.2 - Session History Visualization (Spark Bars + Date Timeline)**

---

## ✨ Current Features

### 🔗 Google Sheets Data Layer
- Google Sheets used as lightweight database
- Centralized read/write service layer
- Cached reads with automatic invalidation
- Optimized to reduce API quota usage

---

### 🧩 Master Data Management (Unified Module)
- Single consolidated master data interface (input, remove, restore)
- Creation and deletion of exercise definitions
- Safe workflow with previews + backups
- Restore from timestamped backups
- State-driven UI

---

### 🏋️ Exercise Session Tracking

- Recommended workout suggestions based on history
- Dynamic exercise and measurement input
- **Session history preview with spark-style trend visualization**
  - Last 5 sessions per measurement
  - Date-based timeline display
  - Inline spark bars for quick trend interpretation
- Safe workflow with preview and checks before submission
- Google Sheets write-back
- State-driven UI

---

## 🧪 Tech Stack

- Streamlit
- Python
- Pandas
- Google Sheets API (`gspread`)
- Google Cloud Service Account Auth

---

## 🚀 Roadmap

- [x] Project setup
- [x] Google Sheets integration
- [x] Master data CRUD system
- [x] Backup + restore system
- [x] Session tracking (state machine UI)
- [x] Modular architecture (pages + states)
- [x] Cached data layer + API optimization
- [x] Unified master data module (input / remove / restore)
- [x] Session history visualization (spark bars + date view)
- [x] UI/UX improvements
- [ ] Analytics dashboard - Landing Page
- [ ] Authentication
- [ ] Deployment

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py
