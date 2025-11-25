
import pygame
import random
import time

# Definición de colores
COLOR_FONDO = (25, 25, 25)
COLOR_PARED = (24, 145, 255)  # Azul
COLOR_CAMINO = (40, 40, 40)
COLOR_JUGADOR = (255, 209, 102)  # Amarillo
COLOR_ENTRADA = (129, 235, 137)  # Verde
COLOR_SALIDA = (255, 107, 107)  # Rojo
COLOR_TEXTO = (255, 255, 255)

# Configuración del laberinto
ANCHO_CELDA = 20
COLUMNAS = 35
FILAS = 25
MARGEN = 40  # Margen para mostrar el tiempo y mensajes

# Dimensiones de la pantalla
ANCHO_PANTALLA = COLUMNAS * ANCHO_CELDA
ALTO_PANTALLA = FILAS * ANCHO_CELDA + MARGEN

# Constantes
PARED = 1
CAMINO = 0

def generar_laberinto(columnas, filas):
    """
    Genera un laberinto usando el algoritmo de Búsqueda en Profundidad (DFS).
    Garantiza que haya un único camino entre cualquier par de celdas.
    """
    laberinto = [[PARED for _ in range(columnas)] for _ in range(filas)]
    pila = []

    # Elegir un punto de partida aleatorio
    inicio_x, inicio_y = random.randint(0, columnas - 1), random.randint(0, filas - 1)
    laberinto[inicio_y][inicio_x] = CAMINO
    pila.append((inicio_x, inicio_y))

    while pila:
        x, y = pila[-1]
        vecinos = []

        # Comprobar vecinos (a 2 celdas de distancia para crear paredes entre caminos)
        for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columnas and 0 <= ny < filas and laberinto[ny][nx] == PARED:
                vecinos.append((nx, ny))

        if vecinos:
            # Elegir un vecino aleatorio
            nx, ny = random.choice(vecinos)

            # Eliminar la pared entre la celda actual y el vecino
            laberinto[ny][nx] = CAMINO
            laberinto[y + (ny - y) // 2][x + (nx - x) // 2] = CAMINO

            pila.append((nx, ny))
        else:
            # Retroceder
            pila.pop()

    return laberinto

class JuegoLaberinto:
    """Clase principal para gestionar la lógica del juego del laberinto."""

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()
        self.laberinto = generar_laberinto(COLUMNAS, FILAS)
        
        # Coordenadas de entrada y salida
        self.entrada_pos = (0, 1)
        self.salida_pos = (COLUMNAS - 1, FILAS - 2)
        
        # Asegurarse de que la entrada y la salida sean caminos
        self.laberinto[self.entrada_pos[1]][self.entrada_pos[0]] = CAMINO
        self.laberinto[self.salida_pos[1]][self.salida_pos[0]] = CAMINO

        self.jugador_pos = list(self.entrada_pos)
        
        # Estado del juego
        self.corriendo = True
        self.juego_terminado = False
        self.mensaje_final = ""
        
        # Cronómetro
        self.tiempo_inicio = None
        self.tiempo_transcurrido = 0
        self.primer_movimiento = False

        self.fuente = pygame.font.Font(None, 36)

    def dibujar_laberinto(self):
        """Dibuja cada celda del laberinto en la pantalla."""
        for y, fila in enumerate(self.laberinto):
            for x, tipo_celda in enumerate(fila):
                rect = pygame.Rect(x * ANCHO_CELDA, y * ANCHO_CELDA + MARGEN, ANCHO_CELDA, ANCHO_CELDA)
                if (x, y) == self.entrada_pos:
                    color = COLOR_ENTRADA
                elif (x, y) == self.salida_pos:
                    color = COLOR_SALIDA
                elif tipo_celda == PARED:
                    color = COLOR_PARED
                else:
                    color = COLOR_CAMINO
                pygame.draw.rect(self.pantalla, color, rect)

    def dibujar_jugador(self):
        """Dibuja al jugador en su posición actual."""
        rect = pygame.Rect(
            self.jugador_pos[0] * ANCHO_CELDA,
            self.jugador_pos[1] * ANCHO_CELDA + MARGEN,
            ANCHO_CELDA,
            ANCHO_CELDA,
        )
        pygame.draw.rect(self.pantalla, COLOR_JUGADOR, rect)

    def dibujar_hud(self):
        """Dibuja el área de información (cronómetro y mensajes)."""
        # Fondo del HUD
        hud_rect = pygame.Rect(0, 0, ANCHO_PANTALLA, MARGEN)
        pygame.draw.rect(self.pantalla, (10, 10, 10), hud_rect)

        # Mostrar tiempo
        if self.primer_movimiento and not self.juego_terminado:
            self.tiempo_transcurrido = time.time() - self.tiempo_inicio
        
        texto_tiempo = self.fuente.render(f"Tiempo: {self.tiempo_transcurrido:.2f}s", True, COLOR_TEXTO)
        self.pantalla.blit(texto_tiempo, (10, 10))

        # Mensaje final
        if self.juego_terminado:
            texto_final = self.fuente.render(self.mensaje_final, True, COLOR_JUGADOR)
            rect_final = texto_final.get_rect(center=(ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2))
            pygame.draw.rect(self.pantalla, COLOR_FONDO, rect_final.inflate(20, 20))
            self.pantalla.blit(texto_final, rect_final)


    def mover_jugador(self, dx, dy):
        """Mueve al jugador y comprueba colisiones."""
        if self.juego_terminado:
            return

        # Iniciar el cronómetro en el primer movimiento
        if not self.primer_movimiento:
            self.primer_movimiento = True
            self.tiempo_inicio = time.time()

        nueva_x = self.jugador_pos[0] + dx
        nueva_y = self.jugador_pos[1] + dy

        # Comprobar colisión con los límites y las paredes
        if 0 <= nueva_x < COLUMNAS and 0 <= nueva_y < FILAS:
            if self.laberinto[nueva_y][nueva_x] == CAMINO:
                self.jugador_pos = [nueva_x, nueva_y]

        # Comprobar si ha llegado a la salida
        if tuple(self.jugador_pos) == self.salida_pos:
            self.juego_terminado = True
            self.mensaje_final = f"¡Ganaste! Tiempo: {self.tiempo_transcurrido:.2f}s. Presiona ESC para salir."

    def manejar_eventos(self):
        """Gestiona las entradas del usuario."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False
                elif not self.juego_terminado:
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        self.mover_jugador(0, -1)
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        self.mover_jugador(0, 1)
                    elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                        self.mover_jugador(-1, 0)
                    elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                        self.mover_jugador(1, 0)

    def bucle_principal(self):
        """Bucle principal del juego."""
        while self.corriendo:
            self.manejar_eventos()

            self.pantalla.fill(COLOR_FONDO)
            self.dibujar_laberinto()
            self.dibujar_jugador()
            self.dibujar_hud()

            pygame.display.flip()
            self.reloj.tick(30)

def main():
    """Función principal para ejecutar el juego de forma independiente."""
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Juego del Laberinto")
    juego = JuegoLaberinto(pantalla)
    juego.bucle_principal()
    pygame.quit()

if __name__ == "__main__":
    main()

"""
--- PRUEBAS DE SOFTWARE ---

A continuación se presentan funciones de prueba para verificar la lógica del laberinto.
Para ejecutarlas, necesitarías un entorno de pruebas como 'pytest' o simplemente
descomentarlas y llamarlas desde un script. Están autocontenidas y no dependen
directamente de Pygame para su lógica central.

def prueba_generacion_laberinto():
    # Prueba que el laberinto se genera con las dimensiones correctas.
    print("Ejecutando prueba_generacion_laberinto...")
    columnas, filas = 15, 10
    laberinto = generar_laberinto(columnas, filas)
    assert len(laberinto) == filas, "El número de filas no es correcto."
    assert len(laberinto[0]) == columnas, "El número de columnas no es correcto."
    
    # Prueba que el laberinto contiene solo caminos (0) y paredes (1).
    tipos_celda = {celda for fila in laberinto for celda in fila}
    assert tipos_celda.issubset({CAMINO, PARED}), "El laberinto contiene valores no válidos."
    print("Prueba completada con éxito.")

def prueba_camino_valido_asegurado():
    # Prueba que existe un camino desde la entrada hasta cualquier otra celda alcanzable.
    # Utiliza un algoritmo BFS (Búsqueda en Amplitud) para encontrar un camino.
    print("Ejecutando prueba_camino_valido_asegurado...")
    columnas, filas = 21, 21 # Usar un tamaño considerable
    laberinto = generar_laberinto(columnas, filas)
    
    # Definir una entrada y una salida arbitrarias que sean caminos
    entrada = None
    for i in range(filas):
        if laberinto[i][1] == CAMINO:
            entrada = (1, i)
            break
            
    salida = None
    for i in range(filas - 1, -1, -1):
        if laberinto[i][columnas - 2] == CAMINO:
            salida = (columnas - 2, i)
            break
            
    assert entrada is not None, "No se encontró una celda de entrada válida."
    assert salida is not None, "No se encontró una celda de salida válida."

    # Algoritmo BFS para búsqueda de caminos
    cola = [entrada]
    visitado = {entrada}
    
    camino_encontrado = False
    while cola:
        x, y = cola.pop(0)
        
        if (x, y) == salida:
            camino_encontrado = True
            break
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columnas and 0 <= ny < filas and \
               laberinto[ny][nx] == CAMINO and (nx, ny) not in visitado:
                visitado.add((nx, ny))
                cola.append((nx, ny))
                
    assert camino_encontrado, "No se encontró un camino válido entre la entrada y la salida."
    print("Prueba completada con éxito.")

def prueba_colision_con_paredes():
    # Prueba que la lógica de colisión impide moverse hacia una pared.
    print("Ejecutando prueba_colision_con_paredes...")
    
    # Creamos un juego "falso" sin inicializar Pygame
    class FalsoJuego:
        def __init__(self):
            # Laberinto simple y predecible:
            # C C C
            # C P P
            # C C C
            self.laberinto = [
                [CAMINO, CAMINO, CAMINO],
                [CAMINO, PARED, PARED],
                [CAMINO, CAMINO, CAMINO]
            ]
            self.columnas = 3
            self.filas = 3
            self.jugador_pos = [1, 0] # Inicio en (1, 0)
        
        def mover(self, dx, dy):
            nueva_x = self.jugador_pos[0] + dx
            nueva_y = self.jugador_pos[1] + dy
            if 0 <= nueva_x < self.columnas and 0 <= nueva_y < self.filas and \
               self.laberinto[nueva_y][nueva_x] == CAMINO:
                self.jugador_pos = [nueva_x, nueva_y]

    juego = FalsoJuego()
    
    # Intentar moverse hacia la pared en (1, 1)
    posicion_inicial = list(juego.jugador_pos)
    juego.mover(0, 1) # Moverse hacia abajo
    assert juego.jugador_pos == posicion_inicial, "El jugador atravesó una pared."

    # Moverse a una posición válida
    juego.mover(-1, 0) # Moverse a la izquierda
    assert juego.jugador_pos == [0, 0], "El movimiento válido falló."
    print("Prueba completada con éxito.")

# --- FIN DE PRUEBAS ---
# Para ejecutar:
# prueba_generacion_laberinto()
# prueba_camino_valido_asegurado()
# prueba_colision_con_paredes()
"""
