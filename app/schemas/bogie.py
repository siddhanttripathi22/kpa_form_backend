from pydantic import BaseModel
from datetime import date
from typing import Dict

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: Dict[str, str]
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]

class BogieChecksheetOut(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: Dict[str, str]
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]
    status: str

    class Config:
      from_attributes = True
