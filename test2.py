import pgzrun

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600

# Variables de transición
fade_alpha = 255  # Opacidad inicial
fade_direction = -1  # -1 para desvanecer, 1 para aparecer
fade_speed = 0.5  # Velocidad del efecto de desvanecido

# Superficie de desvanecimiento
fade_surface = Actor("negra")
fade_surface.pos = (WIDTH // 2, HEIGHT // 2)

def draw():
    screen.clear()
    # Aquí puedes dibujar el fondo o cualquier otro elemento que quieras que aparezca durante la transición.
    
    # Dibujar la superficie de desvanecido con la opacidad ajustada
    if fade_alpha > 0:
        screen.surface.set_alpha(fade_alpha)
        fade_surface.draw()
        screen.surface.set_alpha(255)  # Resetear la opacidad después de dibujar

def update():
    global fade_alpha

    if fade_alpha > 0:
        fade_alpha += fade_direction * fade_speed
        if fade_alpha < 0:
            fade_alpha = 0

# Iniciar el juego
pgzrun.go()
