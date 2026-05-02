# Exercise Tracker

## 📊 Overview

This is a simple learning project built with Streamlit to explore Python app development.

The app currently connects to Google Sheets and reads exercise data for visualization.

---

## 🚀 Version

**v0.1.0 - Master Data Input System**

---

## ✨ Current Features

- 🔗 Connects to Google Sheets as a data source  
- 📥 Reads data from a live spreadsheet  
- 🧩 Master data input system:
  - Category → Group → Type → Measurement hierarchy  
  - Ability to add new values inline  
  - Multiple measurements per entry  
  - Writes updates back to Google Sheets  

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
- [ ] Delete existing master data entries  
- [ ] Improve UI/UX (searchable dropdowns, validation)  

---

## ▶️ Run Locally

```bash
slit_venv
pip install -r requirements.txt
streamlit run app.py
