"""Предсказание для новой квартиры. Запуск: python src/predict.py"""
import pandas as pd
import joblib

if __name__ == "__main__":
    pipe = joblib.load("model.joblib")
    new = pd.DataFrame([{
        "площадь_м2": 75, "комнаты": 3, "этаж": 7,
        "возраст_дома": 12, "до_метро_мин": 8, "район": "спальный",
    }])
    price = pipe.predict(new)[0]
    print(f"Оценка квартиры: {price:.0f} тыс.")
