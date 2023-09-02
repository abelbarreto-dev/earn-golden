from abc import ABC

from src.utils.validators import Validator


class Controller(ABC):
    _validator: Validator = Validator()

    @property
    def validator(self) -> Validator:
        return self._validator
