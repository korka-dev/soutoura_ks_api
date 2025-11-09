from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class CustomerSurvey(Base):
    __tablename__ = "customer_surveys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(String, nullable=True)
    profession = Column(String, nullable=True)
    style = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    hobbies = Column(String, nullable=True)
    monthly_budget = Column(String, nullable=True)
    clothing_type = Column(String, nullable=True)
    suggestions = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
