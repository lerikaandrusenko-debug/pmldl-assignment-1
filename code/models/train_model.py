# code/models/train_model.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Загрузка датасета
data = pd.read_csv('data/Pokemon.csv')

# Подготовка данных (пример: предсказание, является ли покемон легендарным)
features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
X = data[features]
y = data['Legendary']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабирование признаков
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучение модели
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Сохранение модели и скейлера
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Оценка модели (для проверки)
accuracy = model.score(X_test_scaled, y_test)
print(f"Accuracy: {accuracy}")