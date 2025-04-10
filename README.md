# 💸 Expense Tracker App

A full-stack **Expense Tracker** application built with **FastAPI** (Python) for the backend and **React** for the frontend. It allows users to log daily expenses, view detailed reports, and track spending trends across different months and categories.

---

## ✅ Features

-   📥 Add expenses with category and date
-   📊 Dashboard with total and monthly summaries
-   🚨 Alerts for overspending in specific categories
-   🧾 Category-wise spending vs. budget report
-   🗑️ Expense deletion and table view

---

## 🏗️ Folder Structure

expense-tracker-app/├── backend/│   ├── main.py│   ├── database.py│   ├── models.py│   ├── routes/│   └── requirements.txt├── frontend/│   ├── src/│   │   ├── components/│   │   ├── pages/│   │   └── App.jsx│   ├── public/│   └── package.json└── README.md
---

## ⚙️ Installation & Setup Guide

### 🔙 Backend (FastAPI - Python)

1.  Open terminal and navigate to backend folder:

    ```bash
    cd backend
    ```

2.  Create and activate virtual environment:

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the backend server:

    ```bash
    uvicorn main:app --reload
    ```

5.  API Docs: http://localhost:8000/docs

### 💻 Frontend (React)

1.  Open a new terminal and navigate to frontend folder:

    ```bash
    cd frontend
    ```

2.  Install dependencies:

    ```bash
    npm install
    ```

3.  Start the React dev server:

    ```bash
    npm run dev
    ```

4.  App opens at: http://localhost:3000

---

## 🧾 Pages Overview

### 📍 Dashboard

-   View total spending
-   Monthly expense trends
-   Budget status by category

### ➕ Add Expense

-   Add amount, category, and date
-   Alerts if spending crosses limit (e.g., Food budget)

### 📊 Reports

-   Total spent per month
-   Budget vs Spent chart by category

### 📜 All Expenses

-   Full list of expenses
-   Delete individual entries

---

## 🛠️ Backend Requirements

-   fastapi
-   uvicorn
-   sqlalchemy
-   pydantic
-   aiofiles

Install using:

```bash
pip install -r requirements.txt
📦 Run Commands Summary# Backend
cd backend
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
