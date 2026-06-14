# End-to-End Apartment Price Prediction 🏠

Полный ML-цикл прогноза цен на квартиры: данные → EDA → preprocessing (импутация, scaling,
one-hot) → сравнение трёх моделей с кросс-валидацией → error analysis → выводы для бизнеса.

**GitHub description:** End-to-end apartment price prediction: sklearn pipelines, model comparison, cross-validation and error analysis
**Topics:** machine-learning, regression, sklearn-pipeline, eda, portfolio-project

## Структура репозитория
```
portfolio1_apartment_price/
├── data/                  # датасет (генерируется скриптом)
├── notebooks/
│   └── apartment_price_analysis.ipynb   # основной анализ
├── src/
│   ├── generate_data.py   # генерация данных
│   ├── train.py           # обучение + сохранение model.joblib
│   └── predict.py         # инференс для новой квартиры
├── README.md
└── requirements.txt
```

## Как запустить
```bash
pip install -r requirements.txt
python src/generate_data.py     # создать данные
jupyter notebook notebooks/apartment_price_analysis.ipynb   # полный анализ
# или консольный вариант:
python src/train.py && python src/predict.py
```

## Данные
1200 квартир, 6 признаков (площадь, комнаты, этаж, возраст, минуты до метро, район).
Намеренно реалистичные сложности: пропуски (2%), категориальный признак, выбросы-«элитки».

## Результаты
| Модель | MAE, тыс. | R² (test) |
|---|---|---|
| LinearRegression | ~25 | ~0.93 |
| Ridge (alpha=10) | ~25 | ~0.93 |
| RandomForest | ~20 | ~0.95 |

Error analysis показал: главный источник ошибок — люкс-квартиры без признака «элитности»
в данных. Это вывод про сбор данных, а не про выбор модели.

## Идеи до production-level
- Признаки: класс ЖК, ремонт, гео-координаты, фотографии (CV)
- GridSearchCV/Optuna для гиперпараметров; log-трансформация цены
- Quantile regression — интервалы цены вместо точечной оценки
- FastAPI-сервис + мониторинг дрейфа данных
