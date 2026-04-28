# 💰 PaySentinel AI

### AI-Powered Transaction Fraud Detection System

---

## 🚀 Overview

**PaySentinel AI** is a machine learning-based web application designed to detect fraudulent online transactions in real-time.

The system analyzes transaction data and predicts whether a transaction is **legitimate or fraudulent**, along with a **risk level score** to assist financial systems in preventing fraud.

---

## 🎯 Features

* 🔍 Fraud detection using Machine Learning
* 📊 Risk scoring (Low / Medium / High)
* ⚡ FastAPI backend for real-time predictions
* 📥 Structured API with JSON input
* 🧠 ML model trained using transaction data
* 🌐 Ready for frontend integration (React/Streamlit)

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn (Random Forest)
* **Data Handling:** Pandas
* **Model Storage:** Joblib
* **API Testing:** Swagger UI

---

## 📁 Project Structure

```bash
fraudshield_ai/
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── schema.py
│   ├── train_model.py
│   └── fraud_model.pkl
├── data/
│   └── transactions.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/paysentinel-ai.git
cd paysentinel-ai
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Train the model

```bash
python backend/train_model.py
```

---

### 4. Run the backend server

```bash
uvicorn backend.main:app --reload
```

---

### 5. Open API Docs

Go to:
👉 http://127.0.0.1:8000/docs

---

## 🧪 Sample API Input

```json
{
  "amount": 95000,
  "transaction_hour": 2,
  "old_balance": 100000,
  "new_balance": 5000,
  "is_international": 1
}
```

---

## 📊 Sample Output

```json
{
  "fraud": true,
  "probability": 87.45,
  "risk_level": "High"
}
```

---

## 📈 How It Works

1. Transaction data is passed to the API
2. Data is converted into a structured format
3. Pre-trained ML model analyzes patterns
4. System predicts fraud probability
5. Risk level is assigned

---

## 🔮 Future Enhancements

* 🌐 Frontend dashboard (React)
* 📊 Real-time transaction monitoring
* 📁 CSV bulk upload support
* 🔔 Fraud alert system
* 🧠 Advanced models (XGBoost, Neural Networks)
* 📡 Integration with payment gateways

---

## 📌 Use Cases

* Banking systems
* Payment gateways
* FinTech startups
* Fraud monitoring platforms

---

## 🏆 Resume Description

**PaySentinel AI – ML-Based Fraud Detection System**
Developed a machine learning-powered web application to detect fraudulent transactions using Random Forest algorithms, providing real-time predictions and risk scoring via a FastAPI backend.

---

## 📜 License

This project is for educational and academic purposes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## ⭐ Acknowledgment

Inspired by real-world financial fraud detection systems and AI-driven security solutions.

---
