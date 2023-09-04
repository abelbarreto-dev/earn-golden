from abc import ABC

from sqlalchemy.orm import Session

from src.database.connection import get_session


class Repository(ABC):
    @property
    def session(self) -> Session:
        with get_session() as new_db:
            return new_db
