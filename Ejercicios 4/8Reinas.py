def nReinas(matriz): 
# Comprueba si el tablero está vacío
    flag = 0
    for fila in matriz:
        for casilla in fila:
            if casilla == "R":
                flag +=1
    return flag

def llenaDiagonales(fila, columna, matriz):
    tam = len(matriz)
    # Superior izq
    for i, j in zip(range(fila-1, -1, -1), range(columna-1, -1, -1)):
        if matriz[i][j] != "R":
            matriz[i][j] = "-"
    # Superior der
    for i, j in zip(range(fila-1, -1, -1), range(columna+1, tam)):
        if matriz[i][j] != "R":
            matriz[i][j] = "-"
    # Inferior izq
    for i, j in zip(range(fila+1, tam), range(columna-1, -1, -1)):
        if matriz[i][j] != "R":
            matriz[i][j] = "-"
    # Inferior der
    for i, j in zip(range(fila+1, tam), range(columna+1, tam)):
        if matriz[i][j] != "R":
            matriz[i][j] = "-"

def imprimir_matriz(matriz):
    print("")
    for fila in matriz:
        fila_formateada = ' '.join(map(str, fila))
        print(fila_formateada)

def colocaReina(fila, columna, matriz):
    # Cambia valores en fila
    for casilla in range(len(matriz[fila])):
        if matriz[fila][casilla] != "R":
            matriz[fila][casilla] = "-"
    # Cambia valores en columna
    for casilla in range(len(matriz)):
        if matriz[casilla][columna] != "R":
            matriz[casilla][columna] = "-"
    # Cambiar valores de la diagonal
    llenaDiagonales(fila, columna, matriz)
    """for casilla in range(len(matriz)):
        if matriz[casilla][casilla] != "R":
            matriz[casilla][casilla] = "-"""
    #print("Coloca reina en f:", fila,"c:", columna)
    matriz[fila][columna] = "R"
    # imprimir_matriz(matriz)
    # Coloca a la reina en el tablero


def tableroBlanco(matriz):
    for fila in matriz:
        for i in range(len(fila)):
            fila[i] = 0

if __name__ == "__main__":
    print("Juego de las 8-reinas")
    #Inicializa el tablero con 0 reinas
    tablero = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    reinasT = 0
    fila = 0
    columna = 0
    posPR_f = 0
    posPR_c = 0
    primeraIteracion = True
    # Comienza a colocar reinas
    print("")
    while reinasT < 8:
        if primeraIteracion:
            tableroBlanco(tablero)
            primeraIteracion = False
        while fila < len(tablero):
            #print("La posicion [",fila, columna,"] esta desocupada?")
            if tablero[fila][columna] == 0:
                colocaReina(fila, columna, tablero)
                reinasT = nReinas(tablero)
                if(posPR_c != 0):
                    columna = 0
                    # columna += 1
                else:
                    columna += 1
                if columna >= len(tablero):
                    columna = 0
                break
            fila += 1
        if fila >= len(tablero):
            columna += 1
        if fila and columna >= len(tablero):
            if reinasT < 8:
                tableroBlanco(tablero)
                posPR_f += 1
                if posPR_f >= len(tablero):
                    posPR_f = 0
                    posPR_c += 1
                #print("La Reina se pondra en: (", posPR_f, posPR_c, ")")
                #input()
                fila = posPR_f
                columna = posPR_c
        else:
            fila = 0
        print("+_______________________________________________+")
        imprimir_matriz(tablero)
    print("Si!!! Encontré la solución")         
    """"        
        for columna in range(len(tablero)):
            if tablero[fila][columna] == 0:
                colocaReina(fila, columna, tablero)
                reinasT = nReinas(tablero)
                break
        fila += 1
  
        if nReinas(tablero) < 8:
            tableroBlanco(tablero)
            columna = 0
            for fila in range(len(tablero)):
                if tablero[fila][columna] == 0:
                    colocaReina(fila, columna, tablero)
                    break
"""