import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base

#conftest.py adalah file khusus pytest untuk menyimpan setup bersama
@pytest.fixture
def db_session():

    engine = create_engine(
        "sqlite:///:memory:"
    )

    Base.metadata.create_all(
        engine
    )

    Session = sessionmaker(
        bind=engine
    )

    session = Session()

    try:
        yield session

    finally:
        session.close()