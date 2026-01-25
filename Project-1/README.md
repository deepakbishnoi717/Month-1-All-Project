# 🏦 ATM Banking System (Full-Stack)

A premium, full-stack ATM Banking System built with **FastAPI**, **Vanilla JavaScript**, and **PostgreSQL**. Featuring a modern Glassmorphism UI, robust backend validation, and real-time transaction tracking.

![ATM Banner](money-background.png)

## 🌟 Features

- **Modern UI/UX**: Sleek, money-themed design with Glassmorphism effects and micro-animations.
- **Secure Authentication**: Account creation and login with validated Account Numbers (5+ digits) and PINs (4 digits).
- **Core Banking Operations**:
    - 💸 **Withdrawal**: Instant cash removal with balance verification.
    - 💰 **Deposit**: Seamlessly add funds to your account.
    - 💵 **Balance Inquiry**: Real-time balance updates.
    - 📊 **Transaction History**: Detailed logs of all your credits and debits.
- **Self-Hosted Frontend**: The backend automatically serves the frontend, making deployment a breeze.
- **PostgreSQL Integration**: Robust data persistence for accounts and transactions.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python 3.12+)
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Modern CSS with Glassmorphism and Poppins typography.
- **Server**: Uvicorn

## 🚀 Quick Start

### 1. Prerequisites
- Python installed
- PostgreSQL installed and running
- A browser (Chrome, Edge, Firefox, etc.)

### 2. Database Setup
Ensure you have a PostgreSQL database created. For example, create a database named `atm_db`.

### 3. Installation
```bash
# Clone the repository
git clone https://github.com/deepakbishnoi717/Month-1-All-Project.git
cd Month-1-All-Project/Project-1

# Install dependencies
pip install -r requirements.txt
```

### 4. Configuration
Update the `database.py` file with your actual PostgreSQL credentials:
```python
db_url = "postgresql://user:password@localhost:5432/your_database_name"
```

### 5. Launch
Simply run the included batch script (Windows):
```powershell
.\START.bat
```
Or start manually:
```bash
uvicorn main:app --reload --port 8000
```

Access the app at: **[http://localhost:8000](http://localhost:8000)**

## 📁 Project Structure

- `main.py`: The heart of the application, serving the API and Frontend.
- `models.py`: Database schemas and ATM logic.
- `database.py`: Connection configuration.
- `index.html`: The main UI.
- `style.css`: Premium styling.
- `script.js`: Frontend logic and API integration.

---
Developed as part of the **Month-1 Final Project**. 💻🚀
