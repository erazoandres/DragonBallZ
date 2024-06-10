import pgzrun
import math

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600

# Actor
actor = Actor("nube.png", (100, 300))  # Coloca la imagen del actor en la posición inicial

# Variables para controlar la trayectoria curva
t = 0  # Variable de tiempo para el movimiento

# Configuración de la curva
amplitud = 20  # Amplitud de la curva (altura de la onda)
frecuencia = 0.05  # Frecuencia de la curva (anchura de la onda)
velocidad = 2  # Velocidad de movimiento a lo largo del eje x

def update_actor():
    global t
    t += velocidad  # Incrementa la variable de tiempo para mover al actor a lo largo del eje x

    # Calcula la nueva posición del actor utilizando una combinación de movimiento lineal y curva
    actor.x = t
    actor.y = 300 + amplitud * math.sin(frecuencia * t)

    # Si el actor sale de la pantalla, lo reiniciamos
    if actor.x > WIDTH:
        actor.x = 0
        t = 0

# Usar clock.schedule_interval para actualizar la posición del actor cada 0.05 segundos
clock.schedule_interval(update_actor, 0.05)

def draw():
    screen.clear()
    actor.draw()

pgzrun.go()
