from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# Obtener conjuntos de datos del Repositorio de Machine Learning de UCI
iris = fetch_ucirepo(id=53)  # Conjunto de datos Iris
wine = fetch_ucirepo(id=109)  # Conjunto de datos Wine
breast_cancer = fetch_ucirepo(id=17)  # Conjunto de datos Breast Cancer Wisconsin (Diagnóstico)

# Convertir los conjuntos de datos a DataFrames de pandas
datasets = {
    'Iris': (iris.data.features, iris.data.targets),
    'Wine': (wine.data.features, wine.data.targets),
    'Breast Cancer': (breast_cancer.data.features, breast_cancer.data.targets)
}

# Inicializar un diccionario para almacenar los resultados
results = {
    'Dataset': [],
    '1-NN Hold-Out 70/30 Accuracy': [],
    '1-NN 10-Fold CV Accuracy': [],
    'K-NN Hold-Out 70/30 Accuracy': [],
    'K-NN 10-Fold CV Accuracy': [],
    'Best K': [],
    '1-NN Hold-Out 70/30 Confusion Matrix': [],
    '1-NN 10-Fold CV Confusion Matrix': [],
    'K-NN Hold-Out 70/30 Confusion Matrix': [],
    'K-NN 10-Fold CV Confusion Matrix': []
}

# Procesar cada conjunto de datos
for name, (X, y) in datasets.items():
    # Asegurarse de que las etiquetas estén en formato numérico usando LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y.values.ravel())  # Convertir y a un array de NumPy y asegurarse de que sea 1D
    
    # División Hold-Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Clasificador 1-NN
    knn_1 = KNeighborsClassifier(n_neighbors=1)
    knn_1.fit(X_train, y_train)  # Entrenar el clasificador con los datos de entrenamiento
    
    # Precisión y Matriz de Confusión para Hold-Out 70/30
    y_pred_1 = knn_1.predict(X_test)
    accuracy_1_holdout = accuracy_score(y_test, y_pred_1) * 100  # Calcular la precisión
    confusion_1_holdout = confusion_matrix(y_test, y_pred_1)  # Calcular la matriz de confusión
    
    # Precisión para Validación Cruzada con 10 Pliegues
    accuracy_1_cv = cross_val_score(knn_1, X, y, cv=10).mean() * 100  # Calcular la precisión promedio con validación cruzada
    
    # Encontrar el mejor K para K-NN usando GridSearchCV
    param_grid = {'n_neighbors': np.arange(3, 12)}
    knn = KNeighborsClassifier()
    knn_gs = GridSearchCV(knn, param_grid, cv=10)  # Usar GridSearchCV para encontrar el mejor valor de K
    knn_gs.fit(X_train, y_train)
    best_k = knn_gs.best_params_['n_neighbors']  # Obtener el mejor valor de K
    
    # Clasificador K-NN con el mejor K
    knn_best = KNeighborsClassifier(n_neighbors=best_k)
    knn_best.fit(X_train, y_train)  # Entrenar el clasificador con el mejor K
    
    # Precisión y Matriz de Confusión para Hold-Out 70/30
    y_pred_best = knn_best.predict(X_test)
    accuracy_best_holdout = accuracy_score(y_test, y_pred_best) * 100  # Calcular la precisión
    confusion_best_holdout = confusion_matrix(y_test, y_pred_best)  # Calcular la matriz de confusión
    
    # Precisión para Validación Cruzada con 10 Pliegues
    accuracy_best_cv = cross_val_score(knn_best, X, y, cv=10).mean() * 100  # Calcular la precisión promedio con validación cruzada
    
    # Recopilar los resultados
    results['Dataset'].append(name)
    results['1-NN Hold-Out 70/30 Accuracy'].append(accuracy_1_holdout)
    results['1-NN 10-Fold CV Accuracy'].append(accuracy_1_cv)
    results['K-NN Hold-Out 70/30 Accuracy'].append(accuracy_best_holdout)
    results['K-NN 10-Fold CV Accuracy'].append(accuracy_best_cv)
    results['Best K'].append(best_k)
    results['1-NN Hold-Out 70/30 Confusion Matrix'].append(confusion_1_holdout)
    results['1-NN 10-Fold CV Confusion Matrix'].append(None)  # La matriz de confusión no se usa típicamente con CV
    results['K-NN Hold-Out 70/30 Confusion Matrix'].append(confusion_best_holdout)
    results['K-NN 10-Fold CV Confusion Matrix'].append(None)  # La matriz de confusión no se usa típicamente con CV

# Convertir los resultados a un DataFrame para una mejor visualización
results_df = pd.DataFrame(results)

# Visualizar los resultados
print(results_df)

# Si quieres guardar los resultados en un archivo CSV
results_df.to_csv("classification_results.csv", index=False)

