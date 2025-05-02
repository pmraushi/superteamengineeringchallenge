import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.session import SessionLocal
from app.db.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[SessionLocal] = override_get_db

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

def test_register_and_login(client):
    # Register
    response = client.post("/api/v1/auth/register", json={"username": "tunzaauser", "password": "tunzaapass"})
    assert response.status_code == 200
    assert response.json()["username"] == "tunzaauser"

    # Login
    response = client.post("/api/v1/auth/login", data={"username": "tunzaauser", "password": "tunzaapass"})
    assert response.status_code == 200
    assert "access_token" in response.json()