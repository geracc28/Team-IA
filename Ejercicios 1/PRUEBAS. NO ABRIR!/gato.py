# 1er versión, sólo incluye la interfaz del tablero
# Librerías
import tkinter as tk
from tkinter import *

# Se declara el diccionario que servira para colocar los valores en el tablero como casilla ocupada o no, se inicializa en 0s
casillas = dict(a0="0", a1="0", a2="0", a3="0", a4="0", a5="0", a6="0", a7="0", a8="0")

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
    # Funcion para poder terminar la ejecucion, se coloca de forma anidada para no tener que pasar por referencia "ventana" 
    def salirJuego():
        ventana.destroy()
    # Se declaran los botones de salir y jugar
    botonSalir = tk.Button(ventana, text="Salir", command=salirJuego, bg="khaki", fg="black",font=("Courier New", 25, "bold"), width=8, height=3)
    botonSalir.place(x=625, y=300)
    botonJugar = tk.Button(ventana, text="Jugar", command=limpiaTablero,  bg="sandybrown", fg="black", font=("Courier New", 25, "bold"), width=8, height=3)
    botonJugar.place(x=625, y=100)
    # Mantiene la ventana abierta
    ventana.mainloop()

# Esta funcion se utiliza para inicializar el juego, colocar todo en 0s, se debe llamar por el boton de jugar
def limpiaTablero():
    print("Los valores de las casillas quedaron: ")
    print(casillas)
    # Se itera sobre el diccionario en claves y valores para colocar todo en un solo valor
    for clave, valor in casillas.items():
        casillas[clave] = "1"
    print("Los valores de las casillas son: ")
    print(casillas)


# Funcion principal
def main():
    print("")
    # Se crea ventana principal
    dibujaTablero()
    
    

# Ayuda a definir la funcion main
if __name__ == "__main__":
    main()
