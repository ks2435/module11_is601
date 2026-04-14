from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum

class OperationType(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

class CalculationCreate(BaseModel):
    a: float
    b: float
    type: OperationType
    user_id: Optional[int] = None

    @field_validator("b")
    @classmethod
    def no_zero_division(cls, b, info):
        if "type" in info.data and info.data["type"] == OperationType.divide and b == 0:
            raise ValueError("Cannot divide by zero")
        return b

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: float
    user_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True