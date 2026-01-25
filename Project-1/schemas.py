from pydantic import BaseModel, Field

class Bankdata(BaseModel):
    account : int = Field(..., ge=10000, description="Account number must be at least 5 digits")
    name : str
    pin : int = Field(..., ge=1000, description="PIN must be at least 4 digits")
    bank_name : str = Field(..., max_length=100)
    balance : float
    address : str
