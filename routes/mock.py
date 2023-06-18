from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.create_mock_input import CreateInput

mock_router = APIRouter()

mocks = []


@mock_router.post("/mock")
def create(input: CreateInput):
    mocks.append(input)
    return JSONResponse(status_code=201, content={"message": "Mock creado con éxito"})


@mock_router.get("/mock")
def get_all():
    return JSONResponse(status_code=200, content=jsonable_encoder(mocks))
