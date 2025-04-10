from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str