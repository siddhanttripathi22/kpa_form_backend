from pydantic import BaseModel
from datetime import date
from typing import Dict

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecificationOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]
    status: str

    class Config:
        from_attributes = True
