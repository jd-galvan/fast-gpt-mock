from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.mock import MockInput
from config.database import SessionLocal
from sqlalchemy.orm import Session
from services.mock import MockService

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
    MockService(db).create(input)
    return JSONResponse(status_code=201, content={"message": "Mock creado con éxito"})


@mock_router.get("/mock")
def get_all(db: Session = Depends(get_db)):
    mocks = MockService(db).get_all()
    return JSONResponse(status_code=200, content=jsonable_encoder(mocks))


@mock_router.get("/mock/{endpoint}")
def get(endpoint: str, db: Session = Depends(get_db)):
    mock = MockService(db).get(endpoint)
    return JSONResponse(status_code=200, content=jsonable_encoder(mock))
