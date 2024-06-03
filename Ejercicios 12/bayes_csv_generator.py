import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.naive_bayes import CategoricalNB

def cargar_y_clasificar(cargador_de_dataset, clasificador, discretizar=False):
    data = cargador_de_dataset()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    
    if discretizar:
        discretizador = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform', subsample=None)
        X_train = discretizador.fit_transform(X_train)
        X_test = discretizador.transform(X_test)
    
    clf = clasificador()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    # Uso de pandas para mostrar la matriz de confusión de manera bonita
    cm_df = pd.DataFrame(cm, index=data.target_names, columns=data.target_names)
    
    return acc, cm_df

clasificadores = {
    'Naive Bayes': (GaussianNB, False),
    'Redes Bayesianas': (CategoricalNB, True)
}

datasets = {
    'Iris': load_iris,
    'Wine': load_wine,
    'Breast Cancer': load_breast_cancer
}

# Crear DataFrame para almacenar los resultados
resultados_df = pd.DataFrame()

for nombre, cargador in datasets.items():
    for nombre_clf, (clf, discretizar) in clasificadores.items():
        precisión, matriz_conf = cargar_y_clasificar(cargador, clf, discretizar)
        resultados_df = resultados_df._append({
            'Dataset': nombre,
            'Clasificador': nombre_clf,
            'Precisión': precisión,
            'Matriz de Confusión': matriz_conf.to_string()
        }, ignore_index=True)

# Guardar los resultados en un archivo CSV
resultados_df.to_csv('resultados_clasificacion.csv', index=False)

print("Los resultados han sido guardados en 'resultados_clasificacion.csv'")
