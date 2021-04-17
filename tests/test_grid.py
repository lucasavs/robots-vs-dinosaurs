from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_not_retrieving_invalid_grid():
    response = client.get("/grid/123")
    assert response.status_code == 404


def test_create_grid():
    response = client.post("/grid/create/")
    assert response.status_code == 200

    body = json.loads(response.text)
    new_response = client.get("/grid/" + str(body["grid_id"]))
    assert new_response.status_code == 200
