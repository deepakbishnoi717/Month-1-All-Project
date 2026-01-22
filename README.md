# 🏦 ATM Banking System

A complete full-stack ATM Banking System built with **FastAPI** (Backend) and **React** (Frontend).

## 📋 Features

- ✅ Create bank accounts
- ✅ Secure login with PIN verification
- ✅ Withdraw money (with balance checks)
- ✅ Deposit money
- ✅ Check account balance
- ✅ View transaction history
- ✅ Real-time balance updates
- ✅ Transaction recording (debit/credit)
- ✅ Responsive mobile-friendly UI

## 🛠 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database management
- **Pydantic** - Data validation
- **PostgreSQL/SQLite** - Database

### Frontend
- **React 18** - UI library
- **Axios** - HTTP client
- **CSS3** - Styling with gradients and animations

## 📁 Project Structure

```
atm-banking-system/
├── bank.py                      # FastAPI main application
├── Bankddmoduals.py            # Database models + ATMOperations class
├── BankDatabase.py             # Database configuration
├── Bankpy.py                   # Pydantic data models
├── SETUP_INSTRUCTIONS.md       # Detailed setup guide
│
└── fastapi-demo/frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js              # Main component
        ├── App.css             # Global styles
        ├── index.js            # React entry point
        ├── index.css
        └── components/
            ├── CreateAccount.js    # Login/Register
            └── ATMDashboard.js     # ATM operations
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm

### Backend Setup

```bash
cd week2
python -m venv week22
.\week22\Scripts\Activate.ps1
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
uvicorn bank:app --reload
```

Backend runs on: **http://localhost:8000**

### Frontend Setup

```bash
cd fastapi-demo/frontend
npm install
npm start
```

Frontend runs on: **http://localhost:3000**

## 📚 API Endpoints

### Account Management
- `POST /bankdata` - Create account
- `GET /get_account/{account}` - Get account details
- `PUT /get_account/{account}` - Update account

### ATM Operations
- `POST /atm/withdraw` - Withdraw money
  ```json
  {
    "account": 123,
    "pin": 4567,
    "amount": 100
  }
  ```

- `POST /atm/deposit` - Deposit money
  ```json
  {
    "account": 123,
    "pin": 4567,
    "amount": 500
  }
  ```

- `GET /atm/balance/{account}/{pin}` - Check balance

- `GET /atm/transactions/{account}/{pin}` - Get transaction history

## 🔐 Database Schema

### BankModul Table
```
account (PK) | name | pin | bank | address | balance
```

### Transaction Table
```
transaction_id (PK) | account_id (FK) | type | amount | timestamp | balance_after
```

## 🎨 Frontend Features

### Authentication Page
- Login with account number & PIN
- Create new account with details
- Input validation

### Dashboard
- Quick menu with operation buttons
- Withdraw/Deposit forms
- Balance display with currency formatting
- Transaction history with timestamps
- Responsive design for mobile devices
- Logout functionality

## 📊 Example Usage

1. **Create Account:**
   - Account #: 123
   - Name: John Doe
   - PIN: 4567
   - Bank: ABC Bank
   - Address: 123 Main St
   - Initial Balance: $5000

2. **Login & Withdraw:**
   - Login with account 123, PIN 4567
   - Click Withdraw
   - Enter amount: $100
   - See new balance

3. **View History:**
   - Click History
   - See all transactions with dates

## ⚙️ Configuration

### Database Connection
Edit `BankDatabase.py` to change database settings:
```python
DATABASE_URL = "postgresql://user:password@localhost/atm_db"
```

### API CORS
CORS is enabled in `bank.py` for all origins (configure in production):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🧪 Testing

### Test with FastAPI Docs
- Go to: **http://localhost:8000/docs**
- Interactive API documentation
- Test endpoints directly

### Test with Postman
- Import endpoints
- Create test collection
- Test CRUD operations

## 🔒 Security Notes

**Current Implementation:**
- PIN stored in plain text (for learning)

**Production Improvements Needed:**
- Hash passwords with bcrypt
- Use HTTPS
- Add JWT authentication tokens
- Implement rate limiting
- Add CORS restrictions
- Add input validation
- Database encryption

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

## 🐛 Troubleshooting

**Frontend not loading:**
- Hard refresh: `Ctrl + Shift + R`
- Clear cache: `Ctrl + Shift + Delete`
- Check terminal for npm errors

**Backend connection error:**
- Verify backend is running on port 8000
- Check CORS settings
- Look at browser console (F12)

**Database error:**
- Check database connection string
- Ensure database server is running
- Check user permissions

## 🚢 Deployment

### Vercel (Frontend)
```bash
npm run build
# Deploy 'build' folder to Vercel
```

### Railway/Heroku (Backend)
```bash
# Create Procfile
# Deploy with git
```

## 📚 Learning Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)

## 👥 Contributing

Feel free to fork and submit pull requests!

## 📄 License

MIT License - feel free to use this project

## 🎓 Educational Purpose

This project is designed for learning:
- Full-stack web development
- RESTful API design
- Database design & SQL
- Frontend-backend integration
- User authentication & validation

## 🎨 Credits

- **Frontend Development:** Vise Coding
- **Backend Development:** Full-stack implementation
- **UI/UX Design:** Modern responsive design with React & CSS3

---

**Created for learning ATM & Banking Systems**
