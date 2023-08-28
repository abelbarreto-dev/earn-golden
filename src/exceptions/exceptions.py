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
