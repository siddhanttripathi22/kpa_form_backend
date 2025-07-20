from fastapi import FastAPI
from app.routers import wheel, bogie
from app.database import engine, Base

app = FastAPI(
    title="KPA Form Backend API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(wheel.router)
app.include_router(bogie.router)
