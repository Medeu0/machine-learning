"""Генерация синтетического датасета квартир. Запуск: python src/generate_data.py"""
import numpy as np
import pandas as pd

def generate(n: int = 1200, seed: int = 2024) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    district = rng.choice(["центр", "спальный", "окраина"], n, p=[0.25, 0.5, 0.25])
    mult = pd.Series(district).map({"центр": 1.5, "спальный": 1.0, "окраина": 0.75}).values
    df = pd.DataFrame({
        "площадь_м2": rng.uniform(28, 160, n).round(0),
        "комнаты": rng.integers(1, 5, n),
        "этаж": rng.integers(1, 20, n),
        "возраст_дома": rng.integers(0, 55, n),
        "до_метро_мин": rng.uniform(1, 40, n).round(0),
        "район": district,
    })
    base = 2.2*df["площадь_м2"] + 14*df["комнаты"] - 0.7*df["возраст_дома"] - 1.1*df["до_метро_мин"] + 60
    df["цена_тыс"] = (base * mult + rng.normal(0, 22, n)).round(1)
    df.loc[rng.choice(n, int(n*0.02), replace=False), "возраст_дома"] = np.nan
    lux = rng.choice(n, 8, replace=False)
    df.loc[lux, "цена_тыс"] *= 2.5
    return df

if __name__ == "__main__":
    generate().to_csv("data/apartments.csv", index=False)
    print("saved data/apartments.csv")
