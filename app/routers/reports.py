from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from sqlalchemy import func
from pydantic import BaseModel

from app.database import get_session
from app.models import Transaction

router = APIRouter(prefix="/reports", tags=["Reports"])

class SummaryReport(BaseModel):
    total_income: float
    total_expenses: float
    balance: float

@router.get(
    "/summary",
    response_model=SummaryReport,
    summary="Financial summary",
    description="Returns total income, total expenses and balance."
)
def get_summary(session: Session = Depends(get_session)):
    total_income = session.exec(
        select(func.sum(Transaction.amount)).where(Transaction.type == "income")
    ).one() or 0

    total_expenses = session.exec(
        select(func.sum(Transaction.amount)).where(Transaction.type == "expense")
    ).one() or 0

    balance = total_income - total_expenses

    return SummaryReport(
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance
    )
