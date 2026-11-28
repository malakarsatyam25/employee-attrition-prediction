
import json
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_PATH = BASE_DIR / "models" / "model_metadata.json"

with open(METADATA_PATH, "r", encoding="utf-8") as file:
    metadata = json.load(file)

FEATURES = metadata["input_features"]

CATEGORICAL_FEATURES = {
    "BusinessTravel",
    "Department",
    "EducationField",
    "Gender",
    "JobRole",
    "MaritalStatus",
    "OverTime",
}


def create_employee_data():
    """Create sample input containing every required feature."""
    employee = {}

    for feature in FEATURES:
        if feature in CATEGORICAL_FEATURES:
            employee[feature] = "Test"
        else:
            employee[feature] = 30

    return employee


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict_endpoint():
    employee = create_employee_data()

    response = client.post("/predict", json=employee)

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]
    assert response.json()["prediction_label"] in [
        "Employee may stay",
        "Employee may leave",
    ]
    assert 0 <= response.json()["attrition_probability"] <= 1


def test_predict_missing_feature():
    employee = create_employee_data()

    employee.pop(FEATURES[0])

    response = client.post("/predict", json=employee)

    assert response.status_code == 422


def test_predict_unexpected_feature():
    employee = create_employee_data()
    employee["UnexpectedField"] = 123

    response = client.post("/predict", json=employee)

    assert response.status_code == 422
