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
    AGENCY = r"^[0-9]{4}(?:[0-9]{1})?$"
    CHECKING = "^[0-9]{9}(?:[0-9]{1})?$"
    SAVING = "^[0-9]{5}(?:[0-9]{1})?$"
    CPF = "^[0-9]{11}$"
    CNPJ = r"^[0-9]{14}$"
    MOBILE = r"^55[0-9]{2}9[0-9]{4}[0-9]{4}$"
    UUID = r"^[a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12}$"
    MONEY_COMMON = r"^[0-9]+[.,][0-9]+$"
