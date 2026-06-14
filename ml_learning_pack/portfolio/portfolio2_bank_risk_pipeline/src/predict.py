"""Скоринг нового клиента. Запуск: python src/predict.py"""
import pandas as pd
import joblib

THRESHOLD = 0.3  # выбран минимизацией убытка (см. notebook)

if __name__ == "__main__":
    pipe = joblib.load("model.joblib")
    client = pd.DataFrame([{
        "доход_тыс": 380, "долг_к_доходу": 0.55, "просрочки_за_год": 1,
        "стаж_клиента_лет": 2.5, "возраст": 29, "занятость": "ИП",
    }])
    p = pipe.predict_proba(client)[0, 1]
    print(f"P(риск) = {p:.2f} -> {'РИСК: ручная проверка' if p >= THRESHOLD else 'одобрить'}")
