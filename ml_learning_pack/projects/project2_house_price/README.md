# House Price Prediction

Множественная линейная регрессия для оценки стоимости жилья: 4 признака, масштабирование, sklearn Pipeline, анализ влияния признаков и остатков.

**GitHub description (1 строка):** House price prediction with multiple linear regression, feature scaling and sklearn Pipeline
**Topics:** machine-learning, regression, sklearn-pipeline, feature-scaling, python

## Структура
```
project2_house_price/
├── notebook.ipynb      # весь анализ и модель
├── README.md
└── requirements.txt
```

## Как запустить
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Что внутри (этапы)
1. Синтетический датасет 300 домов (площадь, комнаты, возраст, расстояние до центра)
2. EDA: describe, корреляции, гистограммы
3. Pipeline(StandardScaler → LinearRegression)
4. MAE, R² на test
5. Сравнение влияния признаков по масштабированным весам
6. Анализ остатков, предсказание для новой квартиры

## Результаты
MAE ≈ 14–16 тыс.$, R² ≈ 0.95. Площадь — главный плюс-фактор, удалённость от центра — главный минус.

## Идеи улучшения
- Реальные данные (Kaggle House Prices)
- Полиномиальные признаки и Ridge
- GridSearchCV по alpha
- Категориальные признаки (район) через one-hot
