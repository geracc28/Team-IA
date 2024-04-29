from JFIleChoose import seleccionar_archivo_o_directorio as archivo
from funciones import *
import os

# Ruta al archivo .data
file_path = archivo()

# Ejecutar las funciones
data = cargar_datos(file_path)
stats_general = calcular_estadisticas(data.iloc[:, :-1])  # Excluir la columna de especie para cálculos generales
stats_por_categoria = estadisticas_por_categoria(data)

# Mostrar resultados
print("Estadísticas Generales:\n", traducir_indices(stats_general))
print("\nEstadísticas por Categoría:")
for especie, stats in stats_por_categoria.items():
    print(f"\n{especie}:\n{traducir_indices(stats)}")


#Creamos una ruta para los archivos CSV
ruta_estadisticas = "Estadisticas/"
if not os.path.exists(ruta_estadisticas):
    os.makedirs(ruta_estadisticas)

# Opcional: Guardar los resultados en un archivo CSV
stats_general.to_csv(f'{ruta_estadisticas}estadisticas_generales.csv')
for especie, stats in stats_por_categoria.items():
    stats.to_csv(f'{ruta_estadisticas}estadisticas_{especie}.csv')

