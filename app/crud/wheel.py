from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.wheel import WheelSpecification
from app.schemas.wheel import WheelSpecificationCreate

def create_wheel_spec(db: Session, spec: WheelSpecificationCreate):
    existing = db.query(WheelSpecification).filter(WheelSpecification.formNumber == spec.formNumber).first()
    if existing:
        raise HTTPException(status_code=409, detail=f"Form with formNumber '{spec.formNumber}' already exists.")

    db_spec = WheelSpecification(**spec.dict())
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_filtered_wheel_specs(db: Session, filters: dict):
    query = db.query(WheelSpecification)
    if filters.get("formNumber"):
        query = query.filter(WheelSpecification.formNumber == filters["formNumber"])
    if filters.get("submittedBy"):
        query = query.filter(WheelSpecification.submittedBy == filters["submittedBy"])
    if filters.get("submittedDate"):
        query = query.filter(WheelSpecification.submittedDate == filters["submittedDate"])
    return query.all()
