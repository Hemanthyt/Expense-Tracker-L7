from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)