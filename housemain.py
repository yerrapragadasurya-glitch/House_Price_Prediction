from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="House Price Prediction API")


# Load trained model
model = joblib.load(r"C:\Users\SURYA\OneDrive\Desktop\surya-ml\venv\house_price_model.joblib")


# Input data format
class HouseData(BaseModel):
    Id: int
    OverallQual: int
    GrLivArea: float
    GarageCars: float
    TotalBsmtSF: float
    YearBuilt: int
    FullBath: int
    BedroomAbvGr: int
    LotArea: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict(data: HouseData):

    input_data = pd.DataFrame([{
        "Id": data.Id,
        "OverallQual": data.OverallQual,
        "GrLivArea": data.GrLivArea,
        "GarageCars": data.GarageCars,
        "TotalBsmtSF": data.TotalBsmtSF,
        "YearBuilt": data.YearBuilt,
        "FullBath": data.FullBath,
        "BedroomAbvGr": data.BedroomAbvGr,
        "LotArea": data.LotArea
    }])

    prediction = model.predict(input_data)

    return {
       "predicted_SalePrice": float(prediction[0])
    }