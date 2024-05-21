import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.metrics import accuracy_score

#Definir clasificador euclidiano
class EuclideanClassifier:
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_test):
        predictions = []
        for test_point in X_test:
            distances = np.linalg.norm(self.X_train - test_point, axis=1)
            nearest_neighbor_index = np.argmin(distances)
            predictions.append(self.y_train[nearest_neighbor_index])
        return np.array(predictions)
#Cargar conjunto de datos_________________________________________________________
#Conjunto de datos Iris
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# Cargar el conjunto de datos Breast Cancer
breast = load_breast_cancer()
X_breast, y_breast = breast.data, breast.target

#Hold out_________________________________________________________________________
def hold_out_validation(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = EuclideanClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Hold-Out Validation Accuracy: {accuracy:.2f}')

print("Iris Dataset:")
hold_out_validation(X_iris, y_iris)

print("\nBreast Cancer Dataset:")
hold_out_validation(X_breast, y_breast)

#10-Fold____________________________________________________________________
def cross_validation(X, y, k=10):
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    accuracies = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model = EuclideanClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
    mean_accuracy = np.mean(accuracies)
    print(f'{k}-Fold Cross-Validation Mean Accuracy: {mean_accuracy:.2f}')

print("Iris Dataset:")
cross_validation(X_iris, y_iris)

print("\nBreast Cancer Dataset:")
cross_validation(X_breast, y_breast)



