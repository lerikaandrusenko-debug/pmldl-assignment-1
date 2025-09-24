import streamlit as st
import requests

st.title("Прогноз легендарности покемона")

# Вводные поля для характеристик покемона
hp = st.number_input("HP", min_value=0, max_value=255, value=50)
attack = st.number_input("Attack", min_value=0, max_value=255, value=50)
defense = st.number_input("Defense", min_value=0, max_value=255, value=50)
sp_atk = st.number_input("Sp. Atk", min_value=0, max_value=255, value=50)
sp_def = st.number_input("Sp. Def", min_value=0, max_value=255, value=50)
speed = st.number_input("Speed", min_value=0, max_value=255, value=50)

# Кнопка для предсказания
if st.button("Сделать предсказание"):
    # Формирование данных для отправки в API
    data = {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp_Atk": sp_atk,
        "Sp_Def": sp_def,
        "Speed": speed
    }
    
    # Отправка запроса к API
    response = requests.post("http://api:8000/predict", json=data)
    
    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        probability = result["probability"]
        st.write(f"Легендарный: {'Да' if prediction else 'Нет'}")
        st.write(f"Вероятность легендарности: {probability:.2%}")
    else:
        st.error("Ошибка при запросе к API")