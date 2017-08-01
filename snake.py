import turtle
import random

turtle.tracer(1,0)

size_X=800
size_Y=500
turtle.setup(size_X, size_Y)

turtle.penup()

SQUARE_SIZE = 20
6 = 10

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos() [0]
    y_pos=snake.pos() [1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(my_pos)
    pos_list.append(my_pos)

    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGH_ARROW = "Right"
TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 2
DOWN = 1
RIGHT = 3

direction = UP
def up():
    global direction
    direction = UP
    move_snake()
    print("you pressed the up key!")

def down():
    global direction
    direction = DOWN
    move_snake()
    print("you pressed the down key!")

def left():
    global direction
    direction = LEFT
    move_snake()
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
    move_snake()
    print("you pressed the right key!")
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos [1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")
        


