from sqlalchemy import Column, String, Date, JSON
from app.database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    formNumber = Column(String, primary_key=True, index=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    bogieDetails = Column(JSON)
    bogieChecksheet = Column(JSON)
    bmbcChecksheet = Column(JSON)
    status = Column(String, default="Saved")
