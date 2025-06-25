from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    balance: float = 0.0

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    amount: float
    date: datetime
    account_id: int = Field(foreign_key="account.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    type: str  # 'income' or 'expense'
