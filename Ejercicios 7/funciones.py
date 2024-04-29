import pandas as pd

# Cargar los datos desde un archivo .data
def cargar_datos(filepath):
    # Se asume que las columnas son longitud_del_sépalo, ancho_del_sépalo, longitud_del_pétalo, ancho_del_pétalo, especie
    column_names = ['longitud_del_sépalo', 'ancho_del_sépalo', 'longitud_del_pétalo', 'ancho_del_pétalo', 'especie']
    data = pd.read_csv(filepath, header=None, names=column_names)
    return data

# Calcular estadísticas: promedio, varianza y desviación estándar
def calcular_estadisticas(data):
    stats = data.describe().loc[['mean', 'std']]
    stats.loc['var'] = data.var()
    return stats

# Separar datos por categorías y calcular estadísticas para cada una
def estadisticas_por_categoria(data):
    categories = data['especie'].unique()
    category_stats = {}
    for category in categories:
        category_data = data[data['especie'] == category]
        category_stats[category] = calcular_estadisticas(category_data.iloc[:, :-1])  # Excluir columna de especie
    return category_stats

#Ayuda a la traduccion para la representacion de datos
def traducir_indices(dataframe):
    traducciones = {
        'mean': 'Promedio',
        'std': 'Desviación estándar',
        'var': 'Varianza'
    }
    dataframe.index = [traducciones.get(item, item) for item in dataframe.index]
    return dataframe
