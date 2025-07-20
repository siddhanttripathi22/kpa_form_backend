from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.bogie import BogieChecksheetCreate
from app.crud import bogie
from app.utils.response import standard_response
from app.schemas.bogie import BogieChecksheetOut
from typing import Optional
from fastapi import Query
import datetime
import traceback

router = APIRouter(prefix="/api/forms/bogie-checksheet", tags=["Bogie"])



@router.post("/", response_model=dict)
def create_bogie_form(form: BogieChecksheetCreate, db: Session = Depends(get_db)):
    try:
        result = bogie.create_bogie_checksheet(db, form)

       
        validated_result = BogieChecksheetOut.model_validate(result)

        return standard_response(True, "Bogie checksheet submitted successfully.", validated_result)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
def get_filtered_bogie_forms(
    formNumber: Optional[str] = Query(None),
    inspectionBy: Optional[str] = Query(None),
    inspectionDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    filters = {"formNumber": formNumber, "inspectionBy": inspectionBy}
    if inspectionDate:
        try:
            filters["inspectionDate"] = datetime.datetime.strptime(inspectionDate, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    forms = bogie.get_filtered_bogie_checksheet(db, filters)
    result = [BogieChecksheetOut.model_validate(f) for f in forms]
    return standard_response(True, "Filtered bogie checksheet forms fetched successfully.", result)

