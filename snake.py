import turtle
import random

turtle.tracer(1,0)

size_X=800
size_Y=500
turtle.setup(size_X, size_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
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
RIGHT_ARROW = "Right"
TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 2
DOWN = 1
RIGHT = 3

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction
    direction = UP
    #move_snake()
    print("you pressed the up key!")

def down():
    global direction
    direction = DOWN
    #move_snake()
    print("you pressed the down key!")
def left():
    global direction
    direction = LEFT
    #move_snake()
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
    #move_snake()
    print("you pressed the right key!")
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randit(min_y,max_y)*SQUARE_SIZE
    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos [1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    #special place ( part 5)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        turtle.ontimer(move_snake,TIME_STEP)
        
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
        
    turtle.ontimer(move_snake,TIME_STEP)
    


        


turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for food_ID in food_pos:
    food.goto(food_ID)
    Food = food.stamp()
    food_stamps.append(Food)
    food.hideturtle()

move_snake()  
  
    
        


