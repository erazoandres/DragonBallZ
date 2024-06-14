import pgzrun
from pgzero.clock import clock

# Definir el tamaño de la ventana
WIDTH = 800
HEIGHT = 600

# Cargar la imagen
image = Actor('fight.png')  # Reemplaza 'nombre_de_tu_imagen' con el nombre del archivo de tu imagen
fondo2 = Actor('f.jpeg')
image.pos = (WIDTH // 2, HEIGHT // 2)

# Variable para controlar la visibilidad de la imagen
image_visible = True

# Función para ocultar la imagen
def hide_image():
    global image_visible
    image_visible = False

# Programar la función para ocultar la imagen después de 5 segundos
clock.schedule(hide_image, 5.0)

def draw():
    screen.clear()
    fondo2.draw()
    if image_visible:
        image.draw()

pgzrun.go()
