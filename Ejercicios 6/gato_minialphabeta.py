def iniciar():
    return [[' '] * 3 for _ in range(3)]

def mostrar_tablero(estado):
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print('{}|'.format(estado[i][j]), end='')
        print()
    print()

# Retorna:
# 'x' si x ganó
# 'o' si o ganó
# '-' si empataron
# ' ' si no terminó
def marcador(estado):
    # Chequeando victorias horizontales y verticales
    for i in range(3):
        if estado[i] == ['x'] * 3:
            return 'x'
        if estado[i] == ['o'] * 3:
            return 'o'
        if estado[0][i] != ' ' and estado[0][i] == estado[1][i] and estado[1][i] == estado[2][i]:
            return estado[0][i]

    # Chequeando la diagonal principal
    if estado[0][0] != ' ' and estado[0][0] == estado[1][1] and estado[1][1] == estado[2][2]:
        return estado[0][0]

    # Chequeando la diagonal invertida
    if estado[0][2] != ' ' and estado[0][2] == estado[1][1] and estado[1][1] == estado[2][0]:
        return estado[0][2]

    if ' ' not in estado[0] + estado[1] + estado[2]:
        return '-'

    return ' '

# Retorna una tupla siendo:
# 1er valor: puntaje del estado
# 2do valor: posición del movimiento que resulta en el 1er valor
def jugar_max_alpha_beta(estado, alfa, beta):
    final = marcador(estado)
    if final == 'x':
        return (1, (-1, -1))
    if final == 'o':
        return (-1, (-1, -1))
    if final == '-':
        return (0, (-1, -1))

    mayor = -2
    for i in range(3):
        for j in range(3):
            if estado[i][j] == ' ':
                estado[i][j] = 'x'
                (puntaje, (mov_x, mov_y)) = jugar_min_alpha_beta(estado, alfa, beta)
                if puntaje > mayor:
                    mayor = puntaje
                    mejor_movimiento = (i, j)
                estado[i][j] = ' '
                alfa = max(alfa, puntaje)
                if beta <= alfa:
                    break

    return (mayor, mejor_movimiento)

def jugar_min_alpha_beta(estado, alfa, beta):
    final = marcador(estado)
    if final == 'x':
        return (1, (-1, -1))
    if final == 'o':
        return (-1, (-1, -1))
    if final == '-':
        return (0, (-1, -1))

    menor = 2
    for i in range(3):
        for j in range(3):
            if estado[i][j] == ' ':
                estado[i][j] = 'o'
                (puntaje, (mov_x, mov_y)) = jugar_max_alpha_beta(estado, alfa, beta)
                if puntaje < menor:
                    menor = puntaje
                    mejor_movimiento = (i, j)
                estado[i][j] = ' '
                beta = min(beta, puntaje)
                if beta <= alfa:
                    break

    return (menor, mejor_movimiento)

def jugar_ia_vs_humano_alpha_beta(estado):
    humano(estado)  # Turno del jugador
    mostrar_tablero(estado)
    puntaje, movimiento = jugar_min_alpha_beta(estado, float("-inf"), float("inf"))  # Turno de la IA
    estado[movimiento[0]][movimiento[1]] = 'o'
    mostrar_tablero(estado)

    final = marcador(estado)
    if final == 'x':
        print("¡Has ganado!")
    elif final == 'o':
        print("¡La IA ha ganado!")
    elif final == '-':
        print("¡Ha sido un empate!")
    else:
        jugar_ia_vs_humano_alpha_beta(estado)

def humano(estado):
    # |1|2|3|
    # |4|5|6|
    # |7|8|9|

    count = 0
    check = int(input("Selecciona un campo disponible (valor 1-9):"))

    for i in range(3):
        for j in range(3):
            count = count + 1
            if count == check:
                if estado[i][j] != ' ':
                    print("Campo no disponible, intenta de nuevo:")
                    humano(estado)
                else:
                    estado[i][j] = 'x'

def jugar_ia_vs_ia_alpha_beta(estado):
    puntaje, movimiento = jugar_max_alpha_beta(estado, float("-inf"), float("inf"))  # Movimiento de la IA-X
    estado[movimiento[0]][movimiento[1]] = 'x'
    mostrar_tablero(estado)
    puntaje, movimiento = jugar_min_alpha_beta(estado, float("-inf"), float("inf"))  # Movimiento de la IA-O
    estado[movimiento[0]][movimiento[1]] = 'o'
    mostrar_tablero(estado)

    final = marcador(estado)
    if final == 'x':
        print("¡IA-X ha ganado!")
    elif final == 'o':
        print("¡IA-O ha ganado!")
    elif final == '-':
        print("¡Ha sido un empate!")
    else:
        jugar_ia_vs_ia_alpha_beta(estado)

def main():
    estado = iniciar()
    print("Elige uno de los modos a continuación:")
    print("1 - Jugar contra la IA")
    print("2 - Jugar IA vs IA")
    print("3 - Salir")
    opcion = int(input("Ingresa el código del modo que deseas:"))
    if opcion == 1:
        mostrar_tablero(estado)
        jugar_ia_vs_humano_alpha_beta(estado)
    elif opcion == 2:
        mostrar_tablero(estado)
        jugar_ia_vs_ia_alpha_beta(estado)
    elif opcion == 3:
        exit()
    else:
        print("Código inválido, intenta nuevamente:")
        main()

main()
