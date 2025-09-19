"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
import turtle
import math
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    side = end.x - start.x
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()


def circle(start, end):
    """Draw circle from start to end (start=center, end=radio)."""
    turtle.up()
    radius = math.dist([start.x, start.y], [end.x, end.y])
    turtle.goto(start.x, start.y - radius)  # mover a la parte baja del círculo
    turtle.setheading(0)  # orientación estándar
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def rectangle(start, end):
    """Draw rectangle using start and end as opposite corners."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    width = end.x - start.x
    height = end.y - start.y
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()


def triangle(start, end):
    """Draw triangle using start and end as base corners."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    turtle.goto(end.x, end.y)      # segundo vértice
    turtle.goto(start.x, end.y)    # tercer vértice
    turtle.goto(start.x, start.y)  # cerrar

    turtle.end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


# ----------- Configuración del programa -----------
state = {'start': None, 'shape': line}
turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(tap)
turtle.listen()

# Atajos de teclado
turtle.onkey(turtle.undo, 'u')
turtle.onkey(lambda: turtle.color('black'), 'K')
turtle.onkey(lambda: turtle.color('white'), 'W')
turtle.onkey(lambda: turtle.color('green'), 'G')
turtle.onkey(lambda: turtle.color('blue'), 'B')
turtle.onkey(lambda: turtle.color('red'), 'R')
turtle.onkey(lambda: turtle.color('yellow'), 'Y')

turtle.onkey(lambda: store('shape', line), 'l')
turtle.onkey(lambda: store('shape', square), 's')
turtle.onkey(lambda: store('shape', circle), 'c')
turtle.onkey(lambda: store('shape', rectangle), 'r')
turtle.onkey(lambda: store('shape', triangle), 't')

turtle.done()
