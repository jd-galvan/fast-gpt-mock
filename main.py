from fastapi import FastAPI
from routes.mock import mock_router

app = FastAPI()
app.include_router(mock_router)
