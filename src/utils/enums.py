from enum import Enum


class BankAccountType(Enum):
    SAVING = "saving"
    PAYMENT = "payment"
    CHECKING = "checking"


class CardType(Enum):
    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"


class PixType(Enum):
    CPF = 'cpf'
    CNPJ = 'cnpj'
    EMAIL = 'email'
    MOBILE = 'mobile'
    RANDOMIC = 'randomic'


class MoneyOperator(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
