from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Загрузка модели и скейлера
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.post("/predict")
async def predict(data: dict):
    # Получение признаков из запроса
    features = [data['HP'], data['Attack'], data['Defense'], data['Sp_Atk'], data['Sp_Def'], data['Speed']]
    features = np.array(features).reshape(1, -1)
    
    # Масштабирование признаков
    features_scaled = scaler.transform(features)
    
    # Предсказание
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]
    
    return {"prediction": bool(prediction), "probability": float(probability)}