from fastapi import FastAPI
from app.routers import accounts, transactions, categories
from app.database import create_db_and_tables

app = FastAPI(title="Finance API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(categories.router)

@app.get("/")
def read_root():
    return {"message": "Finance API is running"}

