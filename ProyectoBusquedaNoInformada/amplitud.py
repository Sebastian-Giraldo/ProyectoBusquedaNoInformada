from collections import deque

def bfs(matriz):
    inicio = None
    meta = None

    # Encontrar la posición del agente buscador y la meta
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == 4:
                inicio = (i, j)
            elif matriz[i][j] == 5:
                meta = (i, j)

    # definimos una cola para almacenar los nodos que se van visitando
    cola = deque([(inicio, [inicio])])
    # definimos un conjunto para almacenar las posiciones ya visitadas
    visitados = set([inicio])

    # definimos un diccionario para almacenar los costos
    costos = {inicio: 0}

    # inicializamos la bandera en False
    invertir_movimientos = False

    # iteramos mientras la cola no esté vacía
    while cola:
        # sacamos el primer elemento de la cola
        (x, y), camino = cola.popleft()

        # si llegamos a la meta, devolvemos el camino
        if (x, y) == meta:
            return camino

        # exploramos los vecinos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # invertimos el orden de los movimientos si la bandera está en True
            if invertir_movimientos:
                dx, dy = -dx, -dy

            nx, ny = x + dx, y + dy
            # verificamos que la posición sea válida y no haya sido visitada
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] != 0 and (nx, ny) not in visitados:
                # calculamos el costo de llegar a la posición vecina
                costo_vecino = costos[(x, y)] + matriz[nx][ny]
                # actualizamos el costo mínimo si es necesario
                if (nx, ny) not in costos or costo_vecino < costos[(nx, ny)]:
                    costos[(nx, ny)] = costo_vecino
                # añadimos la posición vecina a la cola y al conjunto de visitados
                cola.append(((nx, ny), camino + [(nx, ny)]))
                visitados.add((nx, ny))

        # invertimos la bandera en cada iteración del ciclo
        invertir_movimientos = not invertir_movimientos

    # si no encontramos un camino, devolvemos None
    return None
