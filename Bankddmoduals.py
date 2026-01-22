from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, Session
from datetime import datetime

Baseb = declarative_base()

class BankModul(Baseb) :

    __tablename__ = "bankdata"

    account = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    pin = Column(Integer)
    bank = Column(String)
    address = Column(String)
    balance = Column(Float)


class Transaction(Baseb) :

    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account_id = Column(Integer, index=True)
    transaction_type = Column(String)  # "debit" or "credit"
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    balance_after = Column(Float)


class ATMOperations :
    
    def __init__(self, db: Session):
        self.db = db

    def verify_pin(self, account: int, pin: int) -> bool:
        """
        Verify if PIN matches the account PIN
        Returns True if PIN is correct, False otherwise
        """
        user = self.db.query(BankModul).filter(BankModul.account == account).first()
        if user and user.pin == pin:
            return True
        return False

    def check_balance(self, account: int, pin: int) -> dict:
        """
        Check account balance after verifying PIN
        Returns balance or error message
        """
        if not self.verify_pin(account, pin):
            return {"error": "Invalid PIN", "success": False}
        
        user = self.db.query(BankModul).filter(BankModul.account == account).first()
        if user:
            return {"balance": user.balance, "success": True}
        return {"error": "Account not found", "success": False}

    def withdraw(self, account: int, pin: int, amount: float) -> dict:
        """
        Withdraw money from account
        Checks PIN, balance, and amount validity
        Returns success/error message with new balance
        """
        # Verify PIN
        if not self.verify_pin(account, pin):
            return {"error": "Invalid PIN", "success": False}

        # Check if amount is valid
        if amount <= 0:
            return {"error": "Amount must be greater than 0", "success": False}

        # Get user and check balance
        user = self.db.query(BankModul).filter(BankModul.account == account).first()
        if not user:
            return {"error": "Account not found", "success": False}

        if user.balance < amount:
            return {"error": "Insufficient balance", "success": False, "current_balance": user.balance}

        # Perform withdrawal
        user.balance -= amount
        self.db.commit()
        self.db.refresh(user)

        # Create transaction record
        self.create_transaction(account, "debit", amount, user.balance)

        return {
            "success": True,
            "message": f"Successfully withdrew ${amount}",
            "new_balance": user.balance
        }

    def deposit(self, account: int, pin: int, amount: float) -> dict:
        """
        Deposit money into account
        Checks PIN and amount validity
        Returns success/error message with new balance
        """
        # Verify PIN
        if not self.verify_pin(account, pin):
            return {"error": "Invalid PIN", "success": False}

        # Check if amount is valid
        if amount <= 0:
            return {"error": "Amount must be greater than 0", "success": False}

        # Get user
        user = self.db.query(BankModul).filter(BankModul.account == account).first()
        if not user:
            return {"error": "Account not found", "success": False}

        # Perform deposit
        user.balance += amount
        self.db.commit()
        self.db.refresh(user)

        # Create transaction record
        self.create_transaction(account, "credit", amount, user.balance)

        return {
            "success": True,
            "message": f"Successfully deposited ${amount}",
            "new_balance": user.balance
        }

    def get_transactions(self, account: int, pin: int) -> dict:
        """
        Get transaction history for account
        Returns list of all transactions
        """
        # Verify PIN
        if not self.verify_pin(account, pin):
            return {"error": "Invalid PIN", "success": False}

        # Check if account exists
        user = self.db.query(BankModul).filter(BankModul.account == account).first()
        if not user:
            return {"error": "Account not found", "success": False}

        # Get all transactions for this account
        transactions = self.db.query(Transaction).filter(
            Transaction.account_id == account
        ).all()

        transaction_list = []
        for trans in transactions:
            transaction_list.append({
                "transaction_id": trans.transaction_id,
                "type": trans.transaction_type,
                "amount": trans.amount,
                "timestamp": trans.timestamp,
                "balance_after": trans.balance_after
            })

        return {
            "success": True,
            "account": account,
            "transactions": transaction_list
        }

    def create_transaction(self, account: int, transaction_type: str, amount: float, balance_after: float):
        """
        Create and save a transaction record
        Called after each withdrawal or deposit
        """
        new_transaction = Transaction(
            account_id=account,
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after
        )
        self.db.add(new_transaction)
        self.db.commit()


    