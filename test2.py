import turtle

# Configurar la pantalla
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Dibujo de Estrella con Tortuga")

# Crear una tortuga
star = turtle.Turtle()
star.color("yellow")
star.speed(2)  # Velocidad de la tortuga

# Función para dibujar una estrella
def draw_star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)  # Ángulo para crear la estrella

# Dibujar una estrella de tamaño 100
draw_star(star, 100)

# Esconder la tortuga y mostrar el dibujo
star.hideturtle()

# Esperar al usuario para cerrar la ventana
wn.mainloop()
