from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
from fastapi.testclient import TestClient
from routes.mock import get_db
from main import app

from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Override dependency


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Initialize test client
client = TestClient(app)

# Tests


def test_create(mocker):
    mocker.patch('openai.Completion.create', return_value={
        "choices": [{
            "text": "[{\"nombre\": \"nombre1\"},{\"nombre\":\"nombre2\"}]"
        }]
    })

    response = client.post(
        "/mock", json={"endpoint": "test", "prompt": "test prompt"})

    assert response.status_code == 201


def test_get_all():
    response = client.get("/mock")

    assert response.status_code == 200


def test_get():
    response = client.get("/mock/test")

    assert response.status_code == 200
