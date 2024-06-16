from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
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
    'MLP Hold-Out 70/30 Accuracy': [],
    'MLP 10-Fold CV Accuracy': [],
    'RBF Hold-Out 70/30 Accuracy': [],
    'RBF 10-Fold CV Accuracy': [],
    'MLP Hold-Out 70/30 Confusion Matrix': [],
    'MLP 10-Fold CV Confusion Matrix': [],
    'RBF Hold-Out 70/30 Confusion Matrix': [],
    'RBF 10-Fold CV Confusion Matrix': []
}

# Procesar cada conjunto de datos
for name, (X, y) in datasets.items():
    # Asegurarse de que las etiquetas estén en formato numérico usando LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y.values.ravel())  # Convertir y a un array de NumPy y asegurarse de que sea 1D

    # División Hold-Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Estandarizar las características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Perceptrón Multicapa (MLP)
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000, random_state=42)
    mlp.fit(X_train, y_train)  # Entrenar el clasificador con los datos de entrenamiento
    
    # Precisión y Matriz de Confusión para Hold-Out 70/30
    y_pred_mlp = mlp.predict(X_test)
    accuracy_mlp_holdout = accuracy_score(y_test, y_pred_mlp) * 100  # Calcular la precisión
    confusion_mlp_holdout = confusion_matrix(y_test, y_pred_mlp)  # Calcular la matriz de confusión
    
    # Precisión para Validación Cruzada con 10 Pliegues
    accuracy_mlp_cv = cross_val_score(mlp, X, y, cv=10).mean() * 100  # Calcular la precisión promedio con validación cruzada
    
    # Red Neuronal de Base Radial (RBF) usando SVC_______________________________________
    rbf = SVC(kernel='rbf', random_state=42)
    rbf.fit(X_train, y_train)  # Entrenar el clasificador
    
    # Precisión y Matriz de Confusión para Hold-Out 70/30
    y_pred_rbf = rbf.predict(X_test)
    accuracy_rbf_holdout = accuracy_score(y_test, y_pred_rbf) * 100  # Calcular la precisión
    confusion_rbf_holdout = confusion_matrix(y_test, y_pred_rbf)  # Calcular la matriz de confusión
    
    # Precisión para Validación Cruzada con 10 Pliegues
    accuracy_rbf_cv = cross_val_score(rbf, X, y, cv=10).mean() * 100  # Calcular la precisión promedio con validación cruzada
    
    # Recopilar los resultados
    results['Dataset'].append(name)
    results['MLP Hold-Out 70/30 Accuracy'].append(accuracy_mlp_holdout)
    results['MLP 10-Fold CV Accuracy'].append(accuracy_mlp_cv)
    results['RBF Hold-Out 70/30 Accuracy'].append(accuracy_rbf_holdout)
    results['RBF 10-Fold CV Accuracy'].append(accuracy_rbf_cv)
    results['MLP Hold-Out 70/30 Confusion Matrix'].append(confusion_mlp_holdout)
    results['MLP 10-Fold CV Confusion Matrix'].append(None)  # La matriz de confusión no se usa típicamente con CV
    results['RBF Hold-Out 70/30 Confusion Matrix'].append(confusion_rbf_holdout)
    results['RBF 10-Fold CV Confusion Matrix'].append(None)  # La matriz de confusión no se usa típicamente con CV

# Convertir los resultados a un DataFrame para una mejor visualización
results_df = pd.DataFrame(results)

# Visualizar los resultados
print(results_df)

# Si quieres guardar los resultados en un archivo CSV
results_df.to_csv("classification_results_.csv", index=False)
