from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String(20), nullable=False)
    result = Column(Float, nullable=False)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now())