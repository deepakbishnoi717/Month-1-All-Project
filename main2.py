
from fastapi import FastAPI ,Depends
from database import Sessionlocal,engine
from database_moduls import Base, Data
from sqlalchemy.orm import Session
from pydanticmodul2 import DataCreate

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()

    try :
        yield db
    finally :
        db.close()


@app.post("/add_data")
def add_data(item : DataCreate, db: Session = Depends(get_db)):
    new_data = Data(
        name=item.name,
        age=item.age
    )
    
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.get("/get_data")
def get_data(db : Session = Depends(get_db)) :
    all_data = db.query(Data).all() 
    return all_data

@app.get("/get_data/{id}")
def get_data(id:int,db : Session = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    return data

@app.put("/update_data/{id}")
def put_data(id :int ,db :Session = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id ).first()
    return data

@app.delete("/delete_data/{id}")
def delete_data(id:int,db : Session = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if data is None :
        return {"massage":"data not found!"}
    
    db.delete(data)
    db.commit()
    return {"Massage":"data deleted!"}