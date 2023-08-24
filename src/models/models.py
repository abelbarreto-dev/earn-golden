from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

from src.utils.enums import (
    BankAccountType,
    CardType,
    PixType,
    MoneyOperator,
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


class Invoice(BaseModel):
    total_invoice: Decimal
    installments: int
    installments_value: Decimal
    close_date: date
    payment_date: date
    card_id: Optional[int] = None


class Pix(BaseModel):
    pix_key_type: PixType
    pix_key: str
    bank_account_id: Optional[int] = None


class TransferPix(BaseModel):
    send_pix_type: PixType
    receiver_pix_type: PixType
    is_yours: bool = False
    send_pix_key: str
    receiver_pix_key: str
    balance: Decimal
    account_id: Optional[int] = None


class TransferPixAccounts(BaseModel):
    id_pix_sender: int
    id_pix_receiver: Optional[int] = None


class MoneyBox(BaseModel):
    name: str
    description: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    objective: Optional[Decimal] = None
    balance: Decimal


class TransferMoneyBox(BaseModel):
    money_operator: MoneyOperator
    balance: Decimal
    money_box_id: Optional[int] = None


class Signatures(BaseModel):
    name: str
    descript: str
    due_date: date
    value: Decimal
    account_id: Optional[int] = None


class Payment(BaseModel):
    name: str
    descript: str
    value_to_pay: Decimal
    is_paid: bool = False
    account_id: Optional[int] = None


class Deposit(BaseModel):
    balance: Decimal
    bank_account_id: int
    descript: Optional[str] = None
