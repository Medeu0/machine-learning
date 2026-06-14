# Customer Segmentation

Сегментация клиентов магазина методом K-Means: выбор числа кластеров через elbow, бизнес-интерпретация сегментов, визуализация через PCA. Unsupervised learning без целевой переменной.

**GitHub description (1 строка):** Customer segmentation with K-Means clustering, elbow method and PCA visualization
**Topics:** machine-learning, clustering, kmeans, pca, customer-segmentation

## Структура
```
project5_customer_segmentation/
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
1. Синтетика: 420 клиентов, 4 поведенческих признака
2. Scaling (обязателен для KMeans)
3. Elbow-метод → K=4
4. Кластеризация и таблица-портрет сегментов
5. PCA-визуализация 4D→2D

## Результаты
Найдены 4 интерпретируемых сегмента (VIP, экономные, студенты, средние) с разными стратегиями работы.

## Идеи улучшения
- Silhouette score как второй критерий выбора K
- DBSCAN для кластеров сложной формы
- RFM-анализ (recency/frequency/monetary) на реальных транзакциях
- Дашборд сегментов
