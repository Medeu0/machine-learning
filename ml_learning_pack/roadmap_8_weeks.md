# Roadmap: 8 недель до ML-портфолио

Правило: 1–1.5 часа в день. Каждый день: запустить код урока руками + мини-задание.

---

## Неделя 1 — Основы ML и инструменты
**Изучать:** что такое ML, supervised/unsupervised, X и y, fit/predict, NumPy, pandas.
**Ноутбуки:** `01_ml_basics.ipynb`, `02_numpy_pandas.ipynb`, `03_linear_regression.ipynb`
**Проект:** `projects/project1_student_score/` — Student Score Predictor.
**Повторять:** словарь терминов из cheatsheet (X, y, fit, predict, regression, classification).
**Результат недели:** ты обучил первую модель, понимаешь shape массивов,
сделал первый проект и можешь объяснить, что такое supervised learning.

## Неделя 2 — Как модель учится
**Изучать:** cost function, gradient descent, learning rate, multiple regression, vectorization.
**Ноутбуки:** `04_gradient_descent.ipynb`, `05_multiple_regression.ipynb`, `06_feature_scaling.ipynb`
**Проект:** `projects/project2_house_price/` — House Price Prediction.
**Повторять:** урок 3 (linear regression), формулу w*x + b.
**Результат недели:** ты написал gradient descent с нуля на NumPy
и понимаешь, ЧТО происходит внутри model.fit().

## Неделя 3 — Честная оценка моделей
**Изучать:** train/test split, MAE/MSE/RMSE/R², почему нельзя тестировать на train.
**Ноутбуки:** `07_train_test_metrics.ipynb`
**Проект:** доработать Project 2: добавить train/test split и метрики.
**Повторять:** уроки 4–6, переделать мини-задания без подглядывания.
**Результат недели:** ты умеешь честно измерять качество модели и знаешь 4 метрики регрессии.

## Неделя 4 — Классификация
**Изучать:** logistic regression, sigmoid, decision boundary, accuracy/precision/recall/F1,
confusion matrix, когда accuracy обманывает.
**Ноутбуки:** `08_logistic_regression.ipynb`, `09_classification_metrics.ipynb`
**Проекты:** `projects/project3_pass_fail/` и `projects/project4_bank_risk/`
**Повторять:** разницу regression vs classification.
**Результат недели:** два проекта-классификатора, умеешь читать confusion matrix.

## Неделя 5 — Переобучение и борьба с ним
**Изучать:** overfitting/underfitting, bias/variance, polynomial features, регуляризация.
**Ноутбуки:** `10_overfitting.ipynb`, `11_regularization.ipynb`
**Проект:** мини-эксперимент Model Complexity (внутри урока 10).
**Повторять:** train/test split — это инструмент обнаружения переобучения.
**Результат недели:** ты по графику отличаешь overfit от underfit и знаешь 3 способа лечения.

## Неделя 6 — Деревья и нейросети
**Изучать:** decision trees, random forest, feature importance, нейрон, слой, активация, Keras.
**Ноутбуки:** `12_decision_trees.ipynb`, `13_random_forest.ipynb`, `14_neural_networks.ipynb`
**Проект:** MNIST-классификатор (внутри урока 14).
**Повторять:** метрики классификации (неделя 4).
**Результат недели:** обучил нейросеть на картинках — первый шаг к Computer Vision.

## Неделя 7 — Unsupervised + рекомендации + RL
**Изучать:** K-means, выбор K, anomaly detection, PCA, recommender systems, Q-learning.
**Ноутбуки:** `15_kmeans_pca.ipynb`, `16_anomaly_detection.ipynb`,
`17_recommender.ipynb`, `18_reinforcement_learning.ipynb`
**Проект:** `projects/project5_customer_segmentation/`
**Результат недели:** покрыт весь 3-й курс специализации.

## Неделя 8 — Портфолио
**Делать:** оба портфолио-проекта из `portfolio/`, выложить на GitHub.
**Шаги:** пройти ноутбуки проектов → переписать выводы своими словами →
оформить README → создать репозитории → добавить идеи улучшений как Issues.
**Повторять:** пройти 10 случайных задач из practice_tasks.md уровня intermediate.
**Результат недели:** 2 репозитория на GitHub + 5 учебных проектов = готовое стартовое портфолио.

---

## Что делать после 8 недель
1. Пройти advanced-задачи из practice_tasks.md.
2. Заменить синтетические данные в проектах на реальные (Kaggle: House Prices, Titanic).
3. Начать Computer Vision: промпты для CV есть в prompts_for_future.md.
