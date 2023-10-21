import heapq

def costo_uniforme(matriz):

    start = None
    goal = None

    # Encontrar la posición del agente buscador y la meta
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == 4:
                start = (i, j)
            elif matriz[i][j] == 5:
                goal = (i, j)

    # Inicializar lista de nodos a explorar y conjunto de nodos explorados
    nodos_por_explorar = []
    heapq.heappush(nodos_por_explorar, (0, start, []))
    nodos_explorados = set()

    # Definir movimientos permitidos y costos
    # Arriba, Derecha, Abajo, Izquierda
    movimientos = [(0,1), (1,0), (0,-1), (-1,0)]
    costos = {1:1, 2:2, 3:3}

    # Iterar hasta que se haya explorado todo o se haya encontrado la meta
    while nodos_por_explorar:
        # Extraer el nodo con el menor costo y explorarlo
        costo_actual, nodo_actual, camino_actual = heapq.heappop(nodos_por_explorar)

        # Si se encuentra la meta, devolver el camino
        if nodo_actual == goal:
            return camino_actual + [nodo_actual]

        # Si no, marcar el nodo como explorado y generar sus sucesores
        nodos_explorados.add(nodo_actual)
        for movimiento in movimientos:
            fila, columna = nodo_actual
            fila_nueva, columna_nueva = fila + movimiento[0], columna + movimiento[1]
            sucesor = (fila_nueva, columna_nueva)
            # Ignorar sucesores fuera de la matriz o en casillas negras
            if fila_nueva < 0 or fila_nueva >= len(matriz) or columna_nueva < 0 or columna_nueva >= len(matriz[0]) or matriz[fila_nueva][columna_nueva] == 0:
                continue
            # Calcular costo del sucesor
            costo_sucesor = costo_actual + costos.get(matriz[fila_nueva][columna_nueva], 1)
            # Si el sucesor ya fue explorado, ignorarlo
            if sucesor in nodos_explorados:
                continue
            # Si el sucesor ya está en la lista de nodos por explorar y tiene un costo menor, actualizar su costo
            for i, (costo, nodo, camino) in enumerate(nodos_por_explorar):
                if nodo == sucesor and costo > costo_sucesor:
                    nodos_por_explorar[i] = (costo_sucesor, nodo, camino_actual + [nodo_actual])
                    heapq.heapify(nodos_por_explorar)
                    break
            else:
                # Si el sucesor no está en ninguna lista, agregarlo a la lista de nodos por explorar
                heapq.heappush(nodos_por_explorar, (costo_sucesor, sucesor, camino_actual + [nodo_actual]))

    # Si no se encontró la meta, devolver None
    return None