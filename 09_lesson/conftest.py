import pytest
from db import engine, SessionLocal
from models import Base


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)
