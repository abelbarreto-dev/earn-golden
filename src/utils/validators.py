from re import match

from decimal import Decimal

from src.utils.enums import CheckRegex

from src.exceptions.exceptions import (
    EmailException,
    UsernameException,
    MoneyException,
    PercentException,
    DateException,
    DueDateException,
    NumberCardException,
)


class Validator:
    @classmethod
    def check_email(cls, email: str) -> None:
        if not match(CheckRegex.EMAIL.value, email):
            raise EmailException()

    @classmethod
    def check_username(cls, username: str) -> None:
        if not match(CheckRegex.USERNAME.value, username):
            raise UsernameException()

    @classmethod
    def check_money(cls, money: Decimal) -> None:
        if not match(CheckRegex.MONEY.value, str(money)):
            raise MoneyException()

    @classmethod
    def check_percent(cls, percent: Decimal, name: str = "percentage") -> None:
        if not match(CheckRegex.PERCENT.value, str(percent)):
            raise PercentException(name)
