from datetime import date

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def auth_headers(email: str = "test@example.com", password: str = "secret123"):
    register = client.post(
        "/auth/register",
        json={"email": email, "password": password, "full_name": "Test User"},
    )
    if register.status_code not in (201, 400):
        raise AssertionError(register.text)

    login = client.post("/auth/login", data={"username": email, "password": password})
    assert login.status_code == 200
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_food_and_entry_flow():
    headers = auth_headers()

    food_resp = client.post(
        "/foods",
        headers=headers,
        json={
            "name": "Chicken Breast",
            "brand": "Generic",
            "serving_size": 100,
            "serving_unit": "g",
            "calories": 165,
            "protein": 31,
            "carbs": 0,
            "fat": 3.6,
        },
    )
    assert food_resp.status_code == 201
    food_id = food_resp.json()["id"]

    today = str(date.today())
    entry_resp = client.post(
        "/entries",
        headers=headers,
        json={"food_id": food_id, "meal_type": "lunch", "servings": 1.5, "consumed_date": today},
    )
    assert entry_resp.status_code == 201

    summary_resp = client.get(f"/entries/daily-summary?consumed_date={today}", headers=headers)
    assert summary_resp.status_code == 200
    summary = summary_resp.json()
    assert summary["calories"] == 247.5
    assert summary["protein"] == 46.5
