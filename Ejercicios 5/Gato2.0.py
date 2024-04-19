import tkinter as tk
from tkinter import *
import random

# Función para inicializar el juego
def iniciar_juego():
    persona = 'X'
    computador = 'O'
    return persona, computador

# Función para determinar si hay empate
def empate(matriz):
    return " " not in matriz

# Función para determinar las jugadas ganadoras
def ganar(matriz):
    ganar_condiciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    for a, b, c in ganar_condiciones:
        if matriz[a] == matriz[b] == matriz[c] and matriz[a] != " ":
            return True
    return False

# Función para el movimiento del jugador humano
def movimiento_jugador(matriz, casilla, persona, casillas_marcadas):
    matriz[casilla] = persona
    casillas_marcadas.append(casilla)
        
# Función para determinar el resultado del juego mediante una heurística
def resultado_heuristico(matriz):
    ganar_condiciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    
    puntaje_computadora = 0
    puntaje_persona = 0
    
    for a, b, c in ganar_condiciones:
        linea = [matriz[a], matriz[b], matriz[c]]
        count_computadora = linea.count(computador)
        count_persona = linea.count(persona)
        
        # Evaluar líneas abiertas y amenazas inminentes para la computadora
        if count_computadora == 2 and count_persona == 0:
            puntaje_computadora += 10
        elif count_computadora == 1 and count_persona == 0:
            puntaje_computadora += 1
        elif count_computadora == 0 and count_persona == 2:
            puntaje_persona += 10
        elif count_computadora == 0 and count_persona == 1:
            puntaje_persona += 1
            
    # Asignar puntajes adicionales basados en la importancia de las casillas
    puntajes_casillas = [0, 1, 2, 1, 2, 3, 2, 3, 4]
    for i, valor in enumerate(matriz):
        if valor == computador:
            puntaje_computadora += puntajes_casillas[i]
        elif valor == persona:
            puntaje_persona += puntajes_casillas[i]
            
    if puntaje_computadora > puntaje_persona:
        return 1 # Gana el Computador
    elif puntaje_persona > puntaje_computadora:
        return -1 # Gana el Jugador
    elif " " not in matriz:
        return 0 # Empate
    else:
        return 0 # En juego

def generar_todos_los_movimientos(matriz, turno, jugador):
    movimientos = []
    for i, casilla in enumerate(matriz):
        if casilla == " ":
            nueva_matriz = matriz.copy()
            nueva_matriz[i] = jugador
            movimientos.append((i, nueva_matriz))
            if not ganar(nueva_matriz) and " " in nueva_matriz:
                siguiente_turno = turno + 1
                siguiente_jugador = "X" if jugador == "O" else "O"
                movimientos += generar_todos_los_movimientos(nueva_matriz, siguiente_turno, siguiente_jugador)
    return movimientos

def elegir_mejor_movimiento(matriz, turno, jugador):
    movimientos = generar_todos_los_movimientos(matriz, turno, jugador)
    mejores_movimientos = []
    mejor_puntaje = float('-inf') if jugador == 'X' else float('inf')
    
    for movimiento in movimientos:
        _, nueva_matriz = movimiento
        puntaje = evaluar_movimiento(nueva_matriz)
        
        if (jugador == 'X' and puntaje > mejor_puntaje) or (jugador == 'O' and puntaje < mejor_puntaje):
            mejor_puntaje = puntaje
            mejores_movimientos = [movimiento]
        elif puntaje == mejor_puntaje:
            mejores_movimientos.append(movimiento)
            
    return random.choice(mejores_movimientos) if mejores_movimientos else None

def evaluar_movimiento(matriz):
    return resultado_heuristico(matriz)

# Función para el movimiento del computador
def movimiento_computador(matriz, computador):
    posiciones_vacias = [i for i, x in enumerate(matriz) if x == " "]
    # Primer cambio importante para hacer a la computadora inteligente
    posibles_mov = []
    for casilla in posiciones_vacias:
        nueva_matriz = matriz.copy()
        nueva_matriz[casilla] = computador
        posibles_mov.append((casilla, nueva_matriz))
    return posibles_mov

# Función para reiniciar el juego
def reiniciar_juego():
    return [" "] * 9

# Función para dibujar el tablero
def dibuja_tablero(canvas, matriz):
    canvas.delete("all")
    canvas.create_line(200, 0, 200, 600, width=5, fill='light blue')
    canvas.create_line(400, 0, 400, 600, width=5, fill='light blue')
    canvas.create_line(0, 200, 600, 200, width=5, fill='light blue')
    canvas.create_line(0, 400, 600, 400, width=5, fill='light blue')
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            x = j * 200 + 100
            y = i * 200 + 100
            canvas.create_text(x, y, text=matriz[index], font=("Courier New", 100, "bold"), fill="azure")

# Función para manejar el clic en la casilla
def clic_casilla(event):
    global turno, matriz
    x, y = event.x, event.y
    casilla = None
    if x < 200:
        if y < 200:
            casilla = 0
        elif y < 400:
            casilla = 3
        else:
            casilla = 6
    elif x < 400:
        if y < 200:
            casilla = 1
        elif y < 400:
            casilla = 4
        else:
            casilla = 7
    else:
        if y < 200:
            casilla = 2
        elif y < 400:
            casilla = 5
        else:
            casilla = 8
    if casilla not in casillas_marcadas:
        movimiento_jugador(matriz, casilla, persona, casillas_marcadas)
        turno += 1
        if not juego(matriz, turno):
            mejor_movimiento = elegir_mejor_movimiento(matriz, turno, computador)
            if mejor_movimiento:
                _, matriz = mejor_movimiento
                turno += 1
                juego(matriz, turno)
        dibuja_tablero(canvas, matriz)

# Función principal para el desarrollo del juego
def juego(matriz, turno):
    global casillas_marcadas
    ganador = ganar(matriz)
    if ganador:
        # Determinar el ganador basado en el turno actual
        if (turno - 1) % 2 == 0:
            print("**Gana el Jugador**")
        else:
            print("**Gana el Computador**")
        
        # Marcar todas las casillas vacías como ocupadas al final del juego
        posiciones_vacias = [i for i, x in enumerate(matriz) if x == " "]
        casillas_marcadas.extend(posiciones_vacias)
        return True
    elif empate(matriz):
        print("**Empate**")
        return True
    return False  # Continuar el juego si no hay ganador ni empate

# Función para reiniciar el juego y limpiar el tablero
def reiniciar():
    global matriz, turno, casillas_marcadas
    matriz = reiniciar_juego()
    turno = 0
    dibuja_tablero(canvas, matriz)
    casillas_marcadas = []

# Función para cerrar la ventana
def salir():
    ventana.destroy()

# Función principal
def main():
    global matriz, turno, persona, computador, canvas, ventana, casillas_marcadas
    ventana = tk.Tk()
    ventana.title("Michi Inteligente")
    ventana.geometry("600x625+10+50")
    canvas = tk.Canvas(ventana, width=600, height=600, background='deepskyblue')
    canvas.pack()

    boton_jugar = Button(ventana, text="Reiniciar", command=reiniciar)
    boton_jugar.pack(side=LEFT)

    boton_salir = Button(ventana, text="Salir", command=salir)
    boton_salir.pack(side=RIGHT)

    matriz = reiniciar_juego()
    persona, computador = iniciar_juego()
    turno = 0
    casillas_marcadas = []

    dibuja_tablero(canvas, matriz)
    canvas.bind("<Button-1>", clic_casilla)
    ventana.mainloop()

if __name__ == "__main__":
    main()