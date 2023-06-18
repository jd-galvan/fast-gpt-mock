from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
from schemas.mock import MockInput
from config.database import SessionLocal
from sqlalchemy.orm import Session
from services.mock import MockService
from services.gpt import get_response

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
    response = get_response(input.prompt)
    MockService(db).create(input, response)
    return JSONResponse(status_code=201, content={"message": "Mock creado con éxito"})


@mock_router.get("/mock")
def get_all(db: Session = Depends(get_db)):
    mocks = MockService(db).get_all()
    return JSONResponse(status_code=200, content=jsonable_encoder(mocks))


@mock_router.get("/mock/{endpoint}")
def get(endpoint: str, db: Session = Depends(get_db)):
    mock = MockService(db).get(endpoint)
    response = json.loads(mock.response)
    print("hasdsad")
    return JSONResponse(status_code=200, content=jsonable_encoder(response))
