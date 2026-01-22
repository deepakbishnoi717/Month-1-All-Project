# 🏦 ATM Banking System - Frontend & Backend Setup

Complete ATM Banking System with React Frontend and FastAPI Backend.

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

### Backend Setup (FastAPI)

1. **Navigate to project directory:**
   ```bash
   cd "c:\Users\HP\OneDrive\Desktop\Ready for comeback\week2"
   ```

2. **Activate Python virtual environment:**
   ```bash
   # On Windows
   .\week22\Scripts\Activate.ps1
   ```

3. **Install required packages:**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```

4. **Run the backend server:**
   ```bash
   uvicorn bank:app --reload
   ```
   - Backend will run on: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

---

### Frontend Setup (React)

1. **Open a new terminal and navigate to frontend:**
   ```bash
   cd "c:\Users\HP\OneDrive\Desktop\Ready for comeback\week2\fastapi-demo\frontend"
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```
   - Frontend will open on: `http://localhost:3000`

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

## 🔐 Test Account

After creating an account through the frontend, you can:
1. Login with your account number and PIN
2. Perform ATM operations

---

## 📁 Project Structure

```
week2/
├── bank.py                    (FastAPI backend)
├── Bankddmoduals.py          (Database models + ATMOperations)
├── BankDatabase.py           (Database connection)
├── Bankpy.py                 (Pydantic models)
│
└── fastapi-demo/frontend/
    ├── package.json
    ├── public/
    └── src/
        ├── App.js            (Main component)
        ├── App.css           (Styling)
        ├── index.js
        └── components/
            ├── CreateAccount.js    (Login/Register)
            └── ATMDashboard.js     (ATM operations)
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

## 🎨 Frontend Features

### Authentication
- Create new account
- Login with account number and PIN
- Logout functionality

### Dashboard
- Menu with quick access buttons
- Withdraw/Deposit transactions
- Real-time balance display
- Transaction history with timestamps
- Responsive design (mobile-friendly)

---

## ⚙️ Troubleshooting

**CORS Error:**
- Backend CORS is enabled for all origins
- Make sure backend is running on port 8000

**Database Connection Error:**
- Check BankDatabase.py configuration
- Ensure database server is running

**Port Already in Use:**
```bash
# Backend on different port
uvicorn bank:app --reload --port 8001

# Frontend on different port
PORT=3001 npm start
```

---

## 📝 Example Usage Flow

1. **Create Account:**
   - Go to "Create Account" tab
   - Fill in details (account #, name, PIN, etc.)
   - Click "Create Account"

2. **Login:**
   - Go to "Login" tab
   - Enter account number
   - Enter PIN
   - Click "Login"

3. **Withdraw Money:**
   - Click "Withdraw" button
   - Enter amount
   - Confirm

4. **Check Balance:**
   - Click "Balance" button
   - Your current balance displays

5. **View History:**
   - Click "History" button
   - See all transactions with timestamps

---

## 🔐 Security Notes

- PINs are stored in database (consider hashing in production)
- CORS is open to all origins (restrict in production)
- Use HTTPS in production
- Add request validation and rate limiting

---

## 📞 Support

If you encounter issues:
1. Check backend logs in terminal
2. Check browser console (F12)
3. Verify both servers are running
4. Check database connection settings

---

**Created with ❤️ for Banking System Learning**
