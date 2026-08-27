# 🏠 House Price Prediction using Machine Learning

## 📊 Project Overview

This project is an end-to-end **House Price Prediction Machine Learning application** that predicts the sale price of a house based on important property characteristics.

The project includes:

- Data preprocessing
- Data cleaning
- Exploratory Data Analysis
- Feature selection
- Machine Learning model training
- Model evaluation
- Model saving using Joblib
- FastAPI backend
- REST API
- Interactive HTML/CSS/JavaScript frontend

The trained Machine Learning model takes house-related features as input and predicts the expected **Sale Price**.

---

# 🛠️ Technologies Used

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Backend

- FastAPI
- Uvicorn
- Pydantic
- REST API
- CORS

## Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- JSON

---

# 📁 Dataset

The dataset contains house-related features used to predict the selling price.

## Dataset Columns

| Column | Description |
|---|---|
| `Id` | Unique house identifier |
| `OverallQual` | Overall quality of the house |
| `GrLivArea` | Above-ground living area |
| `GarageCars` | Garage capacity in cars |
| `TotalBsmtSF` | Total basement area |
| `YearBuilt` | Year the house was built |
| `FullBath` | Number of full bathrooms |
| `BedroomAbvGr` | Number of bedrooms above ground |
| `LotArea` | Total lot area |
| `SalePrice` | House sale price / target variable |

---

# 🎯 Target Variable

The target variable is:

```text
SalePrice
```

The Machine Learning model uses the following features to predict `SalePrice`:

```text
Id
OverallQual
GrLivArea
GarageCars
TotalBsmtSF
YearBuilt
FullBath
BedroomAbvGr
LotArea
```

---

# 🧹 Data Preprocessing

The dataset was prepared before training the Machine Learning model.

The preprocessing steps include:

- Loading the dataset using Pandas
- Checking dataset information
- Checking missing values
- Handling missing values
- Checking duplicate records
- Checking data types
- Performing exploratory data analysis
- Selecting relevant features
- Separating input features and target variable
- Splitting data into training and testing sets
- Preparing data for Machine Learning

---

# 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the relationship between house characteristics and sale price.

The analysis includes:

- Distribution of house prices
- Overall quality analysis
- Living area analysis
- Garage capacity analysis
- Basement area analysis
- Year built analysis
- Bathroom analysis
- Bedroom analysis
- Lot area analysis
- Correlation analysis
- Feature relationship analysis

---

# 📊 Input Features

The model uses the following input features:

```text
Id
OverallQual
GrLivArea
GarageCars
TotalBsmtSF
YearBuilt
FullBath
BedroomAbvGr
LotArea
```

---

# 🤖 Machine Learning

This project uses Machine Learning regression algorithms to predict house prices.

The problem is a:

```text
Regression Problem
```

because the target variable `SalePrice` is a continuous numerical value.

The dataset is divided into:

```text
Training Data
        ↓
Machine Learning Model
        ↓
Testing Data
        ↓
Predicted Sale Price
```

---

# 📈 Model Evaluation

The trained regression model can be evaluated using:

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted prices.

```text
MAE
```

### MSE

Mean Squared Error measures the squared difference between actual and predicted prices.

```text
MSE
```

### RMSE

Root Mean Squared Error provides the error in the same unit as the target variable.

```text
RMSE
```

### R² Score

R² Score measures how well the model explains the variation in house prices.

```text
R² Score
```

---

# 💾 Model Saving using Joblib

The trained Machine Learning model is saved using Joblib.

```python
import joblib

joblib.dump(model, "house_price_model.joblib")

print("House price model saved successfully!")
```

The model can later be loaded using:

```python
import joblib

model = joblib.load("house_price_model.joblib")
```

---

# 📦 Saved Model

The trained model is stored as:

```text
house_price_model.joblib
```

This file contains the trained Machine Learning regression model used by the FastAPI backend.

---

# ⚡ FastAPI Backend

FastAPI is used to deploy the Machine Learning model as a REST API.

The backend receives house information, sends the input to the trained model, and returns the predicted house price.

---

# 📂 Backend File

The FastAPI backend is implemented in:

```text
main.py
```

---

# 🔗 API Endpoints

## Home Endpoint

```text
GET /
```

Example:

```text
http://127.0.0.1:8000/
```

Example response:

```json
{
    "message": "House Price Prediction API is running"
}
```

---

## Prediction Endpoint

```text
POST /predict
```

This endpoint accepts house information and returns the predicted sale price.

---

# 📥 API Request

Example JSON request:

```json
{
    "Id": 100,
    "OverallQual": 7,
    "GrLivArea": 1710,
    "GarageCars": 2,
    "TotalBsmtSF": 856,
    "YearBuilt": 2003,
    "FullBath": 2,
    "BedroomAbvGr": 3,
    "LotArea": 8450
}
```

---

# 📤 API Response

Example:

```json
{
    "predicted_sale_price": 200000.0
}
```

The actual prediction depends on the trained Machine Learning model.

---

# 📖 Swagger API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

- View API endpoints
- Enter house details
- Test the prediction API
- Send JSON requests
- View prediction results

---

# 🌐 Frontend

An interactive frontend has been created using:

- HTML
- CSS
- JavaScript

The frontend provides a form where users can enter house information.

The frontend sends the entered data to the FastAPI `/predict` endpoint.

---

# 🖥️ Frontend

The frontend is contained in:

```text
index.html
```

The file contains:

```text
HTML
CSS
JavaScript
```

in a single file.

---

# 📝 Frontend Inputs

The website accepts the following inputs:

```text
Id
Overall Quality
Living Area
Garage Cars
Total Basement Area
Year Built
Full Bathrooms
Bedrooms
Lot Area
```

After entering the values, the user can click:

```text
Predict House Price
```

The predicted price is then displayed on the webpage.

---

# 🔄 Frontend and Backend Workflow

```text
User
  ↓
HTML Form
  ↓
JavaScript
  ↓
FastAPI /predict
  ↓
House Price ML Model
  ↓
Prediction
  ↓
JSON Response
  ↓
Frontend
  ↓
Predicted House Price
```

---

# 🔌 API Integration

JavaScript communicates with the FastAPI backend using the Fetch API.

Example:

```javascript
const response = await fetch(
    "http://127.0.0.1:8000/predict",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }
);

const result = await response.json();
```

The returned prediction is displayed on the frontend.

---

# 🔐 CORS

CORS middleware can be used to allow communication between the frontend and FastAPI backend.

Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

# 🧪 Example Prediction

### Input

```json
{
    "Id": 100,
    "OverallQual": 7,
    "GrLivArea": 1710,
    "GarageCars": 2,
    "TotalBsmtSF": 856,
    "YearBuilt": 2003,
    "FullBath": 2,
    "BedroomAbvGr": 3,
    "LotArea": 8450
}
```

### Output

```json
{
    "predicted_sale_price": 200000.0
}
```

> The output shown above is only an example. The actual predicted price will be generated by the trained model.

---

# 📊 Project Architecture

```text
┌─────────────────────────────────────┐
│                USER                 │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          HTML / CSS / JS            │
│             FRONTEND                │
└──────────────────┬──────────────────┘
                   │
                   │ POST /predict
                   ▼
┌─────────────────────────────────────┐
│              FASTAPI                │
│              BACKEND                │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│        HOUSE PRICE MODEL            │
│       house_price_model.joblib      │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│       PREDICTED SALE PRICE          │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          FRONTEND RESULT            │
└─────────────────────────────────────┘
```

---

# 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
EDA
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Joblib Serialization
   ↓
FastAPI Deployment
   ↓
Frontend Integration
   ↓
House Price Prediction
```

---

# 📂 Project Structure

```text
House-Price-Prediction/
│
├── houseprediction.ipynb
│
├── main.py
│
├── index.html
│
├── house_price_model.joblib
│
├── data/
│   └── house_data.csv
│
└── README.md
```

---

# 🚀 How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd House-Price-Prediction
```

---

# Step 2: Create Virtual Environment

```bash
python -m venv venv
```

---

# Step 3: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

# Step 4: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib fastapi uvicorn pydantic
```

---

# Step 5: Start FastAPI

Run:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

# Step 6: Test the API

Open:

```text
http://127.0.0.1:8000/docs
```

Select:

```text
POST /predict
```

Click:

```text
Try it out
```

Enter the house details and click:

```text
Execute
```

---

# Step 7: Run the Frontend

Open:

```text
index.html
```

in your browser.

For development, you can use **Live Server** in VS Code:

```text
Right Click index.html
        ↓
Open with Live Server
```

The frontend will communicate with:

```text
http://127.0.0.1:8000/predict
```

---

# 💼 Business Use Cases

This application can be useful for:

- Real estate price estimation
- Property valuation
- House price analysis
- Real estate decision support
- Buyer price estimation
- Seller price estimation
- Property investment analysis

---

# 🎯 Project Objectives

The main objectives of this project are:

- Build a Machine Learning regression model
- Predict house sale prices
- Perform data preprocessing
- Analyze important house features
- Evaluate model performance
- Save the trained model
- Deploy the model using FastAPI
- Build an interactive frontend
- Connect frontend with backend
- Generate real-time house price predictions

---

# 📌 Project Highlights

✅ End-to-end Machine Learning project

✅ House price prediction

✅ Regression-based prediction

✅ Data cleaning

✅ Exploratory Data Analysis

✅ Feature selection

✅ Model training

✅ Model evaluation

✅ Joblib model serialization

✅ FastAPI REST API

✅ Swagger API documentation

✅ HTML frontend

✅ CSS styling

✅ JavaScript integration

✅ Fetch API

✅ Real-time prediction

---

# 🧠 Skills Demonstrated

## Data Analytics

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Data Visualization
- Correlation Analysis
- Feature Selection

## Machine Learning

- Regression
- Train-Test Split
- Model Training
- Model Evaluation
- Feature Engineering
- Model Serialization

## Backend Development

- FastAPI
- REST API
- Pydantic
- Uvicorn
- CORS
- API Development

## Frontend Development

- HTML
- CSS
- JavaScript
- Fetch API
- JSON
- API Integration

---

# 🔮 Future Improvements

Possible improvements include:

- Compare multiple regression algorithms
- Hyperparameter tuning
- Improve model accuracy
- Add more house features
- Add prediction history
- Add database integration
- Deploy FastAPI to the cloud
- Deploy frontend online
- Add user authentication
- Add interactive charts
- Add property price visualization
- Build a mobile-friendly interface

---

# 🏁 Conclusion

This project demonstrates an end-to-end **Machine Learning deployment workflow** for predicting house sale prices.

The project starts with data cleaning and exploratory data analysis, followed by feature selection, model training, and model evaluation.

The trained regression model is saved using **Joblib** and deployed through a **FastAPI REST API**.

An interactive **HTML, CSS, and JavaScript frontend** allows users to enter property information and receive a predicted house sale price.

The complete workflow is:

```text
Data
 ↓
Cleaning
 ↓
EDA
 ↓
Feature Selection
 ↓
Machine Learning
 ↓
Model Evaluation
 ↓
Joblib
 ↓
FastAPI
 ↓
Frontend
 ↓
House Price Prediction
```

---

# 👨‍💻 Project Information

**Project Name:** House Price Prediction

**Domain:** Machine Learning / Real Estate

**Problem Type:** Regression

**Target Variable:** `SalePrice`

**Model Serialization:** Joblib

**Backend:** FastAPI

**Frontend:** HTML, CSS, JavaScript

**API:** REST API

---

# 🔗 Project Files

Complete project files and dataset:

https://drive.google.com/drive/folders/1mKh61zKVBnPJN0A5lc77osGNkmNa-loI

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
