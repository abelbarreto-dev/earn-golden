from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

from src.utils.enums import BankAccountType


class Account(BaseModel):
    name: str
    cpf: str
    birth_date: date
    username: str
    email: str
    password: str
    mobile: str


class Bank(BaseModel):
    name: str
    code: str
    agency: str
    account_id: Optional[int] = None


class BankAccount:
    variation: int = 0
    number: str
    type_account: BankAccountType
    balance: Decimal
    bank_id: Optional[int] = None
