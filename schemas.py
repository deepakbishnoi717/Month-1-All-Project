from pydantic import BaseModel

class Bankdata(BaseModel):
    account : int
    name : str
    pin : int
    bank : str
    balance : float
    address : str
