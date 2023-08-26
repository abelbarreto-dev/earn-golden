class EmailException(ValueError):
    def __init__(self):
        super().__init__("email format is not valid")


class UsernameException(ValueError):
    def __init__(self):
        super().__init__("username format is not valid")
