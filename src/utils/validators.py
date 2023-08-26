from re import match

from src.utils.enums import CheckRegex


class Validator:
    @classmethod
    def check_email(cls, email: str) -> None:
        if not match(CheckRegex.EMAIL.value, email):
            pass

    @classmethod
    def check_username(cls, username: str):
        if not match(CheckRegex.USERNAME.value, username):
            pass
