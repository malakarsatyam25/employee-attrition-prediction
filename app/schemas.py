import json
from pathlib import Path

from pydantic import ConfigDict, create_model

BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_PATH = BASE_DIR / "models" / "model_metadata.json"

with open(METADATA_PATH, "r", encoding="utf-8") as file:
    metadata = json.load(file)

feature_names = metadata["input_features"]

# Categorical features in the employee attrition dataset
categorical_features = {
    "BusinessTravel",
    "Department",
    "EducationField",
    "Gender",
    "JobRole",
    "MaritalStatus",
    "OverTime",
}

# Create a field with the appropriate data type
employee_fields = {}

for feature in feature_names:
    if feature in categorical_features:
        employee_fields[feature] = (str, ...)
    else:
        employee_fields[feature] = (int, ...)

# Create the request schema dynamically
EmployeeData = create_model(
    "EmployeeData",
    __config__=ConfigDict(extra="forbid", strict=True),
    **employee_fields
)