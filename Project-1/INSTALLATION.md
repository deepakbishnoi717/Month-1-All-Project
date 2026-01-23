# 🏦 ATM Banking System API - Installation Guide

Complete backend API for ATM Banking System built with FastAPI.

## 📋 Features

- ✅ Create new bank accounts
- ✅ Login with account number and PIN
- ✅ Withdraw money (with balance check)
- ✅ Deposit money
- ✅ Check account balance
- ✅ View transaction history (debit/credit)
- ✅ Security PIN verification
- ✅ Real-time balance updates

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Backend Setup (FastAPI)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deepakbishnoi717/Month-1-All-Project.git
   cd Month-1-All-Project/Project-1
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # On Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```

4. **Run the backend server:**
   ```bash
   uvicorn main:app --reload
   ```
   - Backend will run on: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`
   - Alternative Docs: `http://localhost:8000/redoc`

---

## 📊 API Endpoints

### Account Management
- `POST /bankdata` - Create new account
- `GET /get_account/{account}` - Get account details
- `PUT /get_account/{account}` - Update account info

### ATM Operations
- `POST /atm/withdraw` - Withdraw money
  - Params: `account`, `pin`, `amount`
  
- `POST /atm/deposit` - Deposit money
  - Params: `account`, `pin`, `amount`
  
- `GET /atm/balance/{account}/{pin}` - Check balance
  
- `GET /atm/transactions/{account}/{pin}` - Get transaction history

---

## 🧪 Testing the API

### Using Interactive Swagger UI

1. Start the server: `uvicorn main:app --reload`
2. Open browser: `http://localhost:8000/docs`
3. Test endpoints directly in the browser

### Using cURL

**Create Account:**
```bash
curl -X POST "http://localhost:8000/bankdata" \
  -H "Content-Type: application/json" \
  -d '{
    "account": 123,
    "name": "John Doe",
    "pin": 4567,
    "bank": "ABC Bank",
    "address": "123 Main St",
    "balance": 5000
  }'
```

**Withdraw Money:**
```bash
curl -X POST "http://localhost:8000/atm/withdraw?account=123&pin=4567&amount=100"
```

**Check Balance:**
```bash
curl "http://localhost:8000/atm/balance/123/4567"
```

**View Transaction History:**
```bash
curl "http://localhost:8000/atm/transactions/123/4567"
```

### Using Postman

1. Import the API endpoints
2. Set base URL: `http://localhost:8000`
3. Test each endpoint with appropriate parameters

---

## 📁 Project Structure

```
Project-1/
├── main.py              # FastAPI main application
├── models.py            # Database models + ATMOperations class
├── database.py          # Database configuration
├── schemas.py           # Pydantic data models
├── START.bat            # Quick start script (Windows)
└── INSTALLATION.md      # This file
```

---

## 🔧 Database Schema

### BankModul Table
```
account (Primary Key) - Account number
name - Account holder name
pin - 4-digit security code
bank - Bank name
address - Address
balance - Current balance
```

### Transaction Table
```
transaction_id - Auto-increment ID
account_id - Account number (FK)
transaction_type - "debit" or "credit"
amount - Transaction amount
timestamp - When transaction occurred
balance_after - Balance after transaction
```

---

## ⚙️ Configuration

### Database Connection

By default, the application uses SQLite. To change the database:

Edit `database.py`:
```python
# For PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost/atm_db"

# For SQLite (default)
DATABASE_URL = "sqlite:///./atm.db"
```

### CORS Settings

CORS is enabled for all origins in `main.py`. For production, restrict origins:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ⚙️ Troubleshooting

**Port Already in Use:**
```bash
# Run on different port
uvicorn main:app --reload --port 8001
```

**Database Connection Error:**
- Check `database.py` configuration
- Ensure database server is running (if using PostgreSQL)
- Verify SQLite file permissions (if using SQLite)

**Module Import Errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**CORS Error:**
- Backend CORS is enabled for all origins
- Make sure backend is running on port 8000
- Check browser console for specific error

---

## 📝 Example Usage Flow

### 1. Create Account
```bash
POST /bankdata
{
  "account": 123,
  "name": "John Doe",
  "pin": 4567,
  "bank": "ABC Bank",
  "address": "123 Main St",
  "balance": 5000
}
```

### 2. Withdraw Money
```bash
POST /atm/withdraw?account=123&pin=4567&amount=100
```

### 3. Check Balance
```bash
GET /atm/balance/123/4567
```

### 4. View Transaction History
```bash
GET /atm/transactions/123/4567
```

---

## 🔐 Security Notes

**Current Implementation:**
- PINs are stored in database (consider hashing in production)
- CORS is open to all origins (restrict in production)

**Production Improvements:**
- Use HTTPS
- Hash passwords with bcrypt
- Add JWT authentication tokens
- Implement request validation and rate limiting
- Use environment variables for sensitive data
- Add comprehensive logging

---

## 🚢 Deployment

### Using Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Using Railway/Render/Heroku

Create `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Deploy with git:
```bash
git push heroku main
```

---

## 📞 Support

If you encounter issues:
1. Check backend logs in terminal
2. Verify server is running on correct port
3. Check database connection settings
4. Review API documentation at `/docs`

---

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

---

**Created for Backend Development Learning** 🚀
