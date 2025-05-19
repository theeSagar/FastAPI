from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    language = Column(String, unique=False, index=True)
    bio = Column(String, unique=False, index=True)
    version=Column(Integer,nullable=True)

