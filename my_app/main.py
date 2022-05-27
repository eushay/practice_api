import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder #to convert pydantic model into json obj

app = FastAPI()
lr_model = joblib.load('lr_model.joblib')


class Features(BaseModel):
    Temperature: float
    Humidity: float
    Light: int
    CO2: float
    HumidityRatio: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/msg")
def msg(current_vals : Features):
    vals = jsonable_encoder(current_vals)
    prediction = lr_model.predict(pd.DataFrame(vals, index=[0]))[0]
    return {"Prediction": int(prediction)}
