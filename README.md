# Exercise Tracker

**v1.0.0 – First Deployment**

## 📊 Overview

Streamlit app for tracking workouts, logging exercise sessions, and visualizing progress.

---

## ✨ Features

### 🔐 Authentication

- Simple login/logout
- Guest Mode
  - Uses local CSV files
  - Read-only demo mode

---

### 📈 Analytics

- Exercise Session Distribution Heatmap
- Progress Charts line charts

---

### 🏋️ Workout Tracking

- Dynamic input per measurement
- Spark history per metric

---

### 🧩 Master Data
- Create / remove / restore exercises
- Backup + restore support

---

## 🧪 Tech Stack
Streamlit · Python · Pandas · Altair · Google Sheets API

---

## 🏗️ Architecture
- State-driven UI
- Dual data layer (Sheets / CSV)
- Modular structure:
  - `ui_pages/`
  - `services/`
  - `utils/`

---

## 🚀 Roadmap
- Session tracking ✔
- Master data system ✔
- Heatmap ✔
- Progress charts ✔
- Guest mode ✔
- Deployment ⏳

---

## ▶️ Run

```bash
pip install -r requirements.txt
streamlit run app.py
