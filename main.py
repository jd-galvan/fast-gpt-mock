from fastapi import FastAPI
from routes.mock import mock_router
from config.database import engine, Base

app = FastAPI()
app.title = "Fast GPT Mock"
app.version = "0.0.1"

app.include_router(mock_router)
Base.metadata.create_all(bind=engine)
