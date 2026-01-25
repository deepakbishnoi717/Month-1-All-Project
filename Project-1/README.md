# 🏦 ATM Banking System (Full-Stack)

A premium, portfolio-ready full-stack banking application built with **FastAPI**, **PostgreSQL**, and **Vanilla JavaScript**. 

This project demonstrates clean architecture, robust API design, and modern UI practices.

---

## 🏗️ Architecture

The project is divided into two distinct components:

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | FastAPI, SQLAlchemy, PostgreSQL | RESTful API with automated documentation and secure transaction logic. |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JS | Responsive, single-page application (SPA) with real-time UI updates. |

### 📁 Project Structure

```text
atm-banking-system/
├── backend/               # Python/FastAPI Service
│   ├── app/               # Logic & Models
│   ├── .env               # Environment secrets
│   ├── requirements.txt   # Dependencies
│   └── reset_db.py        # Database utility
├── frontend/              # Web Interface
│   ├── assets/            # CSS & Visuals
│   ├── js/                # Scripting
│   └── index.html         # Main page
├── START.bat              # Quick Launch (Windows)
└── README.md              # Project Manual
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **PostgreSQL** (Service must be running)

### 2. Environment Configuration
Navigate to `backend/` and copy `.env.example` to `.env`. Update your credentials:
```env
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_database_name
```

### 3. Quick Run (Windows)
```powershell
.\START.bat
```

### 4. Manual Setup
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# UI
# Automatically served by backend at http://localhost:8000
```

---

## 🔥 Key Technical Features

### 🛡️ Robust Validation
- Used **Pydantic** for typed request/response validation.
- Implemented `HTTPException` for clean RESTful error reporting.

### 💰 Transactional Integrity
- Atomic database commits for all money transfers.
- Real-time transaction logging with historical tracking.

### 🎨 Modern UI Design
- **Glassmorphism**: High-end transparent UI elements with backdrop filtering.
- **Micro-animations**: Interactive hover states and bounce effects for a premium feel.

---

## 📈 Future Enhancements
- [ ] **PIN Hashing**: Secure storage using `bcrypt`.
- [ ] **JWT Auth**: Transition from SessionStorage to stateless JWT tokens.
- [ ] **Admin Dashboard**: Analytics for global bank health.

---
**Created for a Portfolio Showcase** 🚀
