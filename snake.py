from random import randrange, choice, sample
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# --- Colores disponibles (excluyendo rojo) ---
colors = ["blue", "purple", "orange", "yellow", "brown"]

# Elegimos dos colores distintos
snake_color, food_color = sample(colors, 2)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Si la serpiente come la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # --- Mover comida un pasito aleatorio ---
    direction = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])
    new_food = food.copy()
    new_food.move(direction)

    if inside(new_food):  # solo se mueve si sigue dentro
        food.move(direction)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # <- color de la serpiente

    square(food.x, food.y, 9, food_color)  # <- color de la comida
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
