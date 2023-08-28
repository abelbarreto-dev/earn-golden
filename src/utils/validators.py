import datetime
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
    AgencyNumberException,
    CheckingNumberException,
    SavingNumberException,
)

from src.utils.year_month_date import YearMonthDate


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

    @classmethod
    def check_number_card(cls, number_card: str) -> None:
        if not match(CheckRegex.CARD_NUMBER.value, number_card):
            raise NumberCardException()

    @classmethod
    def check_birth_date(cls, birth_date: datetime.date) -> None:
        if not birth_date < datetime.date.today():
            raise DateException("birth date")

    @classmethod
    def check_date_today(cls, today: datetime.date) -> None:
        if today not in (datetime.date.today(), ):
            raise DateException("your date for today")

    @classmethod
    def check_date_future(cls, future: datetime.date) -> None:
        if future <= datetime.date.today():
            raise DateException("future date")

    @classmethod
    def check_card_due_date(cls, due_date: YearMonthDate) -> None:
        if not match(CheckRegex.CARD_DATE.value, str(due_date)):
            raise DueDateException()

    @classmethod
    def check_agency(cls, agency: str) -> None:
        if not match(CheckRegex.AGENCY.value, agency):
            raise AgencyNumberException()

    @classmethod
    def check_account_saving(cls, saving: str) -> None:
        if not match(CheckRegex.SAVING.value, saving):
            raise SavingNumberException()

    @classmethod
    def check_account_checking(cls, checking: str) -> None:
        if not match(CheckRegex.CHECKING.value, checking):
            raise CheckingNumberException()
