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
    CPF = "cpf"
    CNPJ ="cnpj"
    EMAIL = "email"
    MOBILE = "mobile"
    RANDOMIC = "randomic"


class MoneyOperator(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class CheckRegex(Enum):
    EMAIL = r"^[a-z]{1}[a-z._0-9]+[a-z0-9]@[a-z]{1}[a-z.]+[a-z]{1}$"
    USERNAME = r"^[a-z_]+[a-z_.0-9]+[a-z0-9_]{1}$"
    MONEY = r"^[0-9]+(?:\.[0-9]{2})?$"
    PERCENT = r"^[0-9]+.[0-9]{1,}$"
    CARD_NUMBER = r"^[0-9]{16}$"
    CARD_DATE = r"^[0-9]{4}\-[0-9]{2}$"
