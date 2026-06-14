"""Генерация синтетических клиентов банка. Запуск: python src/generate_data.py"""
import numpy as np
import pandas as pd

def generate(n: int = 3000, seed: int = 77) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    employment = rng.choice(["найм", "ИП", "безработный"], n, p=[0.7, 0.2, 0.1])
    emp_risk = pd.Series(employment).map({"найм": 0.0, "ИП": 0.4, "безработный": 1.3}).values
    df = pd.DataFrame({
        "доход_тыс": rng.normal(450, 170, n).clip(80).round(0),
        "долг_к_доходу": rng.uniform(0, 0.95, n).round(2),
        "просрочки_за_год": rng.poisson(0.5, n),
        "стаж_клиента_лет": rng.uniform(0, 18, n).round(1),
        "возраст": rng.integers(21, 70, n),
        "занятость": employment,
    })
    logit = (3.0*df["долг_к_доходу"] + 1.0*df["просрочки_за_год"] + emp_risk
             - 0.003*df["доход_тыс"] - 0.07*df["стаж_клиента_лет"] - 2.0)
    df["риск"] = (rng.uniform(0, 1, n) < 1/(1+np.exp(-logit))).astype(int)
    df.loc[rng.choice(n, int(n*0.03), replace=False), "доход_тыс"] = np.nan
    return df

if __name__ == "__main__":
    generate().to_csv("data/bank_clients.csv", index=False)
    print("saved data/bank_clients.csv")
