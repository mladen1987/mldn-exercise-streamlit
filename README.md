# Exercise Tracker

## 📊 Overview

A Streamlit-based learning project exploring state-driven UI design, modular Python architecture, and Google Sheets as a lightweight database.

The app manages exercise master data, logs workout sessions, and visualizes training progress with a structured, scalable workflow.

---

## 🚀 Version

**v0.7.0 - Analytics Dashboard + Contribution Heatmap + Progress Visualizations**

---

## ✨ Current Features

### 🔐 Authentication System
- Simple password-based login system
- Session stored in `st.session_state`
- Logout functionality via sidebar
- Authentication gate before data layer access

---

### 🧪 Guest Mode (Demo Mode)
- Users can enter the app without authentication
- Fully functional UI without Google Sheets dependency
- Uses local CSV files instead of cloud storage:
  - `dummy_data/exercise_master_data.csv`
  - `dummy_data/exercise_data.csv`
  - `dummy_data/backup_exercise_master_data_*.csv`
- No persistent writes (read-only demo experience)
- Safe sandbox for showcasing app features

---

### 📈 Analytics Dashboard (Landing Page)

#### GitHub-Style Contribution Heatmap
- Daily exercise activity visualization
- One tile per day over the past 365 days
- Week-based layout (Monday → Sunday)
- Green tiles indicate workout activity
- Dynamic yearly session count summary
- Month labels above heatmap

#### Progress Visualization System
- Expandable category/group sections
- Automatic chart generation from master data
- Individual charts for every:
  - Exercise type
  - Measurement
- Interactive line charts with:
  - Date-based x-axis
  - Value-based y-axis
  - Hover tooltips
- Fully data-driven visualization architecture

---

### 🔗 Google Sheets Data Layer
- Google Sheets used as lightweight database (production mode)
- Centralized read/write service layer
- Cached reads with automatic invalidation
- Optimized to reduce API quota usage
- Writes are disabled in guest mode

---

### 🧩 Master Data Management (Unified Module)
- Single consolidated master data interface (input, remove, restore)
- Creation and deletion of exercise definitions
- Safe workflow with previews + backups
- Restore from timestamped backups
- State-driven UI
- Supports both:
  - Google Sheets (production)
  - Local CSV backups (guest mode)

---

### 🏋️ Exercise Session Tracking
- Recommended workout suggestions based on history
- Dynamic exercise and measurement input
- Session history preview with spark-style trend visualization
  - Last 5 sessions per measurement
  - Date-based timeline display
  - Inline spark bars for quick trend interpretation
- Safe workflow with preview and checks before submission
- Google Sheets write-back (disabled in guest mode)
- State-driven UI

---

## 🧪 Tech Stack

- Streamlit
- Python
- Pandas
- Altair
- Google Sheets API (`gspread`)
- Google Cloud Service Account Auth
- Local CSV fallback system (guest mode)

---

## 🏗️ Architecture Highlights

- State-driven UI (Streamlit session state)
- Dual data layer system:
  - **Production:** Google Sheets
  - **Guest mode:** Local CSV files
- Conditional imports based on runtime mode
- Modular visualization system
- Clear separation of:
  - UI layers (`ui_pages/`)
  - Data services (`services/`)
  - Visualization utilities (`utils/`)
  - Dummy data layer (`dummy_data/`)

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
- [x] Authentication system
- [x] Guest mode (CSV-based sandbox)
- [x] Analytics dashboard
- [x] Contribution heatmap
- [x] Dynamic progress visualizations
- [ ] Deployment improvements

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py
```
