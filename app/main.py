# API Request → FastAPI → Saved Model → Prediction → JSON Response
import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from app.schemas import EmployeeData

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="Predict employee attrition using a trained machine learning model.",
    version="1.0.0",
)

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "employee_attrition_model.joblib"
METADATA_PATH = BASE_DIR / "models" / "model_metadata.json"

# Load the trained model and metadata at startup
try:
    model = joblib.load(MODEL_PATH)
except Exception as exc:
    raise RuntimeError(f"Could not load the trained model from {MODEL_PATH}") from exc

try:
    with open(METADATA_PATH, "r", encoding="utf-8") as file:
        metadata = json.load(file)
        EXPECTED_FEATURES = metadata["input_features"]
except (OSError, ValueError, KeyError) as exc:
    raise RuntimeError(f"Could not load model metadata from {METADATA_PATH}") from exc


@app.get("/")
def home():
    return {
        "message": "Welcome to the Employee Attrition Prediction API!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


@app.post("/predict")
def predict_attrition(employee: EmployeeData):
    # Convert validated request data into a dictionary
    employee_data = employee.model_dump()

    # Validate the input columns against metadata
    received_features = set(employee_data.keys())
    expected_feature_set = set(EXPECTED_FEATURES)

    missing_features = expected_feature_set - received_features
    extra_features = received_features - expected_feature_set

    if missing_features or extra_features:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Input features do not match model requirements.",
                "missing_features": sorted(missing_features),
                "unexpected_features": sorted(extra_features),
            },
        )

    # Convert input data into a DataFrame with exact column ordering
    employee_df = pd.DataFrame([employee_data], columns=EXPECTED_FEATURES)

    # Make prediction
    try:
        prediction = int(model.predict(employee_df)[0])
        probability = float(model.predict_proba(employee_df)[0][1])
    except Exception as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Prediction failed due to invalid input values: {exc}",
        ) from exc

    # Return JSON response
    return {
        "prediction": prediction,
        "prediction_label": (
            "Employee may leave" if prediction == 1 else "Employee may stay"
        ),
        "attrition_probability": round(probability, 4),
    }
