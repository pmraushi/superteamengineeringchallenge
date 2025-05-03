import pytest
from fastapi.testclient import TestClient
from app.crud.user import create_user
from app.schemas.user import UserCreate
from app.tests.test_auth import TestingSessionLocal, client

def test_payment_plan_and_savings(client):
    # Setup user
    db = TestingSessionLocal()
    create_user(db, UserCreate(username="tunzaauser", password="tunzaapass"))
    db.close()

    # Login
    login_response = client.post("/api/v1/auth/login", data={"username": "tunzaauser", "password": "tunzaapass"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create payment plan (TZS 20,000)
    response = client.post(
        "/api/v1/payments/plans",
        json={"total_amount": 20000.0},
        headers=headers
    )
    assert response.status_code == 200
    plan_id = response.json()["id"]

    # Add savings (TZS 5,000 x 4)
    for _ in range(4):
        response = client.post(
            f"/api/v1/payments/plans/{plan_id}/savings",
            json={"amount": 5000.0},
            headers=headers
        )
        assert response.status_code == 200

    # Check if target reached
    response = client.post(
        f"/api/v1/payments/plans/{plan_id}/savings",
        json={"amount": 0.0},  # Just to check status
        headers=headers
    )
    assert response.json()["target_reached"] is True