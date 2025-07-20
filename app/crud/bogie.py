from sqlalchemy.orm import Session
from app.models.bogie import BogieChecksheet
from app.schemas.bogie import BogieChecksheetCreate

def create_bogie_checksheet(db: Session, sheet: BogieChecksheetCreate):
    db_sheet = BogieChecksheet(**sheet.dict())
    db.add(db_sheet)
    db.commit()
    db.refresh(db_sheet)
    return db_sheet
def get_filtered_bogie_checksheet(db: Session, filters: dict):
    query = db.query(BogieChecksheet)
    if filters.get("formNumber"):
        query = query.filter(BogieChecksheet.formNumber == filters["formNumber"])
    if filters.get("inspectionBy"):
        query = query.filter(BogieChecksheet.inspectionBy == filters["inspectionBy"])
    if filters.get("inspectionDate"):
        query = query.filter(BogieChecksheet.inspectionDate == filters["inspectionDate"])
    return query.all()
