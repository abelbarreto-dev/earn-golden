from re import match

from src.utils.enums import CheckRegex


class Validator:
    @classmethod
    def check_email(cls, email: str) -> None:
        if not match(CheckRegex.EMAIL.value, email):
            pass
