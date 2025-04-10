from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from fastapi.middleware.cors import CORSMiddleware

# Import your routers here when available
# from app.api.routes import user, expense, budget, report

app = FastAPI(title="Expense Tracker API")
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers here in the future
# app.include_router(user.router, prefix="/users", tags=["Users"])
# app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])
# app.include_router(budget.router, prefix="/budgets", tags=["Budgets"])
# app.include_router(report.router, prefix="/reports", tags=["Reports"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}
