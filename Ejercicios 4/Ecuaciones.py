import math
import random

# Funciones a optimizar
def f1(x):
    return x**4 + 3*x**3 + 2*x**2 - 1
def f2(x):
    return x**2 - 3*x - 8

# Función de enfriamiento
def enfriar(temperatura):
    return temperatura * 0.9

# Fórmula de templado simulado
def probabilidad_aceptacion(delta_evaluacion, temperatura):
    if delta_evaluacion < 0:
        return 1
    return math.exp(-delta_evaluacion / temperatura)

# Función de recocido simulado
def simulated_annealing(funcion, temperatura_inicial, temperatura_minima, enfriamiento, iteraciones):
    temperatura = temperatura_inicial
    estado_actual = random.uniform(-10, 10)  # Estado inicial aleatorio
    mejor_estado = estado_actual

    while temperatura > temperatura_minima:
        for i in range(iteraciones):
            estado_nuevo = estado_actual + random.uniform(-0.1, 0.1)  # Generar un estado vecino
            evaluacion_actual = funcion(estado_actual)
            evaluacion_nueva = funcion(estado_nuevo)

            delta_evaluacion = evaluacion_nueva - evaluacion_actual

            if delta_evaluacion < 0 or random.random() < probabilidad_aceptacion(delta_evaluacion, temperatura):
                estado_actual = estado_nuevo

                # Actualizar el mejor estado encontrado
                if funcion(estado_actual) < funcion(mejor_estado):
                    mejor_estado = estado_actual

        temperatura = enfriar(temperatura)

    return mejor_estado, funcion(mejor_estado)

# Ejecutar el algoritmo para encontrar el mínimo de las funciones
minimo_f1, valor_minimo_f1 = simulated_annealing(f1, temperatura_inicial=100, temperatura_minima=0.1, enfriamiento=enfriar, iteraciones=1000)
minimo_f2, valor_minimo_f2 = simulated_annealing(f2, temperatura_inicial=100, temperatura_minima=0.1, enfriamiento=enfriar, iteraciones=1000)

print("Mínimo de la función f1(x) = x^4 + 3x^3 + 2x^2 - 1:", minimo_f1, "con valor mínimo:", valor_minimo_f1)
print("Mínimo de la función f2(x) = x^2 - 3x - 8:", minimo_f2, "con valor mínimo:", valor_minimo_f2)
