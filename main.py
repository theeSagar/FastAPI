from fastapi import FastAPI , HTTPException,Path,Depends # imported fastAPI
import json
import models
from database import engine,SessionLocal
import models
import schemas
import crud
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app=FastAPI() # made an object of the same.

@app.get("/home") # created route with the help of the decorators.

def myFirst(): # created a func
    return {"status":True,
            "message":"My first GET api in fastAPI."}

@app.get("/about")

def mySecond():
    return {"status":True,
            "message":"This will be all about the fastAPI."}

def load_data():
    with open('dummyData.json','r') as f:
        data=json.load(f)
        # print("_________",data)
    
    return data

@app.get("/dummyData")

def view():
    data=load_data()

    return {"status":True,"data":data}

@app.get("/stuName/{name_id}")
def view(name_id:int=Path(...,description="ID is required." ,example="1,2,3")): # ... means required.

        data=load_data()
        for i in data:
            if i["id"]==name_id:
                return {"status":True,"data":i}
            
        raise HTTPException (status_code=400, detail="Invalid ID")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students")
def create_student(student: schemas.UserCreate, db: Session = Depends(get_db)):
    crud.create_user(db, student)
    raise HTTPException(status_code=201,detail="Student created 👍.")


@app.get("/students", response_model=list[schemas.UserOut])
def read_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

