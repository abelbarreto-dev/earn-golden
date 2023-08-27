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
