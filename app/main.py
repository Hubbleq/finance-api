from app.routers import accounts, transactions, categories, auth
from app.database import create_db_and_tables
from app.routers import accounts, transactions, categories, reports
from app.routers import reports
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código executado antes da aplicação "subir" (startup)
    create_db_and_tables()
    yield
    # Código executado no shutdown, se necessário

app = FastAPI(title="Finance API", lifespan=lifespan)

# inclui suas rotas normalmente



app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(categories.router)
app.include_router(auth.router)
app.include_router(reports.router)

@app.get("/")
def read_root():
    return {"message": "Finance API is running"}

