from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

from src.utils.enums import (
    BankAccountType,
    CardType,
    PixType,
)


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


class BankAccount(BaseModel):
    variation: int = 0
    number: str
    type_account: BankAccountType
    balance: Decimal
    bank_id: Optional[int] = None


class Card(BaseModel):
    name: str
    number: str
    due_date: date
    sec_code: str
    type_card: CardType
    balance: Decimal
    bank_account_id: Optional[int] = None


class Invoice:
    total_invoice: Decimal
    installments: int
    installments_value: Decimal
    close_date: date
    payment_date: date
    card_id: Optional[int] = None


class Pix:
    pix_key_type: PixType
    pix_key: str
    bank_account_id: Optional[int] = None
