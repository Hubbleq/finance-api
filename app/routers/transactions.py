from typing import Optional, List
from fastapi import APIRouter, Query, Depends
from sqlmodel import Session, select
from datetime import datetime
from app.models import Transaction  # Add this import for Transaction model
from app.database import get_session

router = APIRouter()

@router.get(
    "/",
    response_model=List[Transaction],
    status_code=200,
    summary="List all transactions",
)
def read_transactions(
    session: Session = Depends(get_session),
    account_id: Optional[int] = Query(None),
    type: Optional[str] = Query(None, pattern="^(income|expense)$"),
    date_from: Optional[datetime] = Query(None),
    date_to: Optional[datetime] = Query(None),
):
    query = select(Transaction)
    if account_id is not None:
        query = query.where(Transaction.account_id == account_id)
    if type is not None:
        query = query.where(Transaction.type == type)
    if date_from is not None:
        query = query.where(Transaction.date >= date_from)
    if date_to is not None:
        query = query.where(Transaction.date <= date_to)
    transactions = session.exec(query).all()
    return transactions
