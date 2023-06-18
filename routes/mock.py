from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.mock import MockInput
from models.mock import Mock as MockModel
from config.database import SessionLocal
from sqlalchemy.orm import Session

mock_router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@mock_router.post("/mock")
def create(input: MockInput, db: Session = Depends(get_db)):
    db.add(MockModel(**input.dict()))
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Mock creado con éxito"})


@mock_router.get("/mock")
def get_all(db: Session = Depends(get_db)):
    mocks = db.query(MockModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(mocks))
