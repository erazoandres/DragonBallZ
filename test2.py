import os
import pygame
import pgzrun

# Establecer la posición de la ventana (por ejemplo, esquina superior izquierda (100, 100))
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
pygame.init()

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600

# Carga la imagen del fondo
fondo = Actor("c.jpeg")

# Carga las imágenes de los sprites
tele1 = Actor("tele0.png")
tele2 = Actor("tele1.png")
tele3 = Actor("tele2.png")

broly1 = Actor("broly0.png")
broly2 = Actor("broly1.png")
broly3 = Actor("broly2.png")
broly4 = Actor("broly3.png")
broly5 = Actor("broly4.png")
broly6 = Actor("broly5.png")

pelea1 = Actor("pelea0.png")
pelea2 = Actor("pelea1.png")
pelea3 = Actor("pelea2.png")
pelea4 = Actor("pelea3.png")
pelea5 = Actor("pelea4.png")
pelea6 = Actor("pelea5.png")

sprite_x = 200
sprite_y = 470

sprite2_x = 600
sprite2_y = 450

sprite_saltando = Actor("saltando.png")
sprite_left = Actor("gokuleft.png")

sprite1 = Actor("goku0.png")
sprite2 = Actor("goku1.png")
sprite3 = Actor("goku2.png")
sprite4 = Actor("goku3.png")
sprite5 = Actor("goku4.png")
sprite6 = Actor("goku5.png")
sprite7 = Actor("goku6.png")
sprite8 = Actor("goku7.png")
sprite9 = Actor("goku8.png")
sprite10 = Actor("goku9.png")

carga1 = Actor("carga1.png")
carga2 = Actor("carga2.png")
carga3 = Actor("carga3.png")

# Listas de sprites para diferentes acciones
cargas = [carga1, carga2, carga3]
sprites = [sprite_saltando, sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9, sprite10]
peleas = [pelea1, pelea2, pelea3, pelea4, pelea5, pelea6]
teles = [tele1, tele2, tele3]
brolys = [broly1, broly2, broly3, broly4, broly5, broly6]

# Variables de la animación
current_sprite = 0  # ataque
current_sprite2 = 0  # carga
current_sprite3 = 0  # pelea
current_sprite4 = 0  # teletransportación
current_sprite5 = 0  # broly

animation_speed = 1  # Velocidad de la animación, ajustar según necesidad

frame_count = 0
frame_count2 = 0
frame_count3 = 0
frame_count4 = 0
frame_count5 = 0

# Variables de estado
attack = 0
carga = 0
saltando = 0
peleando = 0
teletransportacion = 0
broly_peleando = 1

# Variables de salud
broly_health = 100
player_health = 100

# Actualiza las posiciones y la animación
def update(dt):
    global current_sprite, current_sprite2, current_sprite3, current_sprite4, current_sprite5
    global frame_count, frame_count2, frame_count3, frame_count4, frame_count5
    global attack, carga, sprite_x, sprite_y, saltando, peleando, teletransportacion, broly_peleando
    global sprite2_x, broly_health, player_health
    
    # Actualiza la posición de los sprites de carga
    for carga in cargas:
        carga.pos = (sprite_x + 2, sprite_y - 17)
    
    # Actualiza la posición de los sprites de ataque
    for sprite in sprites:
        sprite.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los sprites de pelea
    for pelea in peleas:
        pelea.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los sprites de teletransportación
    for tele in teles:
        tele.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los sprites de Broly
    for broly in brolys:
        broly.pos = (sprite2_x, sprite2_y)
    
    # Incrementa el contador de cuadros
    frame_count += 1
    frame_count2 += 1
    frame_count3 += 1
    frame_count4 += 1
    frame_count5 += 1
    
    # Actualiza la animación según el contador de cuadros
    if frame_count % animation_speed == 0:
        current_sprite = (current_sprite + 1) % len(sprites)
        
    if frame_count2 % animation_speed == 0:
        current_sprite2 = (current_sprite2 + 1) % len(cargas)
    
    if frame_count3 % animation_speed == 0:
        current_sprite3 = (current_sprite3 + 1) % len(peleas)
        
    if frame_count4 % animation_speed == 0:
        current_sprite4 = (current_sprite4 + 1) % len(teles)
        
    if frame_count5 % animation_speed == 0:
        current_sprite5 = (current_sprite5 + 1) % len(brolys)
    
    # Movimiento del personaje principal
    if keyboard.d:
        sprite_x += 15
    elif keyboard.a:
        sprite_x -= 15
        
    # Salto del personaje principal
    if keyboard.space:
        sprites[0].y -= 30 
        saltando = 1
    else:
        saltando = 0
    
    # Ataque del personaje principal
    if keyboard.v:
        attack = 1
    else:
        current_sprite = 0
        attack = 0
        
    # Carga del personaje principal
    if keyboard.c:
        carga = 1
    else:
        carga = 0
        
    # Pelea del personaje principal
    if keyboard.f:
        peleando = 1
    else:
        peleando = 0
        
    # Teletransportación del personaje principal
    if keyboard.r:
        teletransportacion = 1
        teles[current_sprite4].x += 10 
    else:
        teletransportacion = 0
        
    # Broly sigue al personaje principal con un retraso
    follow_speed = 0.05  # Ajusta esta velocidad para cambiar el retraso
    if broly_peleando == 1: 
        sprite2_x += (sprite_x - sprite2_x) * follow_speed
    
    # Detectar colisiones entre Broly y los ataques del personaje principal
    if attack == 1 and brolys[current_sprite5].colliderect(sprites[current_sprite]):
        broly_health -= 1
        print("Broly Health:", broly_health)
        if broly_health <= 0:
            broly_peleando = 0  # Broly ha sido derrotado

# Dibuja los sprites en la pantalla
def draw():
    screen.clear()
    fondo.draw()
         
    if carga == 1:
        cargas[current_sprite2].draw()
    if attack == 1:
        sprites[current_sprite].draw()
    elif saltando == 1:
        sprites[0].draw()
    elif peleando == 1:
        peleas[current_sprite3].draw()
    elif teletransportacion == 1:
        teles[current_sprite4].draw()
    else:
        sprites[1].draw()
    
    if broly_health > 0:
        brolys[current_sprite5].draw()
    else:
        brolys[0].draw()  # Dibuja la imagen de Broly derrotado (puede cambiarse según la imagen de derrota)
    
    # Dibujar las barras de salud
    draw_health_bar("Player", player_health, 10, 10, (255, 0, 0))
    draw_health_bar("Broly", broly_health, WIDTH - 210, 10, (0, 255, 0))

def draw_health_bar(name, health, x, y, color):
    screen.draw.text(name, (x, y - 20), color="white")
    bar_width = 200
    bar_height = 10  # Ajusta la altura de la barra de salud a 10 píxeles
    health_percentage = health / 100
    fill_width = bar_width * health_percentage
    screen.draw.filled_rect(Rect((x, y), (bar_width, bar_height)), "black")
    screen.draw.filled_rect(Rect((x, y), (fill_width, bar_height)), color)
    screen.draw.rect(Rect((x, y), (bar_width, bar_height)), "white")

pgzrun.go()
