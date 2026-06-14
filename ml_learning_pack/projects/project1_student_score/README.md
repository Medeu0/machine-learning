# Student Score Predictor

Регрессионная модель предсказывает экзаменационную оценку студента по часам подготовки и посещаемости. Учебный проект уровня beginner: полный мини-цикл ML от данных до анализа ошибок.

**GitHub description (1 строка):** ML regression model predicting student exam scores from study hours and attendance (scikit-learn)
**Topics:** machine-learning, linear-regression, scikit-learn, beginner-project, python

## Структура
```
project1_student_score/
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
1. Генерация синтетических данных (150 студентов)
2. EDA: describe, scatter-графики связей
3. Train/test split 80/20
4. LinearRegression
5. MAE и R² на test
6. График predicted vs actual, гистограмма остатков, разбор худших промахов

## Результаты
MAE ≈ 5 баллов, R² ≈ 0.85–0.9. Часы учёбы — главный фактор (~5 баллов за час).

## Идеи улучшения
- Реальные данные (Kaggle: Student Performance)
- Больше признаков: сон, стресс, прошлые оценки
- Кросс-валидация вместо одного split
- Сравнение нескольких моделей
