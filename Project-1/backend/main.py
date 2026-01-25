from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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
    # Check if account already exists
    existing_account = db.query(BankModul).filter(BankModul.account == item.account).first()
    if existing_account:
        raise HTTPException(status_code=400, detail="Account number already exists. Please choose a different one.")

    new_data = BankModul(
        account = item.account,
        name = item.name,
        pin = item.pin,
        bank_name = item.bank_name,
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
        data.bank_name = item.bank_name
        data.address = item.address
        data.balance = item.balance
        db.commit()
        db.refresh(data)
    return data


# ================ ATM ENDPOINTS ================

@app.post("/atm/withdraw")
def withdraw(account: int, pin: int, amount: float, db: Session = Depends(get_db)):
    atm = ATMOperations(db)
    result = atm.withdraw(account, pin, amount)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result

@app.post("/atm/deposit")
def deposit(account: int, pin: int, amount: float, db: Session = Depends(get_db)):
    atm = ATMOperations(db)
    result = atm.deposit(account, pin, amount)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result

@app.get("/atm/balance/{account}/{pin}")
def check_balance(account: int, pin: int, db: Session = Depends(get_db)):
    atm = ATMOperations(db)
    result = atm.check_balance(account, pin)
    if not result.get("success"):
        raise HTTPException(status_code=401, detail=result.get("error"))
    return result

@app.get("/atm/transactions/{account}/{pin}")
def get_transaction_history(account: int, pin: int, db: Session = Depends(get_db)):
    atm = ATMOperations(db)
    result = atm.get_transactions(account, pin)
    if not result.get("success"):
        raise HTTPException(status_code=401, detail=result.get("error"))
    return result


# ================ SERVE FRONTEND ================

# Get the path to the frontend directory
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")

@app.get("/")
async def serve_spa():
    """Serve the main index.html file"""
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Mount subdirectories for assets and js
app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIR, "assets")), name="assets")
app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")
