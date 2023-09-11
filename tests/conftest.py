from typing import Generator, Type

import pytest

from fastapi.testclient import TestClient

from sqlalchemy.orm import SessionTransaction

from app import app

from src.database.connection import get_session

from src.utils.validators import Validator


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as earn_golden:
        yield earn_golden


@pytest.fixture(scope="function")
def session() -> Generator[SessionTransaction, None, None]:
    with get_session().begin() as db_session:
        yield db_session


@pytest.fixture(scope="class")
def validator() -> Generator[Type[Validator], None, None]:
    yield Validator
