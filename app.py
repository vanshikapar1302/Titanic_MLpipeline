from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.joblib")

class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: Passenger):
    features = [[data.Pclass, data.Sex, data.Age, data.SibSp,
                 data.Parch, data.Fare, data.Embarked]]
    prediction = int(model.predict(features)[0])
    return {
        "survived": prediction,
        "result": "Survived" if prediction == 1 else "Did not survive"
    }