import pgzrun
from pgzero.clock import clock
import random
import math
import os 

# Configura el tamaño de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 30

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

# Carga de Actores
broly_menu = Actor("broly_menu.png",(x_broly_menu,y_broly_menu))
goku_menu =  Actor("goku_menu.png",(x_goku_menu,y_goku_menu))
avatar_broly = Actor("avatar_broly.png",(760,40))
fight = Actor("fight.png",(center_x  , center_y + 140))
vs = Actor("vs.png",(center_x  , center_y - 35))
logo =  Actor("logo.png",(center_x  , center_y)) # type: ignore
avatar_goku =  Actor("avatar_goku.png",(48,40))
nube =  Actor("nube.png", pos = (-1500,0)) # type: ignore
nave =  Actor("nave.png",pos = (1400,0))
kamehouse = Actor("kamehouse.png")
perdiste = Actor("derrota.jpeg")
menu_wall = Actor("menu.jpeg")

ganaste =  Actor("win.jpeg")
broly1 = Actor("broly0.png")
broly2 = Actor("broly1.png")
broly3 = Actor("broly2.png")
broly4 = Actor("broly3.png")
broly5 = Actor("broly4.png")
broly6 = Actor("broly5.png")

tele1 = Actor("tele0.png")
tele2 = Actor("tele1.png")
tele3 = Actor("tele2.png")

fondo =  Actor("c.jpeg")
fondo2 = Actor("f.jpeg")
fondo3 = Actor("v.jpeg")
fondo4=  Actor("a.jpeg")

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

goku_derrotado = Actor("goku_derrotado",pos = (sprite_x , sprite_y))

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

explosion0 = Actor("explosion0.png",(center_x +2 , center_y - 35))
explosion1 = Actor("explosion1.png",(center_x +2 , center_y - 35))
explosion2 = Actor("explosion2.png",(center_x +2 , center_y - 35))
explosion3 = Actor("explosion3.png",(center_x +2 , center_y - 35))
explosion4 = Actor("explosion4.png",(center_x +2 , center_y - 35))
explosion5 = Actor("explosion5.png",(center_x +2 , center_y - 35))

#Listas de cada animacion con  todos los actores en ellas.
teles =  [tele1, tele2, tele3]
cargas = [carga1, carga2, carga3]
brolys = [broly1, broly2, broly3, broly4, broly5, broly6]
peleas = [pelea1, pelea2, pelea3, pelea4, pelea5, pelea6]
explosion = [explosion0,explosion1,explosion2,explosion3,explosion4,explosion5]
peleas_left = [pelea1_left, pelea2_left, pelea3_left, pelea4_left, pelea5_left, pelea6_left]
sprite_goku_kamehameha = [sprite_right,kameha1,kameha2,kameha3,kameha4,kameha5,kameha6, kameha7,kameha9,kameha9]
brolys_right = [broly1_right, broly2_right, broly3_right, broly4_right, broly5_right, broly6_right]
broly_desconvertido = [broly0_desconvertido,broly1_desconvertido,broly2_desconvertido,broly3_desconvertido]
kameha_izq = [sprite_left,kameha1_izq, kameha2_izq, kameha3_izq, kameha4_izq, kameha5_izq, kameha6_izq, kameha7_izq, kameha8_izq,  kameha9_izq]
fondos = [fondo,fondo2,fondo3,fondo4]

#Inicializando lista vacia de semillas, rellenada con 3.
semillas  = [] 

x = random.randint(0,WIDTH)
y = random.randint(0,1800)
semilla = Actor("./semillas/semilla.png" , (x,-y))
semillas.append(semilla)

fight.pos = (WIDTH // 2, HEIGHT // 2)

# Variables de la animación
current_sprite  = 0   # ataque
current_sprite2 = 0  # carga
current_sprite3 = 0  # pelea
current_sprite4 = 0  # teletransportación
current_sprite5 = 0  # broly
current_sprite6 = 0  # broly desconvertido
current_sprite7 = 0 # explosion del vs

animation_speed = 8  # Velocidad de la animación, ajustar según necesidad
animation_speedBroly = 16  # Velocidad de la animación, ajustar según necesidad

#Estos frames representan el cuadro de la cada animacion, corresponden con los 'current_spritex' (Estan unas lineas arriba).
frame_count  = 0
frame_count2 = 0
frame_count3 = 0
frame_count4 = 0
frame_count5 = 0
frame_count6 = 0
frame_count7 = 0

# Variables de estado necesarias para controlar varios aspectos del juego
attack = False
carga = 0
saltando = False
peleando = False
teletransportacion = False
broly_peleando = True
desconvertido = False
elemento_volador_random = random.randint(1,2)
tiempo = 0

modo_juego = "menu"

sprite_reproducido = False
firstTime = True
firstTimeScream = True
firstTimeEndBattle = True
kame_sound_firstTime = True
switch_efecto_menu = True
golpeando_sound_firsTime = True

trayectoNave = False
trayectoNube = True


fondo_seleccionado = False
indice_fondos = 0

timer = 0

# Direccion de personaje princial, Papucho Goku! :)
direccion_goku = "right"

# Variables de salud
salud_broly = 0
salud_goku = 100


def sonidos():
    # Cargar y reproduccion de sonidos

    global tele_sound,golpeando_sound,kame_sound,salto_sound,sonido_carga,sonido_muere
    global sonido_curar,sonido_pide,sonido_final_goku,sonido_grito_goku,sonido_efecto

    #Efectos de sonido del juego en .wav
    tele_sound = sounds.sonidotransportacion  # Asegúrate de que el archivo teletransportacion.wav está en la carpeta sounds
    tele_sound.set_volume(0.2)

    golpeando_sound = sounds.sonidogolpeando  # Asegúrate de que el archivo golpeando.wav está en la carpeta sounds
    golpeando_sound.set_volume(0.3)

    kame_sound = sounds.sonidokame  # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    kame_sound.set_volume(0.6)

    salto_sound = sounds.sonidosalto # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    salto_sound.set_volume(0.2)

    sonido_carga = sounds.sonidocarga # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    sonido_carga.set_volume(0.3)

    sonido_muere = sounds.muere # Asegúrate de que el archivo kame.wav está en la carpeta sounds
    sonido_muere.set_volume(0.1)

    sonido_curar = sounds.sonidocurar # Asegúrate de que el archivo curar.wav está en la carpeta sounds
    sonido_curar.set_volume(0.3)

    sonido_pide = sounds.sonidopidesemilla # Asegúrate de que el archivo pide.wav está en la carpeta sounds
    sonido_pide.set_volume(0.6)

    sonido_final_goku = sounds.sonidofinalgoku # Asegúrate de que el archivo final.wav está en la carpeta sounds
    sonido_final_goku.set_volume(0.6)

    sonido_grito_goku = sounds.gritogoku # Asegúrate de que el archivo grito.wav está en la carpeta sounds
    sonido_grito_goku.set_volume(1.5)

    sonido_efecto = sounds.efectomenu # Asegúrate de que el archivo curar.wav está en la carpeta sounds
    sonido_efecto.set_volume(1.5)


    if modo_juego == "menu":
        music.play("musicmenu.mp3")
        music.set_volume(0.5)
    elif modo_juego == "juego":
        music.play("sound.mp3")

def saludar():
    print("hi")

def terminar_juego():
    print("jelo")
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

    global sprite_x, sprite_y, player_energy,carga,direccion_goku,saltando,attack,current_sprite,peleando,teletransportacion, kame_sound_firstTime
    # Movimiento del personaje principal
    if keyboard.d and sprite_x<WIDTH - 16:
        sprite_x += 2
        direccion_goku = "right"
    elif keyboard.a and sprite_x>=16:
        sprite_x -= 2
        direccion_goku = "left"
        
    # Salto del personaje principal
    if keyboard.space:
        salto_sound.play()
        sprite_goku_kamehameha[0].y -= 150 
        saltando = 1
    else:
        saltando = 0
    
    # Ataque del personaje principal
    if keyboard.j and player_energy > 0:
        if kame_sound_firstTime == True:
           
            kame_sound.play()  # Reproduce el sonido de teletransportación
            kame_sound_firstTime = False
        attack = 1
        
        player_energy -= random.random()
        
    
    else:
        current_sprite = 0
        attack = 0
        
    # Carga del personaje principal
    if keyboard.i:
        sonido_carga.play()
        carga = 1
        if player_energy < energy_max:
            player_energy += 1
    

    else:
        carga = 0
        
    # Pelea del personaje principal
    if keyboard.l:
        peleando = 1
    else:
        peleando = 0
        
    # Teletransportación del personaje principal
    if keyboard.u:

        golpeando_sound.stop()
        tele_sound.play()  # Reproduce el sonido de teletransportación
        teletransportacion = 1      
    
    else:
        teletransportacion = 0

def update(dt):
    global current_sprite, current_sprite2, current_sprite3, current_sprite4, current_sprite5,current_sprite6,current_sprite7
    global frame_count, frame_count2, frame_count3, frame_count4, frame_count5,frame_count6,frame_count7,firstTimeEndBattle,switch_efecto_menu
    global attack, carga, sprite_x, sprite_y, saltando, peleando, teletransportacion, broly_peleando , direccion_goku,firstTimeScream
    global sprite2_x, salud_broly, salud_goku,desconvertido,teles,firstTime,t,t2,modo_juego,player_energy,broly_energy,golpeando_sound_firsTime

    if modo_juego == "juego":
        t += velocidad
        t2 += velocidad

      
        mover_semillas()

        #Reproducir dialogo entre Krilin y Goku cuando este nececita semillas.
        for i in range(len(semillas)):
            if semillas[i].y >= 0 and firstTime == True and salud_goku>=0:
                sonido_pide.play() 
                firstTime = False
       
        # Actualiza la posición de los sprite_goku_kamehameha de ataque
        for sprite in sprite_goku_kamehameha:
            sprite.pos = (sprite_x, sprite_y)

        # Actualiza la posición de los sprite_goku_kamehameha izquierdo de ataque
        for sprite in kameha_izq:
            sprite.pos = (sprite_x, sprite_y)
            
        # Actualiza la posición de los sprite_goku_kamehameha de pelea
        for pelea in peleas:
            pelea.pos = (sprite_x, sprite_y)
            
        # Actualiza la posición de los sprite_goku_kamehameha de teletransportación
        for tele in teles:
            tele.pos = (sprite_x, sprite_y)
            
        # Actualiza la posición de los sprite_goku_kamehameha 
        for broly in brolys:
            broly.pos = (sprite2_x, sprite2_y)

        # Actualiza la posición de los sprite_goku_kamehameha 
        for broly in brolys_right:
            broly.pos = (sprite2_x, sprite2_y)

        # Actualiza la posición de la destransformacion de broly
        for broly in broly_desconvertido:
            broly.pos = (sprite2_x, sprite2_y)

        # Actualiza la posición de la destransformacion de broly
        for pelea in peleas_left:
            pelea.pos = (sprite_x, sprite_y)
        
        # Incrementa el contador de cuadros
        frame_count += 1
        frame_count2 += 1
        frame_count3 += 1
        frame_count4 += 1
        frame_count5 += 1
        frame_count6 += 1
        frame_count7 += 1
        
        # Actualiza la animación según el contador de cuadros
        if frame_count % animation_speed == 0:
            current_sprite = (current_sprite + 1) % len(sprite_goku_kamehameha)
            
        if frame_count2 % animation_speed == 0:
            current_sprite2 = (current_sprite2 + 2) % len(cargas)
        
        if frame_count3 % animation_speed == 0:
            current_sprite3 = (current_sprite3 + 1) % len(peleas)
            
        if frame_count4 % animation_speed == 0:
            current_sprite4 = (current_sprite4 + 1) % len(teles)
            
        if frame_count5 % animation_speed == 0:
            current_sprite5 = (current_sprite5 + 1) % len(brolys)

        if frame_count6 % animation_speedBroly == 0:
            current_sprite6 = (current_sprite6 + 1) % len(broly_desconvertido)

        if frame_count7 % animation_speedBroly == 0:
            current_sprite7 = (current_sprite7 + 1) % len(explosion)
        

        if broly_peleando == True: 

            controles()
            
            # Broly sigue al personaje principal con un retraso
            follow_speed = 0.007  # Ajusta esta velocidad para cambiar el retraso
            if broly_peleando == 1: 
                sprite2_x += ((sprite_x - sprite2_x) * follow_speed)
        
            
            #Verifica si derrotamos a Broly.
            if salud_broly > 99:
                broly_peleando = False  # Broly ha sido derrotado
                modo_juego = "victoria"
            else:
                # Detectar colisiones entre Broly y los ataques del personaje principal
                if brolys[current_sprite5].colliderect(sprite_goku_kamehameha[current_sprite]):
                    
                    if golpeando_sound_firsTime == True:
                        golpeando_sound.play()      
                    else:
                        golpeando_sound_firsTime = False     
                
                    #Restando via a Broly con los ataques de Goku   
                    if peleando == 1  and salud_broly < 99:
                        salud_broly += random.random() / 3
                    elif attack == 1  and salud_broly < 99: 
                        salud_broly += random.random() / 3      


                    salud_goku -= random.random() / 3

                    #Retrocede cuando lo golpeo
                    if direccion_goku == "left":
                        sprite2_x -=1
                    elif direccion_goku == "right":
                        sprite2_x += 1

    elif modo_juego == "menu":
        animacion_logo_menu()

        #Efecto de sonido choque
        if switch_efecto_menu == True:
            sonido_efecto.play()
            switch_efecto_menu = False

    elif modo_juego == "derrota" and firstTimeScream == True:
        golpeando_sound.stop() # IMPORTANTE ! HAY QUE DETENER UN .WAV PARA QUE DEJE SONAR OTRO, ME COSTO BASTANTE DESCUBRIELO XD
        sonido_grito_goku.play()
        firstTimeScream = False

def elemento_volador_aleatorio():
    global elemento_volador_random

    elemento_volador_random = random.randint(1,100)

def elementos_secundarios():

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
    if probabilidad_semilla == 15 and  salud_goku <= 50:

        #Dibujado de las semillas del ermitaño
            #Moviendo las semillas hacia abajo

        contacto = sprite_goku_kamehameha[current_sprite].collidelist(semillas)

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
    global modo_juego
    if goku_menu.collidepoint(pos):
        modo_juego = "juego"

def barras():
    # Dibujar las barras de salud
    draw_health_bar_goku("Player", salud_goku, 40, 30, "green")
    draw_health_bar_broly("Broly", salud_broly, 520, 30, "black")
    
    draw_energy_bar(40, 50, player_energy, energy_max)
    draw_energy_bar(550, 50, broly_energy, energy_max)

def draw():
    
    global current_sprite6 , broly_peleando , sprite_goku_kamehameha , sprite_x, sprite2_x  ,sprite_reproducido,firstTimeEndBattle,indice_fondos
    global goku_derrotado,elemento_volador_random,trayectoNave,trayectoNube, modo_juego,timer, fondo_seleccionado

    if modo_juego == "juego":

        #Dibujando fondo1

        if fondo_seleccionado == False:
            indice_fondos = random.choice(fondos)
            fondo_seleccionado = True
        
        indice_fondos.draw()
        fight.draw()
        elementos_secundarios()
        vs.draw()
        barras()    
        avatar_broly.draw()
        avatar_goku.draw()
        dibujar_semillas()

        if carga == 1:
            #Animacion de la carga de Goku.
            cargas[current_sprite2].pos = sprite_goku_kamehameha[0].pos
            cargas[current_sprite2].y -= 18
            cargas[current_sprite2].draw()

        #Solo puede hacer el Kamehame-Ha si tiene energia
        if attack == 1 :
            #Animacion del Kamehame-ha!, en ambas direcciones
            if direccion_goku == "right" and salud_goku>=0 :
                sprite_goku_kamehameha[current_sprite].draw()
            elif direccion_goku == "left" and salud_goku>=0 :
                kameha_izq[current_sprite].draw()          

        #Animacion cuando salto
        elif saltando == 1:
            sprite_goku_kamehameha[0].draw()
        elif peleando == 1:

            #Animacion de ataque fisico #1 hacia los lados
            if direccion_goku == "right":
                peleas[current_sprite3].draw()
            elif direccion_goku == "left":
                peleas_left[current_sprite3].draw()
        #Animacion y traslado de teletransportacion
        elif teletransportacion == 1:
            teles[current_sprite4].draw()
            sprite_x = sprite2_x + 10       
        else:
            
            #Girar hacia los estados, estando estatico.
            if direccion_goku == "left" :
                kameha_izq[0].draw()
            elif direccion_goku == "right":
                sprite_goku_kamehameha[0].draw()
            else:
                
                goku_derrotado.pos = (sprite2_x+50,sprite2_y+20)
                goku_derrotado.draw()
        
        #Animacion de ataque de Broly
        if salud_broly < 150 and salud_goku >= 0 and broly_peleando == 1:
            if sprite2_x > sprite_x:
                brolys[current_sprite5].draw()
            elif sprite2_x < sprite_x:
                brolys_right[current_sprite5].draw()
        
        #Broly cambia de postura al ganar.
        elif salud_goku<=0:
            brolys_right[5].draw()
            modo_juego = "derrota"
        else:
            if modo_juego == "victoria" and not sprite_reproducido:
    
                broly_desconvertido[current_sprite6].draw()
                sprite_reproducido = True
            else:
                broly_desconvertido[3].draw()

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
        kamehouse.draw()


if modo_juego == "derrota":
    clock.schedule_unique(saludar, 2.0)

sonidos()
pgzrun.go()