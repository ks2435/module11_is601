import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from calculation_model import Calculation
from calculation_factory import calculate
from calculation_schemas import OperationType

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/calc_db")

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_calculation(db):
    result = calculate(10, 5, OperationType.add)
    calc = Calculation(a=10, b=5, type="add", result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    assert calc.id is not None
    assert calc.result == 15

def test_divide_calculation(db):
    result = calculate(10, 2, OperationType.divide)
    calc = Calculation(a=10, b=2, type="divide", result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    assert calc.result == 5

def test_invalid_divide_by_zero(db):
    with pytest.raises(ValueError):
        calculate(10, 0, OperationType.divide)

def test_multiply_calculation(db):
    result = calculate(4, 5, OperationType.multiply)
    calc = Calculation(a=4, b=5, type="multiply", result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    assert calc.result == 20