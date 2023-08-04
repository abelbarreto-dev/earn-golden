from pydantic import BaseModel
from typing import Optional
from datetime import date


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
