def dfs(matriz, limite_profundidad=10):
  
    inicio = None
    meta = None
    
    # Encontrar la posición del agente buscador y la meta
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == 4:
                inicio = (i, j)
            elif matriz[i][j] == 5:
                meta = (i, j)
  
    # definimos una pila para almacenar los nodos que se van visitando
    pila = [(inicio, [inicio], 0)]
    # definimos un conjunto para almacenar las posiciones ya visitadas
    visitados = set([inicio])
    
    # definimos un diccionario para almacenar los costos
    costos = {inicio: 0}

    # iteramos mientras la pila no esté vacía
    while pila:
        # sacamos el último elemento de la pila
        (x, y), camino, profundidad = pila.pop()

        # si llegamos a la meta, devolvemos el camino
        if (x, y) == meta:
            return camino

        # si alcanzamos la profundidad máxima, saltamos a la siguiente iteración
        if profundidad >= limite_profundidad:
            continue

        # exploramos los vecinos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            # verificamos que la posición sea válida y no haya sido visitada
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] != 0 and (nx, ny) not in visitados:
                # calculamos el costo de llegar a la posición vecina
                costo_vecino = costos[(x, y)] + matriz[nx][ny]
                # actualizamos el costo mínimo si es necesario
                if (nx, ny) not in costos or costo_vecino < costos[(nx, ny)]:
                    costos[(nx, ny)] = costo_vecino
                # añadimos la posición vecina a la pila y al conjunto de visitados
                pila.append(((nx, ny), camino + [(nx, ny)], profundidad + 1))
                visitados.add((nx, ny))

    # si no encontramos un camino, devolvemos None
    return None
