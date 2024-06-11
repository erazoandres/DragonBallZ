import pgzrun

player_health = 100
broly_health = 0

def draw_health_bar(name, health, x, y, color):
    #Dibujando los rectangulos de la vida de ambos personajes.
    screen.draw.text(name, (x, y - 20), color="white")
    bar_width = 160
    bar_height = 20
    health_percentage = health / 100
    fill_width = bar_width * health_percentage
    screen.draw.filled_rect(Rect((x, y), (bar_width, bar_height)), (0, 255, 0))
    screen.draw.filled_rect(Rect((x, y), (fill_width, bar_height)), color)
    screen.draw.rect(Rect((x, y), (fill_width, bar_height)), "white")



def draw():


    screen.fill("blue")
    draw_health_bar("Son Goku", player_health, 40, 30, (255, 0, 0))
    draw_health_bar("Broly", broly_health, 462, 30, "red")


def update():
    global broly_health
    if keyboard.space and broly_health<=100:
        broly_health +=1

pgzrun.go()
