import joblib
import pandas as pd


model = joblib.load("backend/fraud_model.pkl")


def predict_fraud(transaction_data: dict) -> dict:
    df = pd.DataFrame([transaction_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if probability >= 0.75:
        risk_level = "High"
    elif probability >= 0.40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "is_fraud": bool(prediction),
        "fraud_probability": round(probability * 100, 2),
        "risk_level": risk_level
    }
