#Juego sin interfaz decente 
import time
import random
import os

#Funcion para iniciar el juego
def iniciar_juego():
    persona = 'X'
    computador = 'O'
    return persona, computador
#definir la matriz con metodo format
def tablero(matriz):
    print("MICHI TONTO\n")
    print("1 {} |2 {} |3 {}".format(matriz[0], matriz[1], matriz[2]))
    print("   |   |   ")
    print("-----------")
    print("4 {} |5 {} |6 {}".format(matriz[3], matriz[4], matriz[5]))
    print("   |   |   ")
    print("-----------")
    print("7 {} |8 {} |9 {}".format(matriz[6], matriz[7], matriz[8]))
    print("   |   |   \n")

#función cuando se finaliza una partida por empate
def empate(matriz):
    return " " not in matriz

#Definir las posiciones para ganar 
def ganar(matriz):
    ganar_condiciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    for a, b, c in ganar_condiciones:
        if matriz[a] == matriz[b] == matriz[c] and matriz[a] != " ":
            return True
    return False

def movimiento_jugador(matriz, persona):
    while True:
        try:
            casilla = int(input("Seleccione casilla (1-9): "))
            if casilla in range(1, 10) and matriz[casilla-1] == " ":
                matriz[casilla-1] = persona
                break
            else:
                print("Casilla no válida o ya está ocupada.")
        except ValueError:
            print("Introduce un número válido, no seas macaco")

def movimiento_computador(matriz, computador):
    posiciones_vacias = [i for i, x in enumerate(matriz) if x == " "]
    if posiciones_vacias:
        casilla = random.choice(posiciones_vacias)
        matriz[casilla] = computador
#Definir desarrollo de las partidas 
def juego():
    while True:
        matriz = [" "] * 9
        os.system("cls" if os.name == "nt" else "clear")
        persona, computador = iniciar_juego()
        turno = 0

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            tablero(matriz)

            if ganar(matriz):
                if turno % 2 == 0:
                    print("**Gana la Computadora**")
                else:
                    print("**Gana el Jugador**")
                break
            elif empate(matriz):
                print("**Empate**")
                break

            if turno % 2 == 0:
                movimiento_jugador(matriz, persona)
            else:
                movimiento_computador(matriz, computador)

            turno += 1

        print("**Fin del Juego**\nReiniciando...")
        time.sleep(5)
        #break  

if __name__ == "__main__":
    juego()
