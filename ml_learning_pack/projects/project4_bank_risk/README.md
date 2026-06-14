# Bank Client Risk Classifier

Учебный классификатор риска клиентов банка на синтетических данных. Фокус проекта — работа с несбалансированными классами: почему accuracy обманывает и как class_weight и выбор метрик решают задачу.

**GitHub description (1 строка):** Credit risk classification on imbalanced synthetic data: class weighting, precision/recall trade-offs
**Topics:** machine-learning, classification, imbalanced-data, credit-risk, scikit-learn

## Структура
```
project4_bank_risk/
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
1. Синтетика: 2000 клиентов, ~20% рискованных
2. Baseline «все надёжные» — разоблачение accuracy
3. Три модели: LogReg, LogReg(class_weight=balanced), RandomForest
4. Сравнение по classification report (фокус на recall класса «риск»)
5. Confusion matrix, feature importance

## Результаты
Balanced-модели находят 75–85% рискованных клиентов против 0% у baseline при той же «красивой» accuracy.

## Идеи улучшения
- ROC-AUC и precision-recall кривые
- Подбор порога по стоимости ошибок в деньгах
- SMOTE (oversampling редкого класса)
- Калибровка вероятностей, monitoring drift
