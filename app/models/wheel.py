from sqlalchemy import Column, String, Date, JSON
from app.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    formNumber = Column(String, primary_key=True, index=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)
    status = Column(String, default="Saved")
