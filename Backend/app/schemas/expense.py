from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    date: date
    description: Optional[str] = None

class ExpenseOut(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True