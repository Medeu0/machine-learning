"""Обучение лучшей модели и сохранение в model.joblib. Запуск: python src/train.py"""
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

NUM = ["площадь_м2", "комнаты", "этаж", "возраст_дома", "до_метро_мин"]
CAT = ["район"]

def build_pipeline() -> Pipeline:
    prep = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())]), NUM),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT),
    ])
    return Pipeline([("prep", prep),
                     ("model", RandomForestRegressor(n_estimators=300, random_state=0))])

if __name__ == "__main__":
    df = pd.read_csv("data/apartments.csv")
    X, y = df.drop(columns="цена_тыс"), df["цена_тыс"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = build_pipeline().fit(X_tr, y_tr)
    pred = pipe.predict(X_te)
    print(f"MAE={mean_absolute_error(y_te, pred):.1f}  R2={r2_score(y_te, pred):.3f}")
    joblib.dump(pipe, "model.joblib")
    print("saved model.joblib")
