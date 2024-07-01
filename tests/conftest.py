import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_reg


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    table_reg.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_reg.metadata.drop_all(engine)
