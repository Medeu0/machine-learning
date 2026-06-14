"""Обучение модели риска и сохранение. Запуск: python src/train.py"""
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, classification_report

NUM = ["доход_тыс", "долг_к_доходу", "просрочки_за_год", "стаж_клиента_лет", "возраст"]
CAT = ["занятость"]

def build_pipeline() -> Pipeline:
    prep = ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                          ("sc", StandardScaler())]), NUM),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT),
    ])
    return Pipeline([("prep", prep), ("model", GradientBoostingClassifier(random_state=0))])

if __name__ == "__main__":
    df = pd.read_csv("data/bank_clients.csv")
    X, y = df.drop(columns="риск"), df["риск"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    pipe = build_pipeline().fit(X_tr, y_tr)
    proba = pipe.predict_proba(X_te)[:, 1]
    print("ROC-AUC:", round(roc_auc_score(y_te, proba), 3))
    print(classification_report(y_te, (proba >= 0.3).astype(int)))  # порог 0.3 из анализа стоимости
    joblib.dump(pipe, "model.joblib")
    print("saved model.joblib")
