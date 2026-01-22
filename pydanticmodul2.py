from pydantic import BaseModel

class DataCreate(BaseModel):
    name : str
    age : int

