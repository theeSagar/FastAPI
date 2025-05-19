from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    language: str
    bio: str
    version: Optional[int] = None
  # Use Optional if the field can be None (nullable)

class UserOut(UserCreate):
    id: int  # DB-generated ID

    class Config:
        orm_mode = True
    
    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy model as a dict
