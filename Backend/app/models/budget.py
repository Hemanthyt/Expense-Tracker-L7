from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.db.base import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    month = Column(String, nullable=False)