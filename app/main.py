from fastapi import FastAPI
from app.routers import accounts, transactions, categories
from app.database import create_db_and_tables
from app.routers import accounts, transactions, categories, reports
from app.routers import reports


app = FastAPI(title="Finance API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(categories.router)
app.include_router(reports.router)
app.include_router(reports.router)

@app.get("/")
def read_root():
    return {"message": "Finance API is running"}

