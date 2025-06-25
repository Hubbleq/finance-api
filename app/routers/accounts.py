from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List
from sqlmodel import Session, select
from app.database import get_session
from app.models import Account
from fastapi import Body

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post(
    "/",
    response_model=Account,
    status_code=201,
    summary="Create a new account",
    description="Creates a new account with name and initial balance."
)
def create_account(
    account: Account,
    session: Session = Depends(get_session)
):
    session.add(account)
    session.commit()
    session.refresh(account)
    return account

@router.get(
    "/",
    response_model=List[Account],
    status_code=200,
    summary="List all accounts",
    description="Returns a list of all accounts."
)
def list_accounts(
    session: Session = Depends(get_session)
):
    accounts = session.exec(select(Account)).all()
    return accounts

@router.get(
    "/{account_id}",
    response_model=Account,
    status_code=200,
    summary="Get an account by ID",
    description="Retrieve an account by its ID."
)
def get_account(
    account_id: int,
    session: Session = Depends(get_session)
):
    account = session.get(Account, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.delete(
    "/{account_id}",
    status_code=204,
    summary="Delete an account",
    description="Remove an account by its ID."
)
def delete_account(
    account_id: int,
    session: Session = Depends(get_session)
):
    account = session.get(Account, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    session.delete(account)
    session.commit()
    return Response(status_code=204)

@router.post(
    "/{account_id}/deposit",
    status_code=200,
    summary="Deposit to an account",
    description="Deposit a specified amount to an account."
)
def deposit_to_account(
    account_id: int,
    amount: float = Body(..., gt=0, description="Amount to deposit, must be positive"),
    session: Session = Depends(get_session)
):
    account = session.get(Account, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")
    
    account.balance += amount
    session.commit()
    session.refresh(account)
    return account
    
