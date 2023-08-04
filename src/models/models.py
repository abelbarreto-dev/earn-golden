from pydantic import BaseModel
from datetime import date


class Account(BaseModel):
    name: str
    cpf: str
    birth_date: date
    username: str
    email: str
    password: str
    mobile: str
