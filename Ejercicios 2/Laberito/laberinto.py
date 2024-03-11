# Práctica de laberinto con búsqueda profunda
# Estructura con características de pila Last in First Out

import time

def solve_maze(maze, start, end):
    stack = [start]
    while stack:
        x, y = stack[-1]

        # If reached the end point
        if (x, y) == end:
            return True, stack

        # Mark as visited
        maze[x][y] = '2'
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()

    return False, []


if __name__ == "__main__":
    start_time = time.time()
    # 0 = open path, 1 = wall, S = start, E = end
    maze = [
        ['1', '1', '1', '1', '1','1','1','1','1','1'],
        ['S', '0', '0', '0', '0','1','0','1','1','1'],
        ['1', '0', '1', '0', '1','0','0','0','0','1'],
        ['1', '0', '1', '1', '0','0','0','1','1','1'],
        ['1', '0', '0', '0', '0','1','0','0','0','1'],
        ['1', '0', '1', '0', '0','1','0','1','1','1'],
        ['1', '0', '1', '1', '1','1','0','0','0','1'],
        ['1', '0', '1', '0', '0','1','0','1','0','1'],
        ['1', '0', '0', '0', '0','1','0','0','E','1'],
        ['1', '1', '1', '1', '1','1','1','1','1','1']
    ]
    start = (1, 0)
    end = (8, 8)
    solved, path = solve_maze(maze, start, end)
    mazeunsolved = [
        ['1', '1', '1', '1', '1','1','1','1','1','1'],
        ['S', '0', '0', '0', '0','1','0','1','1','E'],
        ['1', '0', '1', '0', '1','0','0','0','0','1'],
        ['1', '0', '1', '1', '0','0','0','1','1','1'],
        ['1', '0', '0', '0', '0','1','0','0','0','1'],
        ['1', '0', '1', '0', '0','1','0','1','1','1'],
        ['1', '0', '1', '1', '1','1','0','0','0','1'],
        ['1', '0', '1', '0', '0','1','0','1','0','1'],
        ['1', '0', '0', '0', '0','1','0','0','1','1'],
        ['1', '1', '1', '1', '1','1','1','1','1','1']
    ]
    startuns = (2,0)
    enduns = (1,9)
    unsolved, path2 = solve_maze(mazeunsolved, startuns, enduns)
    print("First Maze\n")
    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

    print("\nSecond Maze\n")
    if unsolved:
        print("Maze Solved!")
        for x, y in path2:
            if mazeunsolved[x][y] != 'S' and mazeunsolved[x][y] != 'E':
                mazeunsolved[x][y] = '*'
        for row in mazeunsolved:
            print("".join(row))
    else:
        print("No solution found.")
    end_time = time.time()
    print(f"The execution time was: {end_time - start_time} seconds")
# Comentarios
''' Para poder colocar un laberinto sin solución se tuvo que hacer un segundo laberinto con las
mismas líneas de frontera y cambiando el objetivo de lugar, en este caso "E"
La solución que se nos propone puede no ser la más rápida, pero sí la que encuentra primero
Considerablemente, el retroceso y avance en cada casilla hacen que el número de iteraciones se 
duplique, con el tiempo la diferencia tiene que ver con milisegundos, pero con un poco de suerte 
para la computadora al buscar la solución, puede que a la primera se encuentre con el 
recorrido solución.
El tiempo de la primera versión del código proporcionada por el profesor con un laberinto de 5x5 fue:
0.005918025970458984 seconds
Para la versión de 7x7 fue: 0.004004478454589844 seconds
Y para la versión más extendida de 10x10 fue: 0.010125160217285156 seconds

Pruebas Mark 
Para la version 5x5 de tres pruebas respectivamente el tiempo fue: 0.00010561943054199219 seconds, 0.0001671314239501953 seconds, 0.00020837783813476562
Para la version 10x10 de tres pruebas respectivamente el tiempo fue: 0.00037026405334472656 seconds, 0.0006749629974365234 seconds, 0.00042557716369628906 seconds

'''
