from sqlalchemy.orm import Session
import models
import schemas
from fastapi import FastAPI,Depends


def create_user(db: Session, student: schemas.UserCreate):
    db_student = models.User(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students(db: Session):
    return db.query(models.User).all()