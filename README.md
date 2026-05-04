# Exercise Tracker

## 📊 Overview

This is a simple learning project built with Streamlit to explore Python app development.

The app connects to Google Sheets and allows managing exercise master data for tracking and visualization.

---

## 🚀 Version

**v0.2.0 - Master Data CRUD (Input + Remove)**

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
  - Safe delete with backup to separate Google Sheet  

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
- [ ] Restore from backup  
- [ ] Improve UI/UX (searchable dropdowns, validation)  

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py
