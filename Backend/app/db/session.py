from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL="postgresql://Expense_owner:npg_S6TYZGPioHp4@ep-restless-resonance-a58g00kt-pooler.us-east-2.aws.neon.tech/Expense?sslmode=require"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)