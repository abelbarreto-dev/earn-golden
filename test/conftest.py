import pytest

from fastapi.testclient import TestClient

from typing import Generator

from app import app

from src.database.connection import get_session

from sqlalchemy.orm import SessionTransaction


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as earn_golden:
        yield earn_golden


@pytest.fixture(scope="function")
def session() -> Generator[SessionTransaction, None, None]:
    with get_session().begin() as db_session:
        yield db_session
