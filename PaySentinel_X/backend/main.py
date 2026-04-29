from fastapi import FastAPI
from pydantic import BaseModel

from backend.model import predict_fraud


app = FastAPI(title="FraudShield AI")


class Transaction(BaseModel):
    amount: float
    transaction_hour: int
    old_balance: float
    new_balance: float
    is_international: int


@app.get("/")
def home():
    return {
        "message": "FraudShield AI backend is running"
    }


@app.post("/predict")
def predict(transaction: Transaction):
    transaction_data = transaction.dict()
    result = predict_fraud(transaction_data)

    return {
        "transaction": transaction_data,
        "prediction": result
    }
