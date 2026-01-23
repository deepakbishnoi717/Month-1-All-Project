# 🏦 ATM Banking System API

A complete **backend API** for an ATM Banking System built with **FastAPI** and **SQLAlchemy**.

## 📋 Features

- ✅ Create bank accounts
- ✅ Secure login with PIN verification
- ✅ Withdraw money (with balance checks)
- ✅ Deposit money
- ✅ Check account balance
- ✅ View transaction history
- ✅ Real-time balance updates
- ✅ Transaction recording (debit/credit)
- ✅ RESTful API design

## 🛠 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database management
- **Pydantic** - Data validation
- **PostgreSQL/SQLite** - Database
- **Uvicorn** - ASGI server

## 📁 Project Structure

```
Month-1-All-Project/
├── Project-1/
│   ├── main.py              # FastAPI main application
│   ├── models.py            # Database models + ATMOperations class
│   ├── database.py          # Database configuration
│   ├── schemas.py           # Pydantic data models
│   ├── START.bat            # Quick start script
│   └── INSTALLATION.md      # Detailed setup guide
├── README.md
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/deepakbishnoi717/Month-1-All-Project.git
cd Month-1-All-Project/Project-1
```

2. **Create virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# or
source venv/bin/activate      # Linux/Mac
```

3. **Install dependencies:**
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

4. **Run the server:**
```bash
uvicorn main:app --reload
```

Backend runs on: **http://localhost:8000**

## 📚 API Endpoints

### Account Management
- `POST /bankdata` - Create new account
- `GET /get_account/{account}` - Get account details
- `PUT /get_account/{account}` - Update account

### ATM Operations

#### Withdraw Money
```http
POST /atm/withdraw
Content-Type: application/json

{
  "account": 123,
  "pin": 4567,
  "amount": 100
}
```

#### Deposit Money
```http
POST /atm/deposit
Content-Type: application/json

{
  "account": 123,
  "pin": 4567,
  "amount": 500
}
```

#### Check Balance
```http
GET /atm/balance/{account}/{pin}
```

#### Get Transaction History
```http
GET /atm/transactions/{account}/{pin}
```

## 🔐 Database Schema

### BankModul Table
| Column  | Type    | Description          |
|---------|---------|----------------------|
| account | Integer | Primary Key          |
| name    | String  | Account holder name  |
| pin     | Integer | Security PIN         |
| bank    | String  | Bank name            |
| address | String  | Account address      |
| balance | Float   | Current balance      |

### Transaction Table
| Column          | Type     | Description                |
|-----------------|----------|----------------------------|
| transaction_id  | Integer  | Primary Key                |
| account_id      | Integer  | Foreign Key to BankModul   |
| type            | String   | 'debit' or 'credit'        |
| amount          | Float    | Transaction amount         |
| timestamp       | DateTime | Transaction time           |
| balance_after   | Float    | Balance after transaction  |

## 📊 Example Usage

### 1. Create Account
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

### 2. Withdraw Money
```bash
curl -X POST "http://localhost:8000/atm/withdraw" \
  -H "Content-Type: application/json" \
  -d '{
    "account": 123,
    "pin": 4567,
    "amount": 100
  }'
```

### 3. Check Balance
```bash
curl "http://localhost:8000/atm/balance/123/4567"
```

### 4. View Transaction History
```bash
curl "http://localhost:8000/atm/transactions/123/4567"
```

## 🧪 Testing

### Interactive API Documentation
FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Use these interfaces to:
- Explore all available endpoints
- Test API calls directly in the browser
- View request/response schemas

### Test with Postman
1. Import the API endpoints
2. Create a test collection
3. Test CRUD operations
4. Verify ATM operations

## 📝 Code Overview

### ATMOperations Class
Handles all ATM business logic:
- `verify_pin()` - Validate PIN
- `check_balance()` - Get account balance
- `withdraw()` - Withdraw with validation
- `deposit()` - Deposit with recording
- `get_transactions()` - Retrieve history
- `create_transaction()` - Record transactions

### API Endpoints
Each endpoint:
1. Gets database session
2. Creates ATMOperations instance
3. Calls appropriate method
4. Returns JSON response

## ⚙️ Configuration

### Database Connection
Edit `database.py` to change database settings:
```python
DATABASE_URL = "postgresql://user:password@localhost/atm_db"
# or for SQLite (default):
DATABASE_URL = "sqlite:///./atm.db"
```

### CORS Settings
CORS is enabled in `main.py` for all origins (configure for production):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🔒 Security Notes

**Current Implementation:**
- PIN stored in plain text (for learning purposes)

**Production Improvements Needed:**
- Hash passwords with bcrypt
- Use HTTPS
- Add JWT authentication tokens
- Implement rate limiting
- Add CORS restrictions
- Add comprehensive input validation
- Database encryption
- Environment variables for sensitive data

## 🐛 Troubleshooting

**Backend connection error:**
- Verify backend is running on port 8000
- Check if another process is using port 8000
- Look at terminal for error messages

**Database error:**
- Check database connection string
- Ensure database server is running (if using PostgreSQL)
- Check user permissions
- Verify SQLite file permissions (if using SQLite)

**Module import errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## 🚢 Deployment

### Railway/Render/Heroku
```bash
# Create Procfile
web: uvicorn main:app --host 0.0.0.0 --port $PORT

# Deploy with git
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## 👥 Contributing

Feel free to fork and submit pull requests!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - feel free to use this project for learning and development.

## 🎓 Educational Purpose

This project is designed for learning:
- Backend web development with Python
- RESTful API design
- Database design & SQL
- ORM usage with SQLAlchemy
- User authentication & validation
- Transaction management

## 🎨 Credits

**Backend Development:** Deepak Bishnoi  
**Learning Project:** ATM & Banking Systems API

---

**Created for learning Backend Development and API Design** 🚀
