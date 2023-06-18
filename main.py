from fastapi import FastAPI
from routes.mock import mock_router
from config.database import engine, Base

app = FastAPI()
app.include_router(mock_router)
Base.metadata.create_all(bind=engine)
