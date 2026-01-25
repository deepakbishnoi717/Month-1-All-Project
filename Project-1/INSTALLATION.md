# 🏦 ATM Banking System - Installation Guide

Follow these steps to set up and run the ATM Banking System on your local machine.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10+**
- **PostgreSQL** (Ensure it is running)
- **Git** (Optional)

---

## 🚀 Step-by-Step Installation

### 1. Database Setup
First, create a new database in PostgreSQL. You can use **pgAdmin** or the **psql** terminal:
```sql
CREATE DATABASE deepak;
```

### 2. Get the Code
```bash
git clone https://github.com/deepakbishnoi717/Month-1-All-Project.git
cd Month-1-All-Project/Project-1
```

### 3. Install Dependencies
It is highly recommended to use a virtual environment:
```bash
# Create venv
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 4. Configure Database
Update [database.py](database.py) with your actual PostgreSQL credentials:
```python
db_url = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/deepak"
```
> [!IMPORTANT]
> Change `YOUR_PASSWORD` to your actual PostgreSQL password.

### 5. Run the Application
You can use the provided batch script or run uvicorn directly:

**Option A: Using START.bat (Windows)**
```powershell
.\START.bat
```

**Option B: Manual Command**
```bash
uvicorn main:app --reload --port 8000
```

---

## 🌐 Accessing the App

Once the server is running:
- **Frontend App**: [http://localhost:8000](http://localhost:8000)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📁 Project Overview

| File | Description |
| :--- | :--- |
| `main.py` | Main API server and Frontend host. |
| `models.py` | SQLAlchemy models and ATM operations logic. |
| `database.py` | Connection string and engine setup. |
| `schemas.py` | Pydantic models for request validation. |
| `index.html` | The banking interface. |
| `style.css` | Glassmorphism design system. |
| `script.js` | Frontend interaction and API calls. |

---

## ⚙️ Troubleshooting

- **Authentication Failed**: Double-check the password in `database.py`.
- **Column not found**: If you had an old table, run the [reset_db.py](reset_db.py) script to refresh the schema.
- **Port 8000 busy**: Change the port in the uvicorn command using `--port 8080`.

---
**Created with ❤️ by the development team.**

