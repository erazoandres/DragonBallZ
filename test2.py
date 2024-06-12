import pgzrun
from pgzero.clock import clock

# Definir el tamaño de la ventana
WIDTH = 800
HEIGHT = 600

# Cargar las imágenes
image1 = Actor('c')  # Reemplaza 'nombre_de_tu_imagen1' con el nombre del archivo de tu primera imagen
image1.pos = (WIDTH // 2, HEIGHT // 2)

image2 = Actor('v')  # Reemplaza 'nombre_de_tu_imagen2' con el nombre del archivo de tu segunda imagen
image2.pos = (WIDTH // 2, HEIGHT // 2)

# Variables para controlar la visibilidad de las imágenes
image1_visible = True
image2_visible = False

# Función para ocultar la primera imagen y mostrar la segunda
def switch_images():
    global image1_visible, image2_visible
    image1_visible = False
    image2_visible = True

# Programar la función para cambiar las imágenes después de 5 segundos
clock.schedule(switch_images, 5.0)

def draw():
    screen.clear()
    if image1_visible:
        image1.draw()
    if image2_visible:
        image2.draw()

pgzrun.go()
