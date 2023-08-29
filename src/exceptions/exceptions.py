class EmailException(ValueError):
    def __init__(self):
        super().__init__("email format is not valid")


class UsernameException(ValueError):
    def __init__(self):
        super().__init__("username format is not valid")


class MoneyException(ValueError):
    def __init__(self):
        super().__init__("money format is not valid")


class PercentException(ValueError):
    def __init__(self, name: str = "percentage"):
        super().__init__(f"{name} format is not valid")


class DateException(ValueError):
    def __init__(self, date: str = "date"):
        super().__init__(f"{date} format is not valid")


class DueDateException(ValueError):
    def __init__(self, name: str = "due date card"):
        super().__init__(f"{name} format is not valid")


class NumberCardException(ValueError):
    def __init__(self):
        super().__init__("number card is not valid")


class AgencyNumberException(ValueError):
    def __init__(self):
        super().__init__("bank agency number is not valid")


class SavingNumberException(ValueError):
    def __init__(self):
        super().__init__("saving account number is not valid")


class CheckingNumberException(ValueError):
    def __init__(self):
        super().__init__("checking account number is not valid")


class CPFException(ValueError):
    def __init__(self, message: str = "message"):
        super().__init__(message)


class CNPJException(ValueError):
    def __init__(self, message: str = "message"):
        super().__init__(message)


class MobilePhoneException(ValueError):
    def __init__(self):
        super().__init__("mobile phone number is not valid")
