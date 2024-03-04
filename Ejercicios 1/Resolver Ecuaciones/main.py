import numpy as np

#Creamos una matriz A que contiene los coeficientes de las ecuaciones del sistema. 
#Cada fila de la matriz representa una ecuación y 
#cada columna representa los coeficientes de una incógnita de esas ecuaciones.

A = np.array([[16, -6, 4, 1],
              [1, -8, 1, 1],
              [16, 2, -4, 1],
              [9, 8, -3, 1]])

#Creamos un vector B que contiene los términos independientes de cada ecuación. 
#Estos son los valores de los resultados en cada ecuación.

B = np.array([-36, -64, -4, -64])

#Utilizamos la función np.linalg.solve, que toma dos argumentos: 
#La matriz de coeficientes A y el vector de resultados B.
#Esta función devuelve un array con las soluciones para cada incógnita.

def resolver_sistema_ecuaciones(A, B):
    """
    Resuelve un sistema de ecuaciones lineales Ax = B usando el método de eliminación de Gauss.
    A: Matriz de coeficientes del sistema.
    B: Vector de términos independientes.
    Retorna: Vector solución x.
    """
    A = A.astype(float)  # Asegurar que A es de tipo float
    B = B.astype(float)  # Asegurar que B es de tipo float
    n = len(B)
    M = np.hstack((A, B.reshape(-1, 1)))  # Crear matriz aumentada

    # Eliminación hacia adelante
    for i in range(n):
        M[i] = M[i] / M[i,i]  # Normalizar la fila i
        for j in range(i + 1, n):
            M[j] = M[j] - M[j,i] * M[i]  # Eliminar elemento j debajo de i

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = M[i,n] - np.dot(M[i,i + 1:n], x[i + 1:n])

    return x

solucion_np = resolver_sistema_ecuaciones(A, B)

print(solucion_np)