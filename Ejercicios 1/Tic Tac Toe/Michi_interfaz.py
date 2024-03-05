# Integrantes del equipo
#   Cervantes Cocom Gerardo Onasis
#   Díaz Pérez Ailyn Magali
#   Luna Márquez José Antonio
#   Salinas Monroy America Joana 

#fusion de codigo de Maga y mio, aún no terminado, le faltan afinar detallitos
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
def movimiento_jugador(matriz, casilla, persona):
    if matriz[casilla] == " ":
        matriz[casilla] = persona

# Función para el movimiento del computador
def movimiento_computador(matriz, computador):
    posiciones_vacias = [i for i, x in enumerate(matriz) if x == " "]
    if posiciones_vacias:
        casilla = random.choice(posiciones_vacias) #se posiciona en casillas vacías aleatorias
        matriz[casilla] = computador

# Función para reiniciar el juego
def reiniciar_juego():
    return [" "] * 9

# Función para dibujar el tablero
def dibuja_tablero(canvas, matriz):
    canvas.delete("all")
    canvas.create_line(200, 0, 200, 600, width=5, fill='gold')
    canvas.create_line(400, 0, 400, 600, width=5, fill='gold')
    canvas.create_line(0, 200, 600, 200, width=5, fill='gold')
    canvas.create_line(0, 400, 600, 400, width=5, fill='gold')
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            x = j * 200 + 100
            y = i * 200 + 100
            canvas.create_text(x, y, text=matriz[index], font=("Courier New", 100, "bold"), fill="black")

# Función para manejar el clic en la casilla
def clic_casilla(event):
    global turno
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

    movimiento_jugador(matriz, casilla, persona)
    turno += 1
    if not juego(matriz, turno, persona, computador):
        movimiento_computador(matriz, computador)
        turno += 1
        juego(matriz, turno, persona, computador)
    dibuja_tablero(canvas, matriz)

# Función principal para el desarrollo del juego
def juego(matriz, turno, persona, computador):
    if ganar(matriz):
        print("**Gana el Jugador**" if (turno - 1) % 2 == 0 else "**Gana el Computador**")
        return True
    elif empate(matriz):
        print("**Empate**")
        return True

    return False

# Función para reiniciar el juego y limpiar el tablero
def reiniciar():
    global matriz, turno
    matriz = reiniciar_juego()
    turno = 0
    dibuja_tablero(canvas, matriz)

# Función para cerrar la ventana
def salir():
    ventana.destroy()

# Función principal
def main():
    global matriz, turno, persona, computador, canvas, ventana
    ventana = tk.Tk()
    ventana.title("Michi Tonto")
    ventana.geometry("600x625+10+50")
    canvas = tk.Canvas(ventana, width=600, height=600, background='goldenrod')
    canvas.pack()

    boton_jugar = Button(ventana, text="Reiniciar", command=reiniciar)
    boton_jugar.pack(side=LEFT)

    boton_salir = Button(ventana, text="Salir", command=salir)
    boton_salir.pack(side=RIGHT)

    matriz = reiniciar_juego()
    persona, computador = iniciar_juego()
    turno = 0

    dibuja_tablero(canvas, matriz)
    canvas.bind("<Button-1>", clic_casilla)
    ventana.mainloop()

if __name__ == "__main__":
    main()
