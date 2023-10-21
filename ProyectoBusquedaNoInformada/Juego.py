'''
    @author: Sebastian Dario Giraldo Rodas - 2259391
    @author: Johan Steven Muñoz Lopez - 1958380
    @author: Jose Daniel Ospina Hincapie - 1958374
'''

import pygame
import os
import sys
from amplitud import bfs
from costo import costo_uniforme
from profundidad import dfs
import time

# Carga la matriz desde un archivo de texto separado por espacio
def load_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = tuple(map(int, line.strip().split(" ")))
            matrix.append(row)
    return matrix

# Carga las imágenes y las almacena en un diccionario
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Define el path actual
def load_images():
    images = {}
    for i in range(0, 7):
        path = f"img/{i}.png"
        image = pygame.image.load(path)
        resized_image = pygame.transform.scale(image, (100,100)) # cambia el tamaño 
        images[str(i)] = resized_image
    return images

# Define las dimensiones de la ventana principal
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Define las dimensiones de la ventana de búsqueda
SEARCH_WINDOW_WIDTH = 500
SEARCH_WINDOW_HEIGHT = 500



# Inicializa Pygame
pygame.init()

# Crea la ventana principal
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Búsqueda no informada")

screen = window.subsurface(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

# Define el fuente y tamaño del texto
font = pygame.font.SysFont("Arial", 30)

# Define el texto de las opciones del menú
option_texts = ["Búsqueda por costo", "Búsqueda por amplitud", "Búsqueda por Profundidad iterativa"]

# Renderiza el texto de las opciones del menú
option_surfaces = [font.render(text, True, pygame.Color("white")) for text in option_texts]

# Define las posiciones de las opciones del menú
option_rects = [surface.get_rect(center=(WINDOW_WIDTH // 2, (i+1)*WINDOW_HEIGHT // 4)) for i, surface in enumerate(option_surfaces)]

# Dibuja el fondo del menú
window.fill(pygame.Color("black"))

# Dibuja el texto de las opciones del menú
for surface, rect in zip(option_surfaces, option_rects):
    window.blit(surface, rect)

# Actualiza la pantalla
pygame.display.update()

#------------------------------------------------------------------------------------------------
### PRUEBAS
matrixactual = load_matrix("matriz2.txt")
images = load_images()

#------------------------------------------------------------------------------------------------

def pasaratupla(lista):
    tuplas = tuple(lista[i:i+2] for i in range(0, len(lista), 2))
    print(tuplas)
    return tuplas

while True:
    # Maneja los eventos de Pygame
    for event in pygame.event.get():
        # Si se cierra la ventana principal, termina el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Si se hace clic en una opción del menú, abre la ventana correspondiente
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(option_rects):
                if rect.collidepoint(mouse_pos):
                    if i == 0:
                        # Abre la ventana de búsqueda por costo
                        search_window = pygame.display.set_mode((SEARCH_WINDOW_WIDTH, SEARCH_WINDOW_HEIGHT))
                        pygame.display.set_caption("Búsqueda por Costo")
                        draw_matrix(matrixactual, images, screen, costo_uniforme(matrixactual))
                    elif i == 1:
                        # Abre la ventana de búsqueda por amplitud
                        search_window = pygame.display.set_mode((SEARCH_WINDOW_WIDTH, SEARCH_WINDOW_HEIGHT))
                        pygame.display.set_caption("Búsqueda por Amplitud")
                        draw_matrix(matrixactual, images, screen, bfs(matrixactual))
                    elif i == 2:
                        # Abre la ventana de búsqueda por alternancia
                        search_window = pygame.display.set_mode((SEARCH_WINDOW_WIDTH, SEARCH_WINDOW_HEIGHT))
                        pygame.display.set_caption("Búsqueda por Profundidad Iterativa")
                        draw_matrix(matrixactual, images, screen, dfs(matrixactual))
    # Actualiza la pantalla
    pygame.display.update()

    def draw_matrix(matrix, images, screen, update_positions=None, delay=0.7):
        height = len(matrix)
        width = len(matrix[0])
        cell_width = SEARCH_WINDOW_WIDTH // width
        cell_height = SEARCH_WINDOW_HEIGHT // height
        grid_size = max(cell_width, cell_height)
        # Buscar la posición del agente (4) y la meta (5)
        agent_pos = None
        goal_pos = None
        for row in range(height):
            for col in range(width):
                if matrix[row][col] == 4:
                    agent_pos = (row, col)
                elif matrix[row][col] == 5:
                    goal_pos = (row, col)
        # Verificar que se haya encontrado tanto al agente como a la meta
        if agent_pos is None:
            print("Error: no se encontró al agente en la matriz")
            return
        elif goal_pos is None:
            print("Error: no se encontró la meta en la matriz")
            return
        # Recorrer la ruta dada por update_positions
        for pos in update_positions:
            # Actualizar la posición del agente
            matrix[agent_pos[0]] = tuple(val if idx != agent_pos[1] else 6 for idx, val in enumerate(matrix[agent_pos[0]])) # Reemplazar la posición anterior con un espacio negro
            matrix[pos[0]] = tuple(val if idx != pos[1] else 4 for idx, val in enumerate(matrix[pos[0]])) # Poner el agente en la nueva posición
            agent_pos = pos  # Actualizar la posición actual del agente
            
            # Dibujar la matriz actualizada
            for row in range(height):
                for col in range(width):
                    x = col * grid_size
                    y = row * grid_size
                    image = images[str(matrix[row][col])]
                    image = pygame.transform.scale(image, (grid_size, grid_size))
                    screen.blit(image, (x, y))
                    # Dibujar la rejilla
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, grid_size, grid_size), 1)
                    # Si la posición actual se debe actualizar, dibujarla y esperar un tiempo
                    if (row, col) == pos:
                        pygame.display.update(pygame.Rect(x, y, grid_size, grid_size))
                        time.sleep(delay)
            
            # Actualizar toda la pantalla al final de cada movimiento del agente
            pygame.display.flip()








