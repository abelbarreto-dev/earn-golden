import pytest

from fastapi.testclient import TestClient

from typing import Generator

from app import app


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as earn_golden:
        yield earn_golden
