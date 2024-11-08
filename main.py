import pgzrun
import pgzero.clock
import random
import math
import os 

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 120

#Centrar la ventana al inicio.
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Variables que serviran para representar y controlar la posicion de cada jugados

#Goku
sprite_x = 200
sprite_y = 470

#Broly
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

#Dialogos Posiciones
pos_txt1 = -280
pos_txt2 = 820

# Carga de Actoresf
broly_menu = Actor("./elementos/elementos/broly_menu.png",(x_broly_menu,y_broly_menu)) # type: ignore
goku_menu =  Actor("./elementos/elementos/goku_menu.png",(x_goku_menu,y_goku_menu))
fight = Actor("./elementos/elementos/fight.png",(center_x  , center_y + 140))
avatar_broly = Actor("./elementos/elementos/avatar_broly.png",(760,40))
logo =  Actor("./elementos/elementos/logo.png",(center_x  , center_y))
vs = Actor("./elementos/elementos/vs.png",(center_x  , center_y - 35))
vsGrande = Actor("./elementos/elementos/vsgrande.png",(center_x  , 500))
avatar_goku =  Actor("./elementos/elementos/avatar_goku.png",(48,40))
nube =  Actor("./elementos/elementos/nube.png", pos = (-1500,0)) 
nave =  Actor("./elementos/elementos/nave.png",pos = (1400,0))
perdiste = Actor("./elementos/estados/reinicio10.jpeg")
#perdiste = Actor("./elementos/estados/derrota.jpeg")
menu_wall = Actor("./elementos/fondos/menu.jpeg")
ganaste =  Actor("./elementos/estados/win.jpeg")

volando_izquierda = Actor("./sprites/goku/otros/volando_izquierda.png")
volando_derecha = Actor("./sprites/goku/otros/volando_derecha.png")

caminando_izquierda = Actor("./sprites/goku/otros/caminando_izquierda.png")
caminando_derecha = Actor("./sprites/goku/otros/caminando_derecha.png")

broly1 = Actor("./sprites/broly/izquierda/broly0.png")
broly2 = Actor("./sprites/broly/izquierda/broly1.png")
broly3 = Actor("./sprites/broly/izquierda/broly2.png")
broly4 = Actor("./sprites/broly/izquierda/broly3.png")
broly5 = Actor("./sprites/broly/izquierda/broly4.png")
broly6 = Actor("./sprites/broly/izquierda/broly5.png")

tele1 = Actor("./sprites/goku/teletransportacion/tele0.png")
tele2 = Actor("./sprites/goku/teletransportacion/tele1.png")
tele3 = Actor("./sprites/goku/teletransportacion/tele2.png")

fondo =  Actor("./elementos/fondos/fondo1.jpeg")
fondo2 = Actor("./elementos/fondos/fondo2.jpeg")
fondo3 = Actor("./elementos/fondos/fondo3.jpeg")
fondo4=  Actor("./elementos/fondos/fondo4.jpeg")

broly1_right = Actor("./sprites/broly/derecha/broly0_right.png")
broly2_right = Actor("./sprites/broly/derecha/broly1_right.png")
broly3_right = Actor("./sprites/broly/derecha/broly2_right.png")
broly4_right = Actor("./sprites/broly/derecha/broly3_right.png")
broly5_right = Actor("./sprites/broly/derecha/broly4_right.png")
broly6_right = Actor("./sprites/broly/derecha/broly5_right.png")

broly0_desconvertido = Actor("./sprites/broly/desconvertido/broly_desconvertido1")
broly1_desconvertido = Actor("./sprites/broly/desconvertido/broly_desconvertido2")
broly2_desconvertido = Actor("./sprites/broly/desconvertido/broly_desconvertido3")
broly3_desconvertido = Actor("./sprites/broly/desconvertido/broly_desconvertido4")

pelea1 = Actor("./sprites/goku/atacando/derecha/pelea0.png")
pelea2 = Actor("./sprites/goku/atacando/derecha/pelea1.png")
pelea3 = Actor("./sprites/goku/atacando/derecha/pelea2.png")
pelea4 = Actor("./sprites/goku/atacando/derecha/pelea3.png")
pelea5 = Actor("./sprites/goku/atacando/derecha/pelea4.png")
pelea6 = Actor("./sprites/goku/atacando/derecha/pelea5.png")

pelea1_left = Actor("./sprites/goku/atacando/izquierda/pelea0_left.png")
pelea2_left = Actor("./sprites/goku/atacando/izquierda/pelea1_left.png")
pelea3_left = Actor("./sprites/goku/atacando/izquierda/pelea2_left.png")
pelea4_left = Actor("./sprites/goku/atacando/izquierda/pelea3_left.png")
pelea5_left = Actor("./sprites/goku/atacando/izquierda/pelea4_left.png")
pelea6_left = Actor("./sprites/goku/atacando/izquierda/pelea5_left.png")

sprite_left = Actor("./sprites/goku/otros/gokuleft.png")
sprite_right = Actor("./sprites/goku/otros/gokuright.png")
goku_derrotado = Actor("./sprites/goku/otros/goku_derrotado",pos = (sprite_x , sprite_y))

kameha1 = Actor("./sprites/goku/kamehameha/derecha/goku1.png")
kameha2 = Actor("./sprites/goku/kamehameha/derecha/goku2.png")
kameha3 = Actor("./sprites/goku/kamehameha/derecha/goku3.png")
kameha4 = Actor("./sprites/goku/kamehameha/derecha/goku4.png")
kameha5 = Actor("./sprites/goku/kamehameha/derecha/goku5.png")
kameha6 = Actor("./sprites/goku/kamehameha/derecha/goku6.png")
kameha7 = Actor("./sprites/goku/kamehameha/derecha/goku7.png")
kameha8 = Actor("./sprites/goku/kamehameha/derecha/goku8.png")
kameha9 = Actor("./sprites/goku/kamehameha/derecha/goku9.png")

kameha_recargado1_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_1.png")
kameha_recargado2_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_2.png")
kameha_recargado3_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_3.png")
kameha_recargado4_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_4.png")
kameha_recargado5_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_5.png")
kameha_recargado6_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_6.png")
kameha_recargado7_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_7.png")
kameha_recargado8_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_8.png")
kameha_recargado9_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_9.png")
kameha_recargado10_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_10.png")
kameha_recargado11_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_11.png")
kameha_recargado12_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_12.png")
kameha_recargado13_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_13.png")
kameha_recargado14_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_11.png")
kameha_recargado15_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_12.png")
kameha_recargado16_derecha = Actor("./sprites/goku/kamehameha2/derecha/kamehameha2_13.png")
 
genkidama_goku1 = Actor("./sprites/goku/genkidama/01.png",(sprite_x,sprite_y-20))
genkidama_goku2 = Actor("./sprites/goku/genkidama/02.png",(sprite_x,sprite_y-20))
genkidama_goku3 = Actor("./sprites/goku/genkidama/03.png",(sprite_x,sprite_y-20))
genkidama_goku4 = Actor("./sprites/goku/genkidama/04.png",(sprite_x,sprite_y-20))
genkidama_goku5 = Actor("./sprites/goku/genkidama/05.png",(sprite_x,sprite_y-20))
genkidama_goku6 = Actor("./sprites/goku/genkidama/06.png",(sprite_x,sprite_y-20))
genkidama_goku7 = Actor("./sprites/goku/genkidama/07.png",(sprite_x,sprite_y-20))
genkidama_goku8 = Actor("./sprites/goku/genkidama/08.png",(sprite_x,sprite_y-20))
genkidama_goku9 = Actor("./sprites/goku/genkidama/09.png",(sprite_x,sprite_y-20))
genkidama_goku10 = Actor("./sprites/goku/genkidama/010.png",(sprite_x,sprite_y-20))
genkidama_goku11 = Actor("./sprites/goku/genkidama/011.png",(sprite_x,sprite_y-20))
genkidama_goku12 = Actor("./sprites/goku/genkidama/012.png",(sprite_x,sprite_y-20))
genkidama_goku13 = Actor("./sprites/goku/genkidama/013.png",(sprite_x,sprite_y-20))

genkidama1 = Actor("./sprites/goku/genkidama/genkidama1_1.png", (sprite_x,sprite_y - 90))
genkidama2 = Actor("./sprites/goku/genkidama/genkidama1_2.png", (sprite_x,sprite_y - 90))
genkidama3 = Actor("./sprites/goku/genkidama/genkidama1_3.png", (sprite_x,sprite_y - 90))

kameha_recargado1 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_1.png")
kameha_recargado2 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_2.png")
kameha_recargado3 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_3.png")
kameha_recargado4 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_4.png")
kameha_recargado5 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_5.png")
kameha_recargado6 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_6.png")
kameha_recargado7 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_7.png")
kameha_recargado8 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_8.png")
kameha_recargado9 =  Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_9.png")
kameha_recargado10 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_10.png")
kameha_recargado11 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_11.png")
kameha_recargado12 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_12.png")
kameha_recargado13 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_13.png")
kameha_recargado14 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_14.png")
kameha_recargado15 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_15.png")
kameha_recargado16 = Actor("./sprites/goku/kamehameha2/izquierda/kamehameha2_16.png")

kameha1_izq = Actor("./sprites/goku/kamehameha/izquierda/goku1_left.png")
kameha2_izq = Actor("./sprites/goku/kamehameha/izquierda/goku2_left.png")
kameha3_izq = Actor("./sprites/goku/kamehameha/izquierda/goku3_left.png")
kameha4_izq = Actor("./sprites/goku/kamehameha/izquierda/goku4_left.png")
kameha5_izq = Actor("./sprites/goku/kamehameha/izquierda/goku5_left.png")
kameha6_izq = Actor("./sprites/goku/kamehameha/izquierda/goku6_left.png")
kameha7_izq = Actor("./sprites/goku/kamehameha/izquierda/goku7_left.png")
kameha8_izq = Actor("./sprites/goku/kamehameha/izquierda/goku8_left.png")
kameha9_izq = Actor("./sprites/goku/kamehameha/izquierda/goku9_left.png")

carga1 = Actor("./sprites/cargando/carga1.png")
carga2 = Actor("./sprites/cargando/carga2.png")
carga3 = Actor("./sprites/cargando/carga3.png")

explosion0 = Actor("./sprites/explosion/explosion0.png",(center_x +2 , center_y - 35))
explosion1 = Actor("./sprites/explosion/explosion1.png",(center_x +2 , center_y - 35))
explosion2 = Actor("./sprites/explosion/explosion2.png",(center_x +2 , center_y - 35))
explosion3 = Actor("./sprites/explosion/explosion3.png",(center_x +2 , center_y - 35))
explosion4 = Actor("./sprites/explosion/explosion4.png",(center_x +2 , center_y - 35))
explosion5 = Actor("./sprites/explosion/explosion5.png",(center_x +2 , center_y - 35))

fondo_dialogo = Actor("../images/elementos/fondos/fondo2")
goku_dialogo = Actor("../images/dialogos/goku" , (-200,450))
broly_dialogo = Actor("../images/dialogos/broly", (1000,450))
dialogo = Actor("../images/elementos/elementos/recuadro_dialogo", (1000,550))
dialogo2 = Actor("../images/elementos/elementos/recuadro_dialogo2", (-200,550))


#Listas de cada animacion con  todos los actores en ellas.
teles =  [tele1, tele2, tele3]
cargando = [carga1, carga2, carga3]
goku_peleando_derecha = [pelea1, pelea2, pelea3, pelea4, pelea5, pelea6]
goku_peleando_izquierda = [pelea1_left, pelea2_left, pelea3_left, pelea4_left, pelea5_left, pelea6_left]
explosion = [explosion0,explosion1,explosion2,explosion3,explosion4,explosion5]
kameha_derecha = [sprite_right,kameha1,kameha2,kameha3,kameha4,kameha5,kameha6, kameha7,kameha9,kameha9]
kameha_izquierda = [sprite_left,kameha1_izq, kameha2_izq, kameha3_izq, kameha4_izq, kameha5_izq, kameha6_izq, kameha7_izq, kameha8_izq,  kameha9_izq]
broly_peleando_izquierda = [broly1, broly2, broly3, broly4, broly5, broly6]
broly_peleando_derecha = [broly1_right, broly2_right, broly3_right, broly4_right, broly5_right, broly6_right]
broly_desconvertido = [broly0_desconvertido,broly1_desconvertido,broly2_desconvertido,broly3_desconvertido]
fondos = [fondo,fondo2,fondo3,fondo4]
kameha_recargado_izquierda = [kameha_recargado1,kameha_recargado2,kameha_recargado3,kameha_recargado4,kameha_recargado5,kameha_recargado6,kameha_recargado7,kameha_recargado8,kameha_recargado9,kameha_recargado10,kameha_recargado11,kameha_recargado12,kameha_recargado13,kameha_recargado14,kameha_recargado15,kameha_recargado16]
kameha_recargado_derecha = [kameha_recargado1_derecha,kameha_recargado2_derecha,kameha_recargado3_derecha,kameha_recargado4_derecha,kameha_recargado5_derecha,kameha_recargado6_derecha,kameha_recargado7_derecha,kameha_recargado8_derecha,kameha_recargado9_derecha,kameha_recargado10_derecha,kameha_recargado11_derecha,kameha_recargado12_derecha,kameha_recargado13_derecha,kameha_recargado14_derecha,kameha_recargado15_derecha,kameha_recargado16_derecha]

genkidama_goku = [genkidama_goku1,genkidama_goku2,genkidama_goku3,genkidama_goku4,genkidama_goku5,genkidama_goku6,genkidama_goku7,genkidama_goku8,genkidama_goku9,genkidama_goku10,genkidama_goku11,genkidama_goku12,genkidama_goku13]
genkidama_bola = [genkidama1,genkidama2,genkidama3]

bolas_energia = []
semillas  = [] 

fight.pos = (WIDTH // 2, HEIGHT // 2)

# Variables de la animación
current_sprite  = 0  # ataque
current_sprite2 = 0  # carga
current_sprite3 = 0  # pelea
current_sprite4 = 0  # teletransportación
current_sprite5 = 0  # broly
current_sprite6 = 0  # broly desconvertido
current_sprite7 = 0 # explosion del vs
current_sprite8 = 0 # kamehameha recargado
current_sprite9 = 0 # genkidama

animation_speed = 8  # Velocidad de la animación, ajustar según necesidad
animation_speedBroly = 8  # Velocidad de la animación, ajustar según necesidad

#Estos frames representan el cuadro de la cada animacion, corresponden con los 'current_spritex' (Estan unas lineas arriba).
frame_count  = 0
frame_count2 = 0
frame_count3 = 0
frame_count4 = 0
frame_count5 = 0
frame_count6 = 0
frame_count7 = 0
frame_count8 = 0
frame_count9 = 0

# Variables de estado necesarias para controlar varios aspectos del juego
elemento_volador_random = random.randint(1,2)
sonido_fight_reproducido = False
golpeando_sound_firsTime = True
genkidama_x = sprite_x
genkidama_y = sprite_y
kame_sound_firstTime = True
firstTimeEndBattle = True
teletransportacion = False
sprite_reproducido = False
switch_efecto_menu = True
fondo_seleccionado = False
attack_recargado = False
firstTimeScream = True
ataque_lanzado = False
# broly_peleando = True
broly_peleando = False

desconvertido = False
trayectoNave = False
trayectoNube = True
moviendose = False
modo_juego = "juego"
genkidama = False
genkidama_mover = False
firstTime = True
peleando = False
saltando = False
attack = False

dialogo_goku = False
dialogo_broly = False



direccion_goku = "derecha" # Direccion de personaje principal.
indice_fondos = 0
salud_broly = 0
salud_goku = 40
tiempo = 0
carga = False
timer = 0


def iniciar_dialogo(actor1, actor2):

    global pos_txt1, pos_txt2

    if actor1.x < 100:
        actor1.x += 2
        dialogo2.x += 2


    if actor2.x > 700:
        actor2.x -= 2
        dialogo.x -= 2


    if actor1.x < 100:
        pos_txt2 -= 2

    if actor2.x > 700:
        pos_txt1 += 2


    if not (actor1.x < 100):
        pgzero.clock.schedule(pasar,10)
   
def pasar():
    global modo_juego
    modo_juego = "juego"

def generar_semillas():
    x = random.randint(0,WIDTH)
    y = random.randint(0,1800)
    semilla = Actor("./elementos/elementos/semilla.png" , (x,-y))
    semillas.append(semilla)

def sonidos():
    # Cargar y reproduccion de sonidos

    global tele_sound,golpeando_sound,kame_sound,salto_sound,sonido_carga,sonido_muere, sonido_dialogo_goku
    global sonido_curar,sonido_pide,sonido_final_goku,sonido_grito_goku,sonido_efecto,fight_sound,sonido_dialogo_broly

    #Efectos de sonido del juego en .wav
    fight_sound = sounds.audio_fight  # Asegúrate de que el archivo teletransportacion.wav está en la carpeta sounds
    fight_sound.set_volume(0.2)


    #Efectos de sonido del juego en .wav
    tele_sound = sounds.sonidotransportacion  # Asegúrate de que el archivo teletransportacion.wav está en la carpeta sounds
    tele_sound.set_volume(0.2)

    golpeando_sound = sounds.sonidogolpeando  # Asegúrate de que el archivo golpeando.wav está en la carpeta sounds
    golpeando_sound.set_volume(0)

    kame_sound = sounds.sonidokame  # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    kame_sound.set_volume(0.6)

    salto_sound = sounds.sonidosalto # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    salto_sound.set_volume(0.2)

    sonido_carga = sounds.sonidocarga2 # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    sonido_carga.set_volume(0.3)

    sonido_muere = sounds.muere # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    sonido_muere.set_volume(0.1)

    sonido_curar = sounds.sonidocurar # Asegúrate de que el archivo curar.wav está en la carpeta sounds
    sonido_curar.set_volume(0.3)

    sonido_pide = sounds.sonidopidesemilla # Asegúrate de que el archivo pide.wav está en la carpeta sounds
    sonido_pide.set_volume(1)

    sonido_final_goku = sounds.sonidofinalgoku # Asegúrate de que el archivo final.wav está en la carpeta sounds
    sonido_final_goku.set_volume(0.6)

    sonido_grito_goku = sounds.gritogoku # Asegúrate de que el archivo grito.wav está en la carpeta sounds
    sonido_grito_goku.set_volume(1.5)

    sonido_efecto = sounds.efectomenu # Asegúrate de que el archivo curar.wav está en la carpeta sounds
    sonido_efecto.set_volume(1.5)

    sonido_dialogo_goku = sounds.dialogo_goku
    sonido_dialogo_goku.set_volume(1.5)

    sonido_dialogo_broly = sounds.dialogo_broly
    sonido_dialogo_broly.set_volume(1.5)

    # music.play("musicmenu.mp3")

def terminar_juego():
    global modo_juego
    modo_juego = "derrota"

def draw_energy_bar(x, y, energy, max_energy):
    # Dibuja la barra de energía en la pantalla
    bar_width = 200
    bar_height = 20
    energy_percentage = energy / max_energy
    fill_width = bar_width * energy_percentage
    screen.draw.filled_rect(Rect((x, y), (bar_width, bar_height)), "black")
    screen.draw.filled_rect(Rect((x, y), (fill_width, bar_height)), "yellow")
    screen.draw.rect(Rect((x, y), (bar_width, bar_height)), "white")

def draw_health_bar_goku(name, health, x, y, color):
    #Dibujando los rectangulos de la vida de ambos personajes.
    screen.draw.text(name, (x, y - 20), color="white")
    bar_width = 160
    bar_height = 20
    health_percentage = health / 100
    fill_width = bar_width * health_percentage
    screen.draw.filled_rect(Rect((x, y), (bar_width, bar_height)), "black")
    screen.draw.filled_rect(Rect((x, y), (fill_width, bar_height)), color)
    screen.draw.rect(Rect((x, y), (fill_width, bar_height)), "blue")

def draw_health_bar_broly(name, health, x, y, color):
    #Dibujando los rectangulos de la vida de ambos personajes.
    screen.draw.text(name, (x, y - 20), color="white")
    bar_width2 = 230
    bar_height2 = 20
    health_percentage2 = health / 100
    fill_width2 = bar_width2 * health_percentage2
    screen.draw.filled_rect(Rect((x, y), (bar_width2, bar_height2)), "green")
    screen.draw.filled_rect(Rect((x, y), (fill_width2, bar_height2)), color)
    screen.draw.rect(Rect((x, y), (fill_width2, bar_height2)), "blue")

def animacion_logo_menu():
    global tiempo
    # Incrementa el tiempo
    tiempo += 1
    # Calcula el desplazamiento en y usando una función seno
    desplazamiento_y = amplitud * math.sin(frecuencia * tiempo)
    # Ajusta la posición del logo
    logo.y = center_y + desplazamiento_y
        
def logica_ataque_persecucion():
    global tiempo
    # Incrementa el tiempo
    tiempo += 1
    # Calcula el desplazamiento en y usando una función seno
    desplazamiento2_y = (amplitud -8) * math.sin(frecuencia * tiempo)
    # Ajusta la posición del logo
    goku_menu.y = (center_menu_broly_goku_y + desplazamiento2_y) - 10
    broly_menu.y = center_menu_broly_goku_y + desplazamiento2_y

def controles():

    global sprite_x, sprite_y, player_energy,carga,direccion_goku,attack,current_sprite,peleando,teletransportacion, kame_sound_firstTime,attack_recargado
    global current_sprite8,bolas_energia,saltando,moviendose,genkidama,modo_juego
    # Movimiento del personaje principal
    
    if keyboard.d and sprite_x<WIDTH - 16:
        sprite_x += 2
        moviendose = True
        direccion_goku = "derecha"
    elif keyboard.a and sprite_x>=16:
        sprite_x -= 2
        direccion_goku = "izquierda"
        moviendose = True
    else:
        moviendose = False         

    # Salto del personaje principal
    if (keyboard.space or keyboard.w) and (volando_izquierda.y > 200 or volando_derecha.y >200) :

        if sprite_y >450:
            salto_sound.play()
        saltando = True
        # sprite_y = 315
        sprite_y -=5 
        volando_izquierda.y -= 5
        volando_izquierda.x = sprite_x
        volando_derecha.y -= 5
        volando_derecha.x = sprite_x
        carga = True
    else:
        saltando = False
        sprite_y += 5
        volando_izquierda.y += 5
        volando_izquierda.x = sprite_x
        volando_derecha.y +=5
        volando_derecha.x = sprite_x
        carga = False
        
        if sprite_y > 460 or volando_izquierda.y > 460 or volando_derecha.y > 460 :
            sprite_y = 460
            volando_derecha.y = 460
            volando_izquierda.y = 460
        
    # Carga del personaje principal
    if keyboard.i:
        carga = True
        if player_energy < energy_max:
            player_energy += 1
    else:
        carga = False
  
    # Pelea del personaje principal
    if keyboard.l and salud_goku>0:
        peleando = 1
    else:
        peleando = 0
        
def update():
    global current_sprite, current_sprite2, current_sprite3, current_sprite4, current_sprite5,current_sprite6,current_sprite7,current_sprite8,current_sprite9
    global frame_count, frame_count2, frame_count3, frame_count4, frame_count5,frame_count6,frame_count7,frame_count8,frame_count9,firstTimeEndBattle,switch_efecto_menu
    global attack, sprite_x, sprite_y, saltando, peleando, teletransportacion, broly_peleando , direccion_goku,firstTimeScream
    global sprite2_x,sprite2_y, salud_broly,desconvertido,teles,firstTime,t,t2,modo_juego,player_energy,broly_energy,golpeando_sound_firsTime,ataque_lanzado, dialogo_goku,dialogo_broly, pos_txt2
    global goku_dialogo , broly_dialogo  , salud_goku 

    

    if modo_juego == "juego":
        t += velocidad
        t2 += velocidad
           
        frame_count7 += 1

        if frame_count7 % 15 == 0:
            current_sprite7 = (current_sprite7 + 1) % len(explosion)  

        if salud_goku > 0 :
            controles()
            mover_semillas()

            # Actualiza la posición de los kameha_derecha de ataque
            for sprite in kameha_derecha:
                sprite.pos = (sprite_x, sprite_y)

            # Actualiza la posición de los kameha_derecha izquierdo de ataque
            for sprite in kameha_izquierda:
                sprite.pos = (sprite_x, sprite_y)
                
            # Actualiza la posición de los kameha_derecha de pelea
            for pelea in goku_peleando_derecha:
                pelea.pos = (sprite_x, sprite_y)
                
            # Actualiza la posición de los kameha_derecha de teletransportación
            for tele in teles:
                tele.pos = (sprite_x, sprite_y)
                
            # Actualiza la posición de los kameha_derecha 
            for broly in broly_peleando_izquierda:
                broly.pos = (sprite2_x, sprite2_y)

            # Actualiza la posición de los kameha_derecha 
            for broly in broly_peleando_derecha:
                broly.pos = (sprite2_x, sprite2_y)

            # Actualiza la posición de la destransformacion de broly
            for broly in broly_desconvertido:
                broly.pos = (sprite2_x, sprite2_y)

            # Actualiza la posición de ataques fisicos
            for pelea in goku_peleando_izquierda:
                pelea.pos = (sprite_x, sprite_y)

            # Actualiza la posición de la animacion de ataque recargado
            for kamehameha2 in kameha_recargado_izquierda:
                kamehameha2.pos = (sprite_x, sprite_y)

            # Actualiza la posición de la animacion de ataque recargado
            for kamehameha2 in kameha_recargado_derecha:
                kamehameha2.pos = (sprite_x, sprite_y)
          
            

            # Incrementa el contador de cuadros
            frame_count += 1
            frame_count2 += 1
            frame_count3 += 1
            frame_count4 += 1
            frame_count5 += 1
            frame_count6 += 1
            frame_count8 += 1
            frame_count9 += 1
          
            
            # Actualiza la animación según el contador de cuadros
            if frame_count % animation_speed == 0:
                current_sprite = (current_sprite + 1) % len(kameha_derecha)
                
            if frame_count2 % animation_speed == 0:
                current_sprite2 = (current_sprite2 + 2) % len(cargando)
            
            if frame_count3 % animation_speed == 0:
                current_sprite3 = (current_sprite3 + 1) % len(goku_peleando_derecha)
                
            if frame_count4 % animation_speed == 0:
                current_sprite4 = (current_sprite4 + 1) % len(teles)
                
            if frame_count5 % animation_speedBroly == 0:
                current_sprite5 = (current_sprite5 + 1) % len(broly_peleando_izquierda)

            if frame_count6 % animation_speedBroly == 0:
                current_sprite6 = (current_sprite6 + 1) % len(broly_desconvertido)

            if frame_count8 % animation_speed == 0:
                current_sprite8 = (current_sprite8 + 1) % len(kameha_recargado_izquierda)

            current_sprite9 = (current_sprite9 + 1) % len(genkidama_bola)
           
            #BOLAS ENERGIA
            for i in range(len(bolas_energia)):

                if sprite2_x > sprite_x and not ataque_lanzado:
                    bolas_energia[i].x +=4
                    bolas_energia[i].image = "./sprites/goku/otros/bola_energia.png"
                    ataque_lanzado = False
                    
                elif sprite2_x < sprite_x and not ataque_lanzado:
                    bolas_energia[i].image = "./sprites/goku/otros/bola_energia_izquierda.png"
                    bolas_energia[i].x -=4
                    ataque_lanzado = False

                if bolas_energia[i].x > WIDTH or bolas_energia[i].x < 0:
                    bolas_energia.pop(i)
                    ataque_lanzado = False
                    break
                    
                colision = broly.collidelist(bolas_energia) 

                if colision != -1:
                    bolas_energia.pop(i)
                    salud_broly += random.randint(1,3) 
                    break
                        
            #LOGICA DE BROLLY
            if broly_peleando == True: 

                # Broly sigue al personaje principal con un retraso
                follow_speed = 0.0099  # Ajusta esta velocidad para cambiar el retraso
                if broly_peleando: 
                    sprite2_x += ((sprite_x - sprite2_x) * follow_speed)
            
                #Verifica si derrotamos a Broly.
                if salud_broly > 99:
                    broly_peleando = False  # Broly ha sido derrotado
                    modo_juego = "victoria"
                else:
                    # Detectar colisiones entre Broly y los ataques del personaje principal
                    if broly_peleando_izquierda[current_sprite5].colliderect(kameha_derecha[current_sprite]):
                        
                        if golpeando_sound_firsTime == True:
                            golpeando_sound.play()      
                        else:
                            golpeando_sound_firsTime = False     
                    
                        #Restando via a Broly con los ataques de Goku   
                        esquivar = random.randint(1,3)
                        esquivar_broly = random.randint(1,5)

                        if peleando == 1  and salud_broly < 99:
                            if esquivar_broly != 3:
                                salud_broly += random.random() / 3
                        elif attack == 1  and salud_broly < 99: 
                            if esquivar_broly != 3:
                                salud_broly += random.random() / 3      
                                
                        if attack_recargado == True and salud_broly < 99:
                            salud_broly += random.random() / 2

                        if esquivar != 3:
                            salud_goku -= random.random() / 3

                        #Retrocede cuando lo golpeo
                        if direccion_goku == "izquierda" and peleando == True or attack == True or attack_recargado == True:
                            sprite2_x -=1.2
                        elif direccion_goku == "derecha" and peleando == True or attack == True or attack_recargado == True:
                            sprite2_x +=1.2

    elif modo_juego == "menu":
        animacion_logo_menu()

        #Efecto de sonido choque
        if switch_efecto_menu == True:
            sonido_efecto.play()
            switch_efecto_menu = False

    elif modo_juego == "derrota" and firstTimeScream == True:
        golpeando_sound.stop() # IMPORTANTE ! HAY QUE DETENER UN .WAV PARA QUE DEJE SONAR OTRO, ME COSTO BASTANTE DESCUBRIELO XD
        sonido_grito_goku.play()
       
       #restableciendo valores
        firstTimeScream = False
       
    elif modo_juego == "dialogos":
        iniciar_dialogo(goku_dialogo,broly_dialogo) 

        if not dialogo_goku:
            sonido_dialogo_goku.play()
            dialogo_goku = True

        if not dialogo_broly:
            sonido_dialogo_broly.play()
            dialogo_broly = True
        
        if keyboard.space and modo_juego == "dialogos" and not (goku_dialogo.x < 100):
            pasar()

def elemento_volador_aleatorio():
    global elemento_volador_random

    #elemento_volador_random = 1
    elemento_volador_random = random.randint(1,2)

def on_key_down():
    global player_energy , teletransportacion , attack_recargado, current_sprite,attack, kame_sound_firstTime, genkidama
    
        # Ataque del personaje principal
    
    if keyboard.i : 
        sonido_carga.play() 

    if keyboard.j and player_energy > 20:
        if kame_sound_firstTime == True:
           
            kame_sound.play()  # Reproduce el sonido de teletransportación
            # kame_sound_firstTime = False
        attack = 1        
        player_energy -= 20  
    else:
        current_sprite = 0
        attack = 0

    if keyboard.t and salud_goku <= 40 and player_energy >= 35:
        genkidama = True
        player_energy //= 2
        pgzero.clock.schedule(llamarGenkidama,3)
        
    if keyboard.k and modo_juego == "juego" and len(bolas_energia) <=2 and player_energy >= 15:
    
        bola_energia = Actor("./sprites/goku/otros/bola_energia.png",(sprite_x,sprite_y))        
        bolas_energia.append(bola_energia)
        player_energy -= 15

    # Teletransportación del personaje principal
    if keyboard.u and player_energy >= 10 and modo_juego == "juego":

        golpeando_sound.stop()
        tele_sound.play()  # Reproduce el sonido de teletransportación
        teletransportacion = 1   
        player_energy -= 10
    
    else:
        teletransportacion = 0


    if keyboard.o and player_energy >= 30:
        attack_recargado = True
        player_energy -= 30
    else:
        attack_recargado = False

def elementos_secundarios():

    global genkidama_bola

    if genkidama_bola[current_sprite9].x < 800 and genkidama_mover == True:
        genkidama_bola[current_sprite9].x += 10

    if elemento_volador_random == 1:

        if  nube.x < 600:
            nube.draw()
            nube.x += 1
            nube.y = 180 + amplitud * math.sin(frecuencia * t)

    elif elemento_volador_random == 2:
            if nave.x>0:
                nave.draw()
                nave.x -= 1
                nave.y = 150 + amplitud * math.sin(frecuencia * t2)
    
    explosion[current_sprite7].draw()

def dibujar_semillas():
    for i in range(len(semillas)):
        semillas[i].draw()

def mover_semillas():
    global semillas,firstTime,salud_goku
    #Moviendo las semillas del ermitaño con sistema de probalididad + aleatoriedad.

    probabilidad_semilla = random.randint(1,20)

    
    if probabilidad_semilla == 15 and  salud_goku <= 30:
    

        contacto = kameha_derecha[current_sprite].collidelist(semillas)

        if contacto != -1:
            semillas.pop(contacto)
            salud_goku = 100

        for i in range(len(semillas)):
            if semillas[i].y < HEIGHT + 20:
                semillas[i].y += 15

        #Reproducir dialogo entre Krilin y Goku cuando este nececita semillas.
        for i in range(len(semillas)):
            if semillas[i].y >= 0 and firstTime == True and salud_goku>=0:
                sonido_pide.play() 
                firstTime = False

def on_mouse_down(pos):
    global modo_juego,salud_broly,salud_goku
    global pos_txt1 , pos_txt2 , dialogo_goku , dialogo_broly
    global sprite_x , sprite_y , sprite2_x , sprite2_y, carga, sonido_fight_reproducido
    global fondo_seleccionado , elemento_volador_random , switch_efecto_menu
    

    if goku_menu.collidepoint(pos):
        modo_juego = "dialogos"
        
    elif modo_juego == "derrota" and perdiste.collidepoint(pos):
        modo_juego = "menu"
        goku_dialogo.pos = (-200,450)
        broly_dialogo.pos = (1000,450)
        dialogo.pos = (1000,550)
        dialogo2.pos = (-200,550)
        #Dialogos Posiciones
        pos_txt1 = -280
        sonido_fight_reproducido = False
        pos_txt2 = 820
        elemento_volador_random = random.randint(1,2)
        nube.pos = (-1500,0)
        nave.pos = (1400,0)
        fondo_seleccionado = False
        switch_efecto_menu = True

        dialogo_goku = False
        dialogo_broly = False

        sprite_x = 200
        sprite_y = 470
        sprite2_x = 600
        sprite2_y = 450
        salud_goku = 30
        salud_broly = 0
    
def llamarGenkidama():
    global genkidama_mover
    print("GEnkidama moviendose")
    genkidama_mover = True

def barras():
    # Dibujar las barras de salud
    draw_health_bar_goku("Player", salud_goku, 75, 30, "green")
    draw_health_bar_broly("Broly", salud_broly, 520, 30, "black")
    
    draw_energy_bar(40, 50, player_energy, energy_max)
    draw_energy_bar(550, 50, broly_energy, energy_max)

def draw():
    
    global current_sprite6 , broly_peleando , kameha_derecha , sprite_x, sprite2_x  ,sprite_reproducido,firstTimeEndBattle,indice_fondos
    global goku_derrotado,elemento_volador_random,trayectoNave,trayectoNube, modo_juego,timer, fondo_seleccionado,sonido_fight_reproducido
    global sprite_left , sprite_right,sprite_y,moviendose,peleando,genkidama,salud_broly,genkidama_x,teletransportacion,genkidama_mover , current_sprite9
    if modo_juego == "juego":

        #Dibujando fondo1

        if not fondo_seleccionado:
            indice_fondos = random.choice(fondos)
            fondo_seleccionado = True
        
        indice_fondos.draw()
       
        elementos_secundarios()

        vs.draw()
        barras()    
        avatar_broly.draw()
        avatar_goku.draw()
        dibujar_semillas()

        if not sonido_fight_reproducido:
            fight_sound.play()
            sonido_fight_reproducido = True
        if nube.x < -1400 and elemento_volador_random ==1:
            fight.draw()
        else:
            if nave.x > 1200 and elemento_volador_random ==2: 
                fight.draw()

        for i in range(len(bolas_energia)):
            bolas_energia[i].draw()
        # ESTADOS DEL SPRITE
        if carga == True and not saltando:
            #Animacion de la carga de Goku.
            cargando[current_sprite2].pos = kameha_derecha[0].pos
            cargando[current_sprite2].y -= 18
            cargando[current_sprite2].draw()
        #Solo puede hacer el Kamehame-Ha si tiene energia
        if attack == True :
            #Animacion del Kamehame-ha!, en ambas direcciones
            if direccion_goku == "derecha" and salud_goku>=0 :
                kameha_derecha[current_sprite].draw()
            elif direccion_goku == "izquierda" and salud_goku>=0 :
                kameha_izquierda[current_sprite].draw()   
        elif attack_recargado == True :
            #Animacion del Kamehame-ha!, en ambas direcciones
            if direccion_goku == "derecha" and salud_goku>=0 :
                kameha_recargado_derecha[current_sprite8].draw()
                
            elif direccion_goku == "izquierda" and salud_goku>=0 :
                kameha_recargado_izquierda[current_sprite8].draw() 
        #Animacion cuando salto
        elif saltando == True:           
           
            if direccion_goku == "derecha":    
                #sprite_right.draw()
                volando_derecha.draw()
            else:            
                volando_izquierda.draw()          
        elif peleando == True:

            #Animacion de ataque fisico #1 hacia los lados
            if direccion_goku == "derecha":
                goku_peleando_derecha[current_sprite3].draw()
            elif direccion_goku == "izquierda":
                goku_peleando_izquierda[current_sprite3].draw()
        #Animacion y traslado de teletransportacion
        elif teletransportacion == True:
            teles[current_sprite4].draw()
            sprite_x = sprite2_x + 10       
        elif genkidama == True:
            genkidama_goku[current_sprite5].draw()
            genkidama_bola[current_sprite9].draw()    
            


            for i in range(len(genkidama_bola)):
                index = genkidama_bola[current_sprite9].collidelist(broly_peleando_izquierda)
                index2 = genkidama_bola[current_sprite9].collidelist(broly_peleando_derecha)
            
                if index != -1 or index2 != -1:

                    genkidama = False
                    genkidama_mover = False
                    current_sprite9 = 0
                    salud_broly += 50
                    
                
        else:      
            if moviendose == True and not saltando:
                if direccion_goku == "izquierda":
                    caminando_izquierda.x = sprite_x
                    caminando_izquierda.y = sprite_y
                    caminando_izquierda.draw()
                elif direccion_goku == "derecha":
                    caminando_derecha.x = sprite_x
                    caminando_derecha.y = sprite_y
                    caminando_derecha.draw()
            if salud_goku <= 0:  

                if direccion_goku == "derecha":
                    goku_derrotado.pos = (sprite2_x-50,sprite2_y+20)
                    goku_derrotado.draw()
                    
                else:
                    goku_derrotado.pos = (sprite2_x+50,sprite2_y+20)
                    goku_derrotado.draw()
            else:
                #Girar hacia los estados, estando estatico.
                if direccion_goku == "izquierda" and not moviendose :
                    sprite_left.draw()
                
                elif direccion_goku == "derecha" and not moviendose :
                   sprite_right.draw()
                    
        #PROGRAMACION BROLY
        #Animacion de ataque de Broly
        if salud_broly <= 100 and salud_goku > 0 :
            

            if abs(sprite_x - sprite2_x) < sprite_left.width +30 and not peleando:
               

                if sprite2_x > sprite_x:
                    broly_peleando_izquierda[current_sprite5].draw()
                elif sprite2_x < sprite_x:
                    broly_peleando_derecha[current_sprite5].draw()

            else:

                if sprite2_x > sprite_x:
                    broly_peleando_izquierda[1].draw()
                elif sprite2_x < sprite_x:
                    broly_peleando_derecha[1].draw()

        #Broly cambia de postura al ganar.
        elif salud_goku<=0:
            broly_peleando_derecha[5].draw()
            pgzero.clock.schedule( terminar_juego,3)
           
            
        else:
            if modo_juego == "victoria" and not sprite_reproducido:
    
                broly_desconvertido[current_sprite6].draw()
                modo_juego = "derrota"
            else:
                broly_desconvertido[current_sprite6].draw()

            broly_peleando = 0    
    elif modo_juego == "victoria":
        
        ganaste.draw()
        if firstTimeEndBattle == True:

            golpeando_sound.stop()
            kame_sound.stop()
            sonido_final_goku.play()
            firstTimeEndBattle  = False
    elif modo_juego == "menu":
        menu_wall.draw()
        logo.draw()
        goku_menu.draw()
        broly_menu.draw()
        logica_ataque_persecucion()
    elif modo_juego == "derrota":
        perdiste.draw()
    elif modo_juego == "dialogos":
        fondo_dialogo.draw()
        vsGrande.draw()
        goku_dialogo.draw()
        broly_dialogo.draw()
        dialogo.draw()
        dialogo2.draw()


        if not( goku_dialogo.x < 100):
            screen.draw.text("¡No subestimes mi poder, Broly!", pos=(pos_txt1, 540), fontsize=20, color="white")
            screen.draw.text("¡Estoy listo para luchar!", pos=(pos_txt1, 560), fontsize=20, color="white")


        if not (broly_dialogo.x > 700):
            screen.draw.text("Kkkkkk Kkkk Kkk", pos=(pos_txt2, 540), fontsize=20, color="white")
            screen.draw.text("¡Kaaaa Kaaakaaarotooooo!", pos=(pos_txt2, 560), fontsize=20, color="white")
   


generar_semillas()
sonidos()
pgzrun.go()