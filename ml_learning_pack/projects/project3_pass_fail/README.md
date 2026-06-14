# Pass/Fail Student Classifier

Бинарная классификация (logistic regression): предсказание сдачи экзамена по часам подготовки и среднему баллу, с картой вероятностей и decision boundary.

**GitHub description (1 строка):** Binary classification of student exam outcomes with logistic regression and decision boundary visualization
**Topics:** machine-learning, classification, logistic-regression, scikit-learn, python

## Структура
```
project3_pass_fail/
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
1. Синтетика: 400 студентов, 2 признака
2. Stratified train/test split
3. Pipeline(StandardScaler → LogisticRegression)
4. Accuracy, classification report, confusion matrix
5. Карта вероятностей и decision boundary
6. Вероятностные предсказания для конкретных студентов

## Результаты
Accuracy ≈ 0.85+, наглядная граница решений в пространстве признаков.

## Идеи улучшения
- Подбор порога под бизнес-цель (минимум пропущенных «провалов»)
- Больше признаков: сон, посещаемость
- ROC-кривая и AUC
- Калибровка вероятностей
