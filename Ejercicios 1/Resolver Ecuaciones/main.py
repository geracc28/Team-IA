import numpy as np

def random_search(A, B, num_iterations=1000000, tolerancia=10):
    """
    Resuelve un sistema de ecuaciones mediante búsqueda aleatoria.

    :param A: Matriz de coeficientes del sistema de ecuaciones.
    :param B: Vector de términos independientes de las ecuaciones.
    :param num_iterations: Número de iteraciones para la búsqueda aleatoria.
    :param tolerance: Tolerancia para considerar que una solución es válida.
    :return: Una aproximación a la solución del sistema.
    """
    # Dimensiones del sistema
    num_variables = A.shape[1]

    # Mejor solución encontrada y su error asociado
    mejor_solucion = None
    mejor_error = np.inf

    for _ in range(num_iterations):
        # Generar un conjunto aleatorio de valores para las variables
        random_solution = np.random.rand(num_variables) * 100 - 100  # Rango de -100 a 100

        # Calcular el resultado con la solución aleatoria
        result = np.dot(A, random_solution)

        # Calcular el error como la norma del vector diferencia
        error = np.linalg.norm(result - B)

        # Si el error es menor que el mejor encontrado o está dentro de la tolerancia, actualizar la mejor solución
        if error < mejor_error and error < tolerancia:
            mejor_solucion = random_solution
            mejor_error = error

    return mejor_solucion

# Matriz de coeficientes del sistema
A = np.array([[16, -6, 4, 1],
              [1, -8, 1, 1],
              [16, 2, -4, 1],
              [9, 8, -3, 1]])

# Vector de términos independientes
B = np.array([-36, -64, -4, -64])

# Resolver el sistema
solucion = random_search(A, B)
if solucion is not None:
    print("Solución aproximada encontrada:", solucion)
else:
    print("No se encontró una solución en el número de iteraciones dado.")

