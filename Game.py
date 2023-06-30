

import pygame
import random
import time

# Iniciar libreria
pygame.init()

# Definir dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Asignar nombre a la ventana
pygame.display.set_caption("Juego de Memoria")

# Definir el color de la letra en la pantalla
BLUE = (0, 0, 128)

# Cargar imágenes de las cartas
card_images = [
    pygame.image.load("imagen1.png"),
    pygame.image.load("imagen2.png"),
    pygame.image.load("imagen3.png"),
    pygame.image.load("imagen4.png"),
    pygame.image.load("imagen5.png"),
    pygame.image.load("imagen6.png")
]

# Cantidad de cartas por fila y columna
num_cols = 4
num_rows = 3

# Lista donde se almacenarán las cartas
cards = []
for i in range(num_cols * num_rows // 2):
    # Agregar cartas dos veces
    cards.append(i)
    cards.append(i)

# Ordenar de manera aleatoria las cartas
random.shuffle(cards)

# Dimensiones de las cartas
card_width = 100
card_height = 100

# Almacenar las posiciones de las cartas
card_positions = []
for row in range(num_rows):
    for col in range(num_cols):
        # Calcular la posición x en la columna
        x = col * (card_width + 10) + 50
        # Calcular la posición y en la columna
        y = row * (card_height + 10) + 50
        # Agregar la posición (x, y) a la lista de posiciones de cartas
        card_positions.append((x, y))

# Estado de las cartas (0: boca abajo, 1: boca arriba)
card_state = [0] * len(cards)

# Variables auxiliares
num_matches = 0
selected_cards = []  # Crear una lista para almacenar las cartas seleccionadas

# Variables auxiliares para contar tiempo y errores
start_time = None
end_time = None
num_errors = 0

# Función para contar el tiempo transcurrido
def get_elapsed_time():
    if start_time is None:
        return 0
    elif end_time is None:
        return time.time() - start_time
    else:
        return end_time - start_time

# Mostrar las cartas y otros elementos en la pantalla
def draw_screen():
    # Asignar color a la pantalla, en este caso el color gris claro
    screen.fill((192, 192, 192))
    # Recorrer los indices y las posiciones de las cartas
    for i, pos in enumerate(card_positions):
        x, y = pos
        index = cards[i]
        # Verificar el estado de la carta y si está boca abajo(0), se muestra la parte de atrás de la carta
        if card_state[i] == 0:
            # Dibujar la parte trasera de la carta
            pygame.draw.rect(screen, (0, 0, 255), (x, y, card_width, card_height))
        else:
            # Dibujar la imagen en la carta
            screen.blit(card_images[index], (x, y))

    # Mostrar las instrucciones en la pantalla
    font = pygame.font.Font(None, 24)
    instructions = [
        "*********Instrucciones*********",
        "1. Debe seleccionar la imagen que desea buscar",
        "2. Debe seleccionar el cuadro que considera que",
        "es donde se encuentra la pareja de la imagen anterior",
        "3. El objetivo es encontrar todas las parejas",
        "*****Si está listo para iniciar, oprima la tecla 'Enter' para continuar****"
    ]
    # Dar ubicación a las instrucciones en la ventana
    for i, text in enumerate(instructions):
        text_render = font.render(text, True, BLUE)
        screen.blit(text_render, (50, 400 + i * 30))

    # Mostrar el tiempo y los errores en la pantalla
    font = pygame.font.Font(None, 24)
    elapsed_time = get_elapsed_time()
    time_text = "Tiempo: {:.2f} segundos".format(elapsed_time)
    error_text = "Errores: {}".format(num_errors)
    time_render = font.render(time_text, True, BLUE)
    error_render = font.render(error_text, True, BLUE)
    # Dar ubicación al texto en la pantalla
    screen.blit(time_render, (600, 20))
    screen.blit(error_render, (600, 50))
    # Actualizar pantalla
    pygame.display.flip()

# Voltear las cartas seleccionadas
def flip_cards():
    if len(selected_cards) == 2:
        # Compara los valores de las cartas seleccionadas
        if cards[selected_cards[0]] == cards[selected_cards[1]]:
            # Si las cartas coinciden, eliminarlas de la lista
            cards[selected_cards[0]] = 0
            cards[selected_cards[1]] = 0
            # No hubo error
            return False
        else:
            # Si las cartas no coinciden, hubo un error
            return True
    return False

# Mostrar menú de inicio
def show_menu():
    while True:
        for event in pygame.event.get():
            # Verificar si se ha hecho clic en el botón de cerrar la ventana
            if event.type == pygame.QUIT:
                # Cerrar Pygame y salir del programa
                pygame.quit()
                return

            # Verificar eventos de teclado
            elif event.type == pygame.KEYDOWN:
                # Si la tecla es enter, inicia el juego
                if event.key == pygame.K_RETURN:
                    return True
                # Si la tecla es esc, sale del programa
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Asignar color a la pantalla, en este caso el color gris claro
        screen.fill((192, 192, 192))
        # Fuente para mostrar el texto del menú
        font = pygame.font.Font(None, 36)
        # Crear los objetos de texto para el menú
        menu_text1 = font.render("Juego de Memoria", True, BLUE)
        menu_text2 = font.render("Presione Enter para iniciar", True, BLUE)
        menu_text3 = font.render("Presione Esc para salir", True, BLUE)
        # Dar ubicación al texto en la pantalla
        screen.blit(menu_text1, (width // 2 - menu_text1.get_width() // 2, height // 2 - 50))
        screen.blit(menu_text2, (width // 2 - menu_text2.get_width() // 2, height // 2))
        screen.blit(menu_text3, (width // 2 - menu_text3.get_width() // 2, height // 2 + 50))
        # Actualizar pantalla
        pygame.display.flip()

# Variables de control
running = True
num_errors = 0
game_started = False

# Mostrar menú de inicio
show_menu()

# Bucle principal del juego
while running:
    # Recorrer todos los eventos que encuentre en cada parte del bucle
    for event in pygame.event.get():
        # Si el tipo de evento es QUIT, sale del bucle y cierra la ventana
        if event.type == pygame.QUIT:
            running = False
        # Verificar si se ha oprimido una tecla
        elif event.type == pygame.KEYDOWN:
            # Si la tecla es enter
            if event.key == pygame.K_RETURN:
                # Si el juego no ha iniciado, lo inicia
                if not game_started:
                    game_started = True
                    # Registrar el tiempo de inicio del juego
                    start_time = time.time()
        # Verificar los clics con el mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Si el juego ya ha iniciado
            if game_started:
                # Validar la posición del clic del mouse
                pos = pygame.mouse.get_pos()
                # Recorrer las posiciones de las cartas
                for i, card_pos in enumerate(card_positions):
                    x, y = card_pos
                    # Verificar si la posición del clic está dentro de una carta
                    if x <= pos[0] <= x + card_width and y <= pos[1] <= y + card_height:
                        # Validar si la carta está oculta (0)
                        if card_state[i] == 0:
                            # Cambiar de estado y agregarlo a la lista de cartas seleccionadas
                            card_state[i] = 1
                            selected_cards.append(i)
                            # Validar si se han seleccionado dos cartas
                            if len(selected_cards) == 2:
                                # Verificar si las dos cartas coinciden
                                if cards[selected_cards[0]] == cards[selected_cards[1]]:
                                    # Incrementar el contador de coincidencias
                                    num_matches += 1
                                    # Limpiar lista de cartas seleccionadas
                                    selected_cards.clear()
                                else:
                                    # Esperar un segundo para voltear las cartas seleccionadas
                                    pygame.time.wait(1000)
                                    card_state[selected_cards[0]] = 0
                                    card_state[selected_cards[1]] = 0
                                    # Limpiar lista de cartas seleccionadas
                                    selected_cards.clear()
                                    # Incrementar el contador de errores
                                    num_errors += 1
                            break

    # Verificar si se han encontrado todas las parejas
    if num_matches == len(cards) // 2:
        # Registrar el tiempo y salir del bucle
        end_time = time.time()
        running = False

    # Mostrar la pantalla del juego
    draw_screen()
    pygame.time.wait(1000)

# Mostrar los resultados finales en la ventana antes de cerrarla
while True:
    for event in pygame.event.get():
        # Verifica si se ha hecho clic en el botón de cerrar la ventana
        if event.type == pygame.QUIT:
            # Cerrar Pygame y salir del programa
            pygame.quit()
            sys.exit()

    # Asignar color a la pantalla, en este caso el color gris claro
    screen.fill((192, 192, 192))
    # Fuente para mostrar el texto de los resultados
    font = pygame.font.Font(None, 36)
    # Crear los objetos de texto para los resultados
    result_text1 = font.render("¡Felicitaciones!", True, BLUE)
    result_text2 = font.render("Has encontrado todas las parejas", True, BLUE)
    result_text3 = font.render("Tiempo: {:.2f} segundos".format(end_time - start_time), True, BLUE)
    result_text4 = font.render("Errores: {}".format(num_errors), True, BLUE)
    # Dar ubicación al texto en la pantalla
    screen.blit(result_text1, (width // 2 - result_text1.get_width() // 2, height // 2 - 100))
    screen.blit(result_text2, (width // 2 - result_text2.get_width() // 2, height // 2 - 50))
    screen.blit(result_text3, (width // 2 - result_text3.get_width() // 2, height // 2))
    screen.blit(result_text4, (width // 2 - result_text4.get_width() // 2, height // 2 + 50))
    # Actualizar pantalla
    pygame.display.flip()
