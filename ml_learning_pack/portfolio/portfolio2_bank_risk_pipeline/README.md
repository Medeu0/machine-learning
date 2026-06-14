# Bank Client Risk Classifier — Full ML Pipeline 🏦

Полный пайплайн классификации риска клиентов банка на несбалансированных данных:
EDA → preprocessing (импутация, scaling, one-hot) → baseline и 3 модели → ROC/PR-кривые →
**подбор порога классификации по стоимости ошибок в деньгах** → error analysis.
Данные синтетические, проект учебный/портфолио.

**GitHub description:** Credit risk scoring pipeline on imbalanced data: model comparison, ROC/PR analysis and cost-based threshold tuning
**Topics:** machine-learning, classification, imbalanced-data, credit-scoring, sklearn-pipeline

## Структура репозитория
```
portfolio2_bank_risk_pipeline/
├── data/                  # датасет (генерируется скриптом)
├── notebooks/
│   └── bank_risk_pipeline.ipynb   # основной анализ
├── src/
│   ├── generate_data.py
│   ├── train.py           # обучение + model.joblib
│   └── predict.py         # скоринг нового клиента с порогом 0.3
├── README.md
└── requirements.txt
```

## Как запустить
```bash
pip install -r requirements.txt
python src/generate_data.py
jupyter notebook notebooks/bank_risk_pipeline.ipynb
# или: python src/train.py && python src/predict.py
```

## Ключевые результаты
- Baseline «все надёжные» имеет accuracy ~0.88 и нулевую пользу — метрики выбраны корректно
  (recall риска, F1, ROC-AUC, PR-кривая).
- Лучшая модель: GradientBoosting, ROC-AUC ≈ 0.85–0.9.
- Порог 0.5 заменён порогом ~0.3, найденным минимизацией убытка
  (FN = 2000$, FP = 100$) — суммарный убыток банка снижается заметно.
- Error analysis: пропущенные рисковые — «тихие» клиенты без сигналов в текущих признаках;
  направление улучшения — новые источники данных, а не тюнинг модели.

## Идеи до production-level
- SMOTE vs class_weight, калибровка вероятностей
- SHAP-объяснения решений (требование регуляторов)
- Optuna, мониторинг дрейфа, регулярное переобучение
- REST-сервис скоринга с журналированием решений
