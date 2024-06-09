import os
import pgzrun
import random

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600

FPS = 30

# Carga la imagen del fondo
fondo = Actor("c.jpeg")

# Carga las imágenes de los kameha
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
sprite_right = Actor("gokuright.png")

kameha1 = Actor("goku1.png")
kameha2 = Actor("goku2.png")
kameha3 = Actor("goku3.png")
kameha4 = Actor("goku4.png")
kameha5 = Actor("goku5.png")
kameha6 = Actor("goku6.png")
kameha7 = Actor("goku7.png")
kameha8 = Actor("goku8.png")
kameha9 = Actor("goku9.png")

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

# Listas de kameha para diferentes acciones
cargas = [carga1, carga2, carga3]
kameha =     [kameha1,kameha2,kameha3,kameha4,kameha5,kameha6, kameha7,kameha9,kameha9]
kameha_izq = [kameha1_izq, kameha2_izq, kameha3_izq, kameha4_izq, kameha5_izq, kameha6_izq, kameha7_izq, kameha8_izq,  kameha9_izq]

peleas = [pelea1, pelea2, pelea3, pelea4, pelea5, pelea6]
teles = [tele1, tele2, tele3]
brolys = [broly1, broly2, broly3, broly4, broly5, broly6]

# Variables de la animación
current_sprite = 0  # ataque
current_sprite2 = 0  # carga
current_sprite3 = 0  # pelea
current_sprite4 = 0  # teletransportación
current_sprite5 = 0  # broly

animation_speed = 8  # Velocidad de la animación, ajustar según necesidad

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

# Direccion
dir = "right"

# Variables de salud
broly_health = random.randint(200,250)
player_health = random.randint(150,250)

# Actualiza las posiciones y la animación
def update(dt):
    global current_sprite, current_sprite2, current_sprite3, current_sprite4, current_sprite5
    global frame_count, frame_count2, frame_count3, frame_count4, frame_count5
    global attack, carga, sprite_x, sprite_y, saltando, peleando, teletransportacion, broly_peleando , dir
    global sprite2_x, broly_health, player_health
    
    # Actualiza la posición de los kameha de carga
    for carga in cargas:
        carga.pos = (sprite_x + 2, sprite_y - 17)
    
    # Actualiza la posición de los kameha de ataque
    for sprite in kameha:
        sprite.pos = (sprite_x, sprite_y)

    # Actualiza la posición de los kameha izquierdo de ataque
    for sprite in kameha_izq:
        sprite.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los kameha de pelea
    for pelea in peleas:
        pelea.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los kameha de teletransportación
    for tele in teles:
        tele.pos = (sprite_x, sprite_y)
        
    # Actualiza la posición de los kameha de Broly
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
        current_sprite = (current_sprite + 1) % len(kameha)
        
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
        sprite_x += 2
        dir = "right"
    elif keyboard.a:
        sprite_x -= 2
        dir = "left"
        
    # Salto del personaje principal
    if keyboard.space:
        kameha[0].y -= 30 
        saltando = 1
    else:
        saltando = 0
    
    # Ataque del personaje principal
    if keyboard.j:
        attack = 1
     
    else:
        current_sprite = 0
        attack = 0
        
    # Carga del personaje principal
    if keyboard.i:
        carga = 1
    else:
        carga = 0
        
    # Pelea del personaje principal
    if keyboard.l:
        peleando = 1
    else:
        peleando = 0
        
    # Teletransportación del personaje principal
    if keyboard.u:
        teletransportacion = 1
        teles[current_sprite4].x += 10 
    else:
        teletransportacion = 0
        
    # Broly sigue al personaje principal con un retraso
    follow_speed = 0.007  # Ajusta esta velocidad para cambiar el retraso
    if broly_peleando == 1: 
        sprite2_x += ((sprite_x - sprite2_x) * follow_speed)
    
    # Detectar colisiones entre Broly y los ataques del personaje principal
    if (attack == 1 or peleando == 1) and brolys[current_sprite5].colliderect(kameha[current_sprite]):
        broly_health -= random.random()
        
       

        if peleando == 1:
            broly_health -= random.random()
        elif attack == 1:
            broly_health -= random.random()


        print("Broly Health:", broly_health)
        if broly_health <= 0:
            broly_peleando = 0  # Broly ha sido derrotado

    if brolys[current_sprite5].colliderect(kameha[current_sprite]):
        player_health -= random.random()

# Dibuja los kameha en la pantalla
def draw():
    screen.clear()
    fondo.draw()
         
    if carga == 1:
        cargas[current_sprite2].draw()
    if attack == 1:
        if dir == "right":
            print(len(kameha))
            kameha[current_sprite].draw()
        elif dir == "left":
            print(len(kameha_izq))
            kameha_izq[current_sprite].draw()

    elif saltando == 1:
        kameha[0].draw()
    elif peleando == 1:
        peleas[current_sprite3].draw()
    elif teletransportacion == 1:
        teles[current_sprite4].draw()
    else:

        if dir == "left":
            kameha[2].draw()
        elif dir == "right":
            kameha[1].draw()
    
    if broly_health > 0:
        brolys[current_sprite5].draw()
    else:
        brolys[0].draw()  # Dibuja la imagen de Broly derrotado (puede cambiarse según la imagen de derrota)
    
    # Dibujar las barras de salud
    draw_health_bar("Player", player_health, 10, 30, (255, 0, 0))
    draw_health_bar("Broly", broly_health, WIDTH - 280, 30, (0, 255, 0))

def draw_health_bar(name, health, x, y, color):
    screen.draw.text(name, (x, y - 20), color="white")
    bar_width = 100
    bar_height = 20
    health_percentage = health / 100
    fill_width = bar_width * health_percentage
    screen.draw.filled_rect(Rect((x, y), (bar_width, bar_height)), "black")
    screen.draw.filled_rect(Rect((x, y), (fill_width, bar_height)), color)
    screen.draw.rect(Rect((x, y), (fill_width, bar_height)), "white")

pgzrun.go()
