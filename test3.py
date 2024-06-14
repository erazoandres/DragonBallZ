import pgzrun
from pgzero.clock import clock
import random
import math
import os

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 30

# Centrar la ventana al inicio.
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Variables que servirán para representar y controlar la posición de cada jugador
sprite_x = 200
sprite_y = 470

sprite2_x = 600
sprite2_y = 450

center_x = WIDTH // 2
center_y = 100

center_menu_broly_goku_x = WIDTH // 2
center_menu_broly_goku_y = 500

x_goku_menu = 200
y_goku_menu = 470

x_broly_menu = 600
y_broly_menu = 483

# Configuración de la curva
t = 0  # Variable de tiempo para el movimiento
t2 = 0
amplitud = 6  # Amplitud de la curva (altura de la onda)
frecuencia = 0.05  # Frecuencia de la curva (anchura de la onda)
velocidad = 2  # Velocidad de movimiento a lo largo del eje x

# Variables de energía
player_energy = 100
broly_energy = 100
energy_max = 100

# Carga de Actores
broly_menu = Actor("broly_menu.png", (x_broly_menu, y_broly_menu))
goku_menu = Actor("goku_menu.png", (x_goku_menu, y_goku_menu))
fight = Actor("fight.png", (center_x, center_y + 140))
logo = Actor("logo.png", (center_x, center_y))  # type: ignore
nube = Actor("nube.png", pos=(-1500, 0))  # type: ignore
nave = Actor("nave.png", pos=(1400, 0))
tele1 = Actor("tele0.png")
menu_wall = Actor("menu.jpeg")
kamehouse = Actor("kamehouse.png")
fondo = Actor("c.jpeg")
fondo2 = Actor("f.jpeg")
fondo3 = Actor("v.jpeg")
fondo4 = Actor("a.jpeg")
perdiste = Actor("derrota.jpeg")
ganaste = Actor("win.jpeg")
tele2 = Actor("tele1.png")
tele3 = Actor("tele2.png")
vs = Actor("vs.png", (center_x, center_y - 35))
avatar_goku = Actor("avatar_goku.png", (48, 40))
avatar_broly = Actor("avatar_broly.png", (760, 40))
broly1 = Actor("broly0.png")
broly2 = Actor("broly1.png")
broly3 = Actor("broly2.png")
broly4 = Actor("broly3.png")
broly5 = Actor("broly4.png")
broly6 = Actor("broly5.png")

broly1_right = Actor("broly0_right.png")
broly2_right = Actor("broly1_right.png")
broly3_right = Actor("broly2_right.png")
broly4_right = Actor("broly3_right.png")
broly5_right = Actor("broly4_right.png")
broly6_right = Actor("broly5_right.png")

broly0_desconvertido = Actor("broly0_desconvertido")
broly1_desconvertido = Actor("broly1_desconvertido")
broly2_desconvertido = Actor("broly2_desconvertido")
broly3_desconvertido = Actor("broly3_desconvertido")

pelea1 = Actor("pelea0.png")
pelea2 = Actor("pelea1.png")
pelea3 = Actor("pelea2.png")
pelea4 = Actor("pelea3.png")
pelea5 = Actor("pelea4.png")
pelea6 = Actor("pelea5.png")

pelea1_left = Actor("pelea0_left.png")
pelea2_left = Actor("pelea1_left.png")
pelea3_left = Actor("pelea2_left.png")
pelea4_left = Actor("pelea3_left.png")
pelea5_left = Actor("pelea4_left.png")
pelea6_left = Actor("pelea5_left.png")

sprite_saltando = Actor("saltando.png")
sprite_left = Actor("gokuleft.png")
sprite_right = Actor("gokuright.png")

goku_derrotado = Actor("goku_derrotado", pos=(sprite_x, sprite_y))

kameha1 = Actor("goku1.png")
kameha2 = Actor("goku2.png")
kameha3 = Actor("goku3.png")
kameha4 = Actor("goku4.png")
kameha5 = Actor("goku5.png")
kameha6 = Actor("goku6.png")
kameha7 = Actor("goku7.png")
kameha8 = Actor("goku8.png")
kameha9 = Actor("goku9.png")
kameha10 = Actor("goku_derrotado.png")

kameha1_izq = Actor("goku1_left.png")
kameha2_izq = Actor("goku2_left.png")
kameha3_izq = Actor("goku3_left.png")
kameha4_izq = Actor("goku4_left.png")
kameha5_izq = Actor("goku5_left.png")
kameha6_izq = Actor("goku6_left.png")
kameha7_izq = Actor("goku7_left.png")
kameha8_izq = Actor("goku8_left.png")
kameha9_izq = Actor("goku9_left.png")

carga1 = Actor("carga1.png")
carga2 = Actor("carga2.png")
carga3 = Actor("carga3.png")

explosion0 = Actor("explosion0.png", (center_x + 2, center_y - 35))
explosion1 = Actor("explosion1.png", (center_x + 2, center_y - 35))
explosion2 = Actor("explosion2.png", (center_x + 2, center_y - 35))
explosion3 = Actor("explosion3.png", (center_x + 2, center_y - 35))
explosion4 = Actor("explosion4.png", (center_x + 2, center_y - 35))
explosion5 = Actor("explosion5.png", (center_x + 2, center_y - 35))

# Listas de cada animación con todos los actores en ellas.
teles = [tele1, tele2, tele3]
cargas = [carga1, carga2, carga3]
brolys = [broly1, broly2, broly3, broly4, broly5, broly6]
peleas = [pelea1, pelea2, pelea3, pelea4, pelea5, pelea6]
explosion = [explosion0, explosion1, explosion2, explosion3, explosion4, explosion5]
peleas_left = [pelea1_left, pelea2_left, pelea3_left, pelea4_left, pelea5_left, pelea6_left]
kameha = [sprite_right, kameha1, kameha2, kameha3, kameha4, kameha5, kameha6, kameha7, kameha8, kameha9]
brolys_right = [broly1_right, broly2_right, broly3_right, broly4_right, broly5_right, broly6_right]
broly_desconvertido = [broly0_desconvertido, broly1_desconvertido, broly2_desconvertido, broly3_desconvertido]
kameha_izq = [sprite_left, kameha1_izq, kameha2_izq, kameha3_izq, kameha4_izq, kameha5_izq, kameha6_izq, kameha7_izq, kameha8_izq, kameha9_izq]
fondos = [fondo, fondo2, fondo3, fondo4]

# Inicializando lista vacía de semillas, rellenada con 3.
semillas = []

x = random.randint(0, WIDTH)
y = random.randint(0, 1800)
semilla = Actor("./semillas/semilla.png", (x, -y))
semillas.append(semilla)

fight.pos = (WIDTH // 2, HEIGHT // 2)

# Variables de la animación
current_sprite = 0  # ataque
current_sprite2 = 0  # carga
current_sprite3 = 0  # pelea
current_sprite4 = 0  # teletransportación
current_sprite5 = 0  # broly
current_sprite6 = 0  # broly desconvertido
current_sprite7 = 0  # explosion del vs

animation_speed = 8  # Velocidad de la animación, ajustar según necesidad
animation_speedBroly = 16  # Velocidad de la animación, ajustar según necesidad

# Estos frames representan el cuadro de la cada animación, corresponden con los 'current_spritex' (Están unas líneas mas arriba)
frame_index = 0
frame_index2 = 0
frame_index3 = 0
frame_index4 = 0
frame_index5 = 0
frame_index6 = 0
frame_index7 = 0

# Indicador para rastrear la dirección en la que se mueve el personaje
direction = "right"

# Indica la pantalla en la que se encuentra
menu = True
pre_combate = False
pelea = False
final = False

# Función que se llama cuando se presiona una tecla
def on_key_down(key):
    global direction, pre_combate, menu, peleas, pelea

    if key == keys.RIGHT:
        direction = "right"
    elif key == keys.LEFT:
        direction = "left"
    if menu == True:
        if key == keys.RETURN:
            menu = False
            pre_combate = True
            fight_music()
            clock.schedule_unique(start_pelea, 5.0)  # Programa que pre_combate termine en 5 segundos
    if pelea == True:
        if key == keys.D:
            direction = "right"
            peleas.append(pelea1)
        elif key == keys.A:
            direction = "left"
            peleas.append(pelea1_left)

# Función que se llama después de 5 segundos para empezar la pelea
def start_pelea():
    global pre_combate, pelea
    pre_combate = False
    pelea = True
    pelea_music()

# Función para actualizar la lógica del juego
def update():
    global sprite_x, sprite_y, direction, current_sprite, frame_index, frame_index2, frame_index3, frame_index4, frame_index5, frame_index6, frame_index7
    global broly_energy, player_energy, animation_speed, t, frame_index, pre_combate, pelea, menu, final

    # Movimiento del personaje con las teclas
    if keyboard.right:
        sprite_x += 2
    elif keyboard.left:
        sprite_x -= 2
    if pre_combate == True:
        fight.y -= 5
    if fight.y < 0:
        fight.y = 700

    # Mueve a la nube y la nave a la derecha en el menú
    if menu == True:
        nube.x += 1
        nave.x -= 1

    # Activa el movimiento en curva para sprite
    if pelea == True:
        if direction == "right":
            sprite_x += velocidad
            # Ajuste de la coordenada y basado en una función seno para crear la curva
            sprite_y = amplitud * math.sin(frecuencia * sprite_x) + 470
        elif direction == "left":
            sprite_x -= velocidad
            sprite_y = amplitud * math.sin(frecuencia * sprite_x) + 470

        if sprite_x > WIDTH:
            sprite_x = 0
        elif sprite_x < 0:
            sprite_x = WIDTH

        if broly_energy <= 0:
            pelea = False
            final = True

    # Mueve cada semilla hacia abajo
    for semilla in semillas:
        semilla.y += 2  # Ajusta esta velocidad según sea necesario
        if semilla.colliderect(sprite_right):  # Si la semilla colisiona con el sprite
            semillas.remove(semilla)  # Elimina la semilla de la lista
            player_energy += 5  # Aumenta la energía del jugador
            if player_energy > energy_max:
                player_energy = energy_max  # No puede exceder la energía máxima

    if player_energy <= 0:
        peleas.remove(pelea1)
        peleas.append(goku_derrotado)
        pelea = False
        final = True

# Función para dibujar en pantalla
def draw():
    global broly_energy, current_sprite, frame_index, frame_index2, frame_index3, frame_index4, frame_index5, frame_index6, frame_index7, final
    global pelea
    screen.clear()
    screen.blit("f.jpeg", (0, 0))

    # Dibuja las semillas en pantalla
    for semilla in semillas:
        semilla.draw()

    if menu == True:
        menu_wall.draw()
        logo.draw()
        goku_menu.draw()
        broly_menu.draw()
        nube.draw()
        nave.draw()
        fight.draw()

    if pre_combate == True:
        vs.draw()

    if pelea == True:
        fondo.draw()
        sprite_right.draw()
        for pelea in peleas:
            pelea.draw()
        for broly in brolys_right:
            broly.draw()
        avatar_goku.draw()
        avatar_broly.draw()

        # Barra de energía de Goku
        screen.draw.filled_rect(Rect(10, 10, player_energy * 2, 20), "blue")
        screen.draw.text(f"Goku: {player_energy}", (10, 40), fontsize=24, color="white")

        # Barra de energía de Broly
        screen.draw.filled_rect(Rect(670, 10, broly_energy * 2, 20), "red")
        screen.draw.text(f"Broly: {broly_energy}", (670, 40), fontsize=24, color="white")

    if final == True:
        if broly_energy <= 0:
            screen.clear()
            ganaste.draw()
        elif player_energy <= 0:
            screen.clear()
            perdiste.draw()

# Función para la música en el menú
def menu_music():
    music.play('musicmenu.mp3')

# Función para la música de pelea
def pelea_music():
  
    tele_sound = sounds.sonidotransportacion
    tele_sound.play()

# Función para la música de la transición
def fight_music():
    
    fight = sounds.sonidotransportacion
    fight.play()

menu_music()

pgzrun.go()
