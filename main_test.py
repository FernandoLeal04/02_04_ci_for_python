import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_data():
    with open("data.json", "r") as f:
        expected_data = json.load(f)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected_data

def test_read_data_by_guid():
    with open("data.json", "r") as f:
        data = json.load(f)
    guid = data[0]["guid"]
    response = client.get(f"/{guid}")
    assert response.status_code == 200
    assert response.json() == data[0]

def test_read_data_by_invalid_guid():
    response = client.get("/invalid-guid")
    assert response.status_code == 404
