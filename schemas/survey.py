from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SurveyBase(BaseModel):
    name: str
    email: str
    age: Optional[str]
    profession: Optional[str]
    style: Optional[str]
    brand: Optional[str]
    hobbies: Optional[str]
    monthly_budget: Optional[str]
    clothing_type: Optional[str]
    suggestions: Optional[str]

class SurveyCreate(SurveyBase):
    pass

class SurveyResponse(SurveyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
