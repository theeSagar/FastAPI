from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    language: str
    bio: str
    version: Optional[int] = None
  # Use Optional if the field can be None (nullable)

