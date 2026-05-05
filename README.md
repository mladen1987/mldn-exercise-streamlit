# Exercise Tracker

## 📊 Overview

This is a simple learning project built with Streamlit to explore Python app development.

The app connects to Google Sheets and allows managing exercise master data for tracking and visualization.

---

## 🚀 Version

**v0.3.0 - Master Data Management (CRUD + Backup & Restore)**

---

## ✨ Current Features

- 🔗 Connects to Google Sheets as a data source  
- 📥 Reads data from a live spreadsheet  

- 🧩 Master data input system:
  - Category → Group → Type → Measurement hierarchy  
  - Ability to add new values inline  
  - Multiple measurements per entry  
  - Writes updates back to Google Sheets  

- 🗑️ Master data removal system:
  - Filter by category → group → type → measurement  
  - Supports partial and multi-select filtering  
  - Preview rows before deletion  
  - Safe delete with automatic backup  

- 💾 Backup system:
  - Backups stored in a separate Google Sheet  
  - Timestamped backup versions  
  - Automatic cleanup (keeps latest 5 backups)  

- ♻️ Restore system:
  - View available backups with timestamps  
  - Preview backup data before restoring  
  - Restore full master data from selected backup  
  - Automatic backup before restore (safety layer)  

---

## 🧪 Tech Stack

- Streamlit  
- Python  
- Google Sheets API (via gspread)  
- Google Cloud service account authentication  

---

## 🚀 Current Status / Roadmap

- [x] Project setup  
- [x] Google Sheets connection  
- [x] Master data read + write flow  
- [x] Dynamic input system (category/group/type/measurements)  
- [x] Delete existing master data entries (with backup)  
- [x] Backup management (limit + cleanup)  
- [x] Restore from backup  
- [ ] Improve UI/UX (searchable dropdowns, validation)  
- [ ] Add data visualization module  

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py
