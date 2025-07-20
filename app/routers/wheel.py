from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.wheel import WheelSpecificationCreate, WheelSpecificationOut
from app.crud import wheel
from app.utils.response import standard_response
from typing import Optional
import datetime

router = APIRouter(prefix="/api/forms/wheel-specifications", tags=["Wheel"])

@router.post("/", response_model=dict)
def create_wheel_form(form: WheelSpecificationCreate, db: Session = Depends(get_db)):
    try:
        result = wheel.create_wheel_spec(db, form)
        pydantic_result = WheelSpecificationOut.model_validate(result)
        return standard_response(True, "Wheel specification submitted successfully.", pydantic_result)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=dict)
def get_filtered_forms(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    filters = {"formNumber": formNumber, "submittedBy": submittedBy}

    if submittedDate:
        try:
            filters["submittedDate"] = datetime.datetime.strptime(submittedDate, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    try:
        forms = wheel.get_filtered_wheel_specs(db, filters)
        result_out = [WheelSpecificationOut.model_validate(f) for f in forms]
        return standard_response(True, "Filtered wheel specification forms fetched successfully.", result_out)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
