from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session 
from database import engine, sessionlocalbank
from schemas import Bankdata
from models import Baseb, BankModul, ATMOperations, Transaction

app = FastAPI()

# Enable CORS for API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Baseb.metadata.create_all(engine)

def get_db():
    db = sessionlocalbank()
    try :
        yield db
    finally :
        db.close()


@app.post("/bankdata")
def add_bank_data(item :Bankdata, db : Session = Depends(get_db)):
    new_data = BankModul(
        account = item.account,
        name = item.name,
        pin = item.pin,
        bank = item.bank,
        address = item.address,
        balance = item.balance
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.get("/get_account/{account}")
def get_account(account : int, db : Session = Depends(get_db)) :
    data = db.query(BankModul).filter(account == BankModul.account).first()
    return data

@app.put("/get_account/{account}")
def put_data(account : int, item: Bankdata, db : Session = Depends(get_db)):
    data = db.query(BankModul).filter(BankModul.account == account).first()
    if data:
        data.name = item.name
        data.pin = item.pin
        data.bank = item.bank
        data.address = item.address
        data.balance = item.balance
        db.commit()
        db.refresh(data)
    return data


# ================ ATM ENDPOINTS ================

@app.post("/atm/withdraw")
def withdraw(account: int, pin: int, amount: float, db: Session = Depends(get_db)):
    """
    Withdraw money from account
    Request body: {account, pin, amount}
    """
    atm = ATMOperations(db)
    result = atm.withdraw(account, pin, amount)
    return result


@app.post("/atm/deposit")
def deposit(account: int, pin: int, amount: float, db: Session = Depends(get_db)):
    """
    Deposit money into account
    Request body: {account, pin, amount}
    """
    atm = ATMOperations(db)
    result = atm.deposit(account, pin, amount)
    return result


@app.get("/atm/balance/{account}/{pin}")
def check_balance(account: int, pin: int, db: Session = Depends(get_db)):
    """
    Check account balance
    URL: /atm/balance/{account}/{pin}
    """
    atm = ATMOperations(db)
    result = atm.check_balance(account, pin)
    return result


@app.get("/atm/transactions/{account}/{pin}")
def get_transaction_history(account: int, pin: int, db: Session = Depends(get_db)):
    """
    Get all transactions for account
    URL: /atm/transactions/{account}/{pin}
    """
    atm = ATMOperations(db)
    result = atm.get_transactions(account, pin)
    return result 