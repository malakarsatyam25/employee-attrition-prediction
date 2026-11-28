# Employee Attrition Prediction

## Project Overview

Employee Attrition Prediction is a Machine Learning project that predicts whether an employee is likely to leave an organization based on various employee-related factors.

Employee attrition is an important business problem because high employee turnover can increase recruitment costs, affect productivity, and create challenges for workforce planning.

This project uses classification algorithms to identify patterns associated with employee attrition and provides predictions through a web application.

The trained model is integrated with FastAPI for prediction requests, and Streamlit provides an interactive user interface.

## Project Objectives

- Analyze employee data to understand factors associated with attrition.
- Preprocess employee data for machine learning.
- Train and evaluate multiple classification algorithms.
- Compare model performance using appropriate evaluation metrics.
- Improve the Random Forest model using hyperparameter tuning.
- Deploy the trained model through a FastAPI application.
- Build an interactive Streamlit interface for making predictions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Scikit-learn | Machine learning, preprocessing, and evaluation |
| RandomizedSearchCV | Hyperparameter tuning |
| Joblib | Saving and loading the trained model |
| FastAPI | Building the prediction API |
| Pydantic | Input data validation |
| Streamlit | Building the interactive user interface |
| Uvicorn | Running the FastAPI application |
| Git and GitHub | Version control and project hosting |

## Machine Learning Workflow

The project follows these steps:

1. **Data Collection:** Load the employee dataset.
2. **Exploratory Data Analysis:** Explore employee characteristics and attrition patterns.
3. **Data Preprocessing:** Handle numerical and categorical features.
4. **Feature Engineering:** Prepare the input features for model training.
5. **Model Training:** Train multiple classification algorithms.
6. **Model Evaluation:** Compare model performance using evaluation metrics.
7. **Hyperparameter Tuning:** Use RandomizedSearchCV to search for suitable Random Forest hyperparameters.
8. **Model Saving:** Save the trained model using Joblib.
9. **API Development:** Create prediction endpoints using FastAPI.
10. **Frontend Development:** Build an interactive application using Streamlit.
11. **Prediction:** Accept employee information and display the model's prediction.

## Algorithms Used

### 1. Logistic Regression

Logistic Regression is a classification algorithm that estimates the probability of an employee belonging to the attrition class.

It provides a useful baseline for comparing model performance.

### 2. Decision Tree

A Decision Tree makes predictions using a series of decision rules based on employee features.

It can capture nonlinear relationships and is relatively easy to visualize and interpret.

### 3. Random Forest

Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees.

It can capture complex relationships in employee data and often generalizes better than a single decision tree.

### 4. Tuned Random Forest

Random Forest hyperparameters were optimized using RandomizedSearchCV.

The selected hyperparameter configuration includes:

- Number of trees (`n_estimators`): 500
- Maximum depth (`max_depth`): 10
- Minimum samples required to split a node (`min_samples_split`): 10
- Minimum samples required at a leaf (`min_samples_leaf`): 2
- Maximum features considered for a split (`max_features`): `sqrt`
- Class weights (`class_weight`): `balanced`

The best cross-validation F1-score recorded during hyperparameter search was approximately 0.532.

This is a cross-validation result, not the final test-set F1-score.

The final model selection should be supported by comparing all candidate models using consistent evaluation data.

## Model Evaluation

The models are evaluated using the following classification metrics:

| Metric | Description |
|---|---|
| Accuracy | Measures the proportion of correct predictions. |
| Precision | Measures how many predicted attrition cases were actual attrition cases. |
| Recall | Measures how many actual attrition cases were correctly identified. |
| F1-score | Balances precision and recall using their harmonic mean. |
| ROC-AUC | Measures the model's ability to distinguish between the two classes across classification thresholds. |

For employee attrition prediction, recall and F1-score are particularly useful because missing employees who actually leave can be an important business concern.

The final model should be selected based on actual evaluation results, business requirements, and the trade-off between precision and recall.

### Algorithm Comparison

The following table can be completed with the actual evaluation results generated during model training.

| Algorithm | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | To be added | To be added | To be added | To be added | To be added |
| Decision Tree | To be added | To be added | To be added | To be added | To be added |
| Random Forest | To be added | To be added | To be added | To be added | To be added |
| Tuned Random Forest | To be added | To be added | To be added | To be added | To be added |

**Note:** The comparison scores must be obtained from the actual evaluation results. They should not be estimated or invented.

## Input Features

The model uses 30 employee features:

- Age
- BusinessTravel
- DailyRate
- Department
- DistanceFromHome
- Education
- EducationField
- EnvironmentSatisfaction
- Gender
- HourlyRate
- JobInvolvement
- JobLevel
- JobRole
- JobSatisfaction
- MaritalStatus
- MonthlyIncome
- MonthlyRate
- NumCompaniesWorked
- OverTime
- PercentSalaryHike
- PerformanceRating
- RelationshipSatisfaction
- StockOptionLevel
- TotalWorkingYears
- TrainingTimesLastYear
- WorkLifeBalance
- YearsAtCompany
- YearsInCurrentRole
- YearsSinceLastPromotion
- YearsWithCurrManager

The target variable is `Attrition`.

Target mapping:

- `No` → `0`
- `Yes` → `1`

## Project Structure

```text
employee-attrition-prediction/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── data/
│   └── Employee dataset and processed data
│
├── models/
│   ├── employee_attrition_model.joblib
│   └── model_metadata.json
│
├── notebook/
│   └── Jupyter notebooks
│
├── reports/
│   └── Analysis reports
│
├── tests/
│   └── API tests
│
├── fronted.py
├── requirement.txt
├── Dockerfile
└── README.md
```

## Installation and Setup

### Prerequisites

Install the following:

- Python
- pip
- Git (optional, for version control)

### 1. Clone the Repository

If you are setting up the project from GitHub:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd employee-attrition-prediction
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv my_virtual
```

Activate it on Windows PowerShell:

```powershell
.\my_virtual\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the dependencies listed in the project's requirements file:

```bash
pip install -r requirement.txt
```

If a required package is missing, install it in the activated environment.

## Running the Application

The application has two main components: a FastAPI backend and a Streamlit frontend.

### 1. Start the FastAPI Backend

Open a terminal in the project root and run:

```bash
python -m uvicorn app.main:app --reload
```

The API will normally be available at:

`http://127.0.0.1:8000`

### 2. Open the API Documentation

Open the following address in your browser:

`http://127.0.0.1:8000/docs`

The interactive Swagger documentation allows you to inspect the available API endpoints and test prediction requests.

### 3. Start the Streamlit Frontend

Open a second terminal in the project root, activate the same virtual environment, and run:

```bash
streamlit run fronted.py
```

The Streamlit application will normally be available at:

`http://localhost:8501`

Keep both the FastAPI and Streamlit processes running while using the application.

## API Endpoints

The FastAPI application provides the following endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application root endpoint |
| GET | `/health` | Health-check endpoint |
| POST | `/predict` | Predict employee attrition |

The `POST /predict` endpoint accepts employee information, passes it to the trained model, and returns a prediction.

Check the Swagger documentation at `/docs` for the exact request schema and response fields.

## How to Use the Application

1. Start the FastAPI backend.
2. Start the Streamlit frontend.
3. Open the Streamlit application in your browser.
4. Enter the employee information in the form.
5. Click the Predict Attrition button.
6. Review the predicted outcome and attrition probability, if returned by the API.

The application displays whether the model predicts that an employee may leave or stay.

## Future Improvements

- Add a model comparison dashboard with performance charts.
- Display confusion matrices and ROC curves.
- Add feature importance analysis.
- Improve the user interface and prediction explanations.
- Add stronger automated tests and input validation.
- Monitor model performance on new data.
- Evaluate fairness and potential bias before real-world use.

## Limitations

- Predictions depend on the quality and representativeness of the training data.
- Model predictions are estimates, not guarantees of future employee behavior.
- Performance may change when applied to a different organization or workforce.
- Prediction errors and potential biases must be evaluated before real-world use.
- The model should support workforce analysis rather than serve as the sole basis for employment decisions.

## Conclusion

This project demonstrates an end-to-end machine learning workflow, from data preprocessing and classification model training to API development and an interactive web interface.

It provides practical experience with Python, Scikit-learn, model evaluation, hyperparameter tuning, FastAPI, and Streamlit.

The project also demonstrates how machine learning predictions can be integrated into an application for interactive use.

---

**Author:** Satyam Malakar

**Project:** Employee Attrition Prediction