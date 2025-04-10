from pydantic import BaseModel
from typing import Optional

class BudgetCreate(BaseModel):
    category: str
    amount: float
    month: str

class BudgetOut(BudgetCreate):
    id: int

    class Config:
        orm_mode = True