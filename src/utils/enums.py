from enum import Enum


class BankAccountType(Enum):
    SAVING = "saving"
    PAYMENT = "payment"
    CHECKING = "checking"


class CardType(Enum):
    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"
