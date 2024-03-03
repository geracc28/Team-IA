# 1er versión, sólo incluye la interfaz del tablero
# Librerías
import tkinter as tk
from tkinter import *

# Esta funcion se encarga de comenzar el tablero en blanco
def dibujaTablero():
    ventana = tk.Tk()
    ventana.title("Tic Tac Toe")
    ventana.geometry("800x600+10+50")
    # Se crea la interfaz del tablero
    canvas = tk.Canvas(ventana, width=800, height=600, background='goldenrod')
    canvas.pack() # Manejador de lo que le coloquemos a la ventana
    # Lineas de tablero
    canvas.create_line(200,0,200,600, width=5, fill='gold')
    canvas.create_line(400,0,400,600, width=5, fill='gold')
    canvas.create_line(0,200,600,200, width=5, fill='gold')
    canvas.create_line(0,400,600,400, width=5, fill='gold')
    # Linea separadora
    canvas.create_line(600,0,600,600, fill="gainsboro")
    # Se declaran los botones de salir y jugar
    botonSalir = tk.Button(ventana, text="Salir", bg="khaki", fg="black",font=("Courier New", 25, "bold"), width=8, height=3)
    botonSalir.place(x=625, y=300)
    botonJugar = tk.Button(ventana, text="Jugar", bg="sandybrown", fg="black", font=("Courier New", 25, "bold"), width=8, height=3)
    botonJugar.place(x=625, y=100)
    # Mantiene la ventana abierta
    ventana.mainloop()


# Funcion principal
def main():
    print("")
    # Se crea ventana principal
    dibujaTablero()
    
    

# Ayuda a definir la funcion main
if __name__ == "__main__":
    main()
