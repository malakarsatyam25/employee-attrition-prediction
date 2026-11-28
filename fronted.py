
import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #183153;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: #183153;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #eef4ff;
        border: 1px solid #cbdcff;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">'
    'Employee Attrition Prediction System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning application to predict employee attrition'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("📊 Project Information")

    st.write(
        "This application uses a trained "
        "Random Forest classification model "
        "to predict employee attrition."
    )

    st.subheader("Technologies")

    st.markdown(
        """
        - Python
        - Pandas and NumPy
        - Scikit-learn
        - Random Forest
        - FastAPI
        - Streamlit
        """
    )

    st.divider()

    st.caption("Employee Attrition Prediction Project")


# --------------------------------------------------
# EMPLOYEE INPUT FORM
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Enter Employee Details</div>',
    unsafe_allow_html=True
)

st.write(
    "Fill in the employee information below and click "
    "**Predict Attrition** to get a prediction."
)

with st.form("employee_form"):

    # PERSONAL INFORMATION
    st.subheader("👤 Personal Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=30
        )

    with col2:
        Gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col3:
        MaritalStatus = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Divorced"]
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        Education = st.selectbox(
            "Education Level",
            [1, 2, 3, 4, 5],
            index=2
        )

    with col2:
        EducationField = st.selectbox(
            "Education Field",
            [
                "Life Sciences",
                "Medical",
                "Marketing",
                "Technical Degree",
                "Other",
                "Human Resources"
            ]
        )

    with col3:
        DistanceFromHome = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=29,
            value=5
        )

    st.divider()

    # JOB INFORMATION
    st.subheader("💼 Job Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        Department = st.selectbox(
            "Department",
            [
                "Sales",
                "Research & Development",
                "Human Resources"
            ]
        )

    with col2:
        JobRole = st.selectbox(
            "Job Role",
            [
                "Sales Executive",
                "Research Scientist",
                "Laboratory Technician",
                "Manufacturing Director",
                "Healthcare Representative",
                "Manager",
                "Sales Representative",
                "Research Director",
                "Human Resources"
            ]
        )

    with col3:
        JobLevel = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5],
            index=1
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        BusinessTravel = st.selectbox(
            "Business Travel",
            [
                "Travel_Rarely",
                "Travel_Frequently",
                "Non-Travel"
            ]
        )

    with col2:
        OverTime = st.selectbox(
            "OverTime",
            ["No", "Yes"]
        )

    with col3:
        NumCompaniesWorked = st.number_input(
            "Number of Companies Worked",
            min_value=0,
            max_value=9,
            value=2
        )

    st.divider()

    # SALARY INFORMATION
    st.subheader("💰 Salary Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        MonthlyIncome = st.number_input(
            "Monthly Income",
            min_value=1009,
            max_value=19999,
            value=5000
        )

    with col2:
        DailyRate = st.number_input(
            "Daily Rate",
            min_value=102,
            max_value=1499,
            value=800
        )

    with col3:
        HourlyRate = st.number_input(
            "Hourly Rate",
            min_value=30,
            max_value=100,
            value=65
        )

    col1, col2 = st.columns(2)

    with col1:
        MonthlyRate = st.number_input(
            "Monthly Rate",
            min_value=2094,
            max_value=26999,
            value=14000
        )

    with col2:
        PercentSalaryHike = st.number_input(
            "Percent Salary Hike",
            min_value=11,
            max_value=25,
            value=15
        )

    st.divider()

    # SATISFACTION AND PERFORMANCE
    st.subheader("⭐ Satisfaction and Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        EnvironmentSatisfaction = st.selectbox(
            "Environment Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col2:
        JobSatisfaction = st.selectbox(
            "Job Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col3:
        JobInvolvement = st.selectbox(
            "Job Involvement",
            [1, 2, 3, 4],
            index=2
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        RelationshipSatisfaction = st.selectbox(
            "Relationship Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col2:
        WorkLifeBalance = st.selectbox(
            "Work-Life Balance",
            [1, 2, 3, 4],
            index=2
        )

    with col3:
        PerformanceRating = st.selectbox(
            "Performance Rating",
            [3, 4],
            index=0
        )

    st.divider()

    # WORK EXPERIENCE
    st.subheader("📅 Work Experience")

    col1, col2, col3 = st.columns(3)

    with col1:
        TotalWorkingYears = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=8
        )

    with col2:
        YearsAtCompany = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=5
        )

    with col3:
        YearsInCurrentRole = st.number_input(
            "Years in Current Role",
            min_value=0,
            max_value=18,
            value=3
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        YearsWithCurrManager = st.number_input(
            "Years with Current Manager",
            min_value=0,
            max_value=17,
            value=3
        )

    with col2:
        YearsSinceLastPromotion = st.number_input(
            "Years Since Last Promotion",
            min_value=0,
            max_value=15,
            value=1
        )

    with col3:
        TrainingTimesLastYear = st.number_input(
            "Training Times Last Year",
            min_value=0,
            max_value=6,
            value=3
        )

    col1, col2 = st.columns(2)

    with col1:
        StockOptionLevel = st.selectbox(
            "Stock Option Level",
            [0, 1, 2, 3],
            index=1
        )

    with col2:
        st.write("")
        st.write("")
        st.caption("Review all details before submitting.")

    # SUBMIT BUTTON
    submitted = st.form_submit_button(
        "🔍 Predict Attrition",
        use_container_width=True
    )


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if submitted:

    employee_data = {
        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "Department": Department,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EducationField": EducationField,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobRole": JobRole,
        "JobSatisfaction": JobSatisfaction,
        "MaritalStatus": MaritalStatus,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager
    }

    st.divider()
    st.subheader("📊 Prediction Result")

    with st.spinner("Analyzing employee information..."):

        try:
            response = requests.post(
                API_URL,
                json=employee_data,
                timeout=30
            )

            response.raise_for_status()
            result = response.json()

            prediction_label = result.get(
                "prediction_label",
                "Prediction completed"
            )

            prediction = result.get("prediction")

            # Find the probability returned by the API.
            probability = result.get("attrition_probability")

            if probability is None:
                probability = result.get("probability")

            if probability is None:
                probability = result.get("prediction_probability")

            # Display prediction
            if prediction == 1:
                st.error("⚠️ " + prediction_label)
            elif prediction == 0:
                st.success("✅ " + prediction_label)
            else:
                st.info(prediction_label)

            # Display probability if the API returns it.
            if probability is not None:

                probability = float(probability)

                # Handle probabilities represented as percentages.
                if 1 < probability <= 100:
                    probability = probability / 100

                probability = max(0.0, min(1.0, probability))

                st.metric(
                    "Predicted Attrition Probability",
                    f"{probability:.1%}"
                )

                st.progress(probability)

            st.caption(
                "This is a machine learning prediction, "
                "not a guarantee of an employee's future behavior."
            )

            with st.expander("View API response"):
                st.json(result)

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to the FastAPI backend. "
                "Start the API in another terminal using: "
                "python -m uvicorn app.main:app --reload"
            )

        except requests.exceptions.Timeout:
            st.error(
                "The prediction request timed out. "
                "Please try again."
            )

        except requests.exceptions.HTTPError:
            st.error(
                f"API request failed with status "
                f"{response.status_code}."
            )

            try:
                st.json(response.json())
            except ValueError:
                st.write(response.text)

        except (ValueError, TypeError) as error:
            st.error(f"Could not process the prediction result: {error}")

        except requests.exceptions.RequestException as error:
            st.error(f"Request failed: {error}")
