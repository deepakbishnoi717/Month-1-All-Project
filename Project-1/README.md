# 🏦 ATM Banking System (Full-Stack)

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=render)](https://atm-banking-system.onrender.com)

A premium, portfolio-ready full-stack banking application built with **FastAPI**, **PostgreSQL**, and **Vanilla JavaScript**. 

This project demonstrates clean architecture, robust API design, and modern UI practices.

---

## 🔗 Live Application
You can access the live version of this project here:
👉 **[https://atm-banking-system.onrender.com](https://atm-banking-system.onrender.com)**

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
│   ├── main.py            # API Entry point & Routes
│   ├── models.py          # Database Models
│   ├── database.py        # Connection logic
│   ├── .env               # Environment secrets
│   └── requirements.txt   # Dependencies
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

### 3. Running Locally (Windows)
To start both backend and frontend automatically:
```powershell
.\START.bat
```

### 4. Manual Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
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
**Backend developed and designed by Deepak** | **Frontend crafted with AI** 🚀
