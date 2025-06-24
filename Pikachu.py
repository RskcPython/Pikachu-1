import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
pikachu = turtle.Turtle()
pikachu.speed(3)

# Draw face
pikachu.penup()
pikachu.goto(0, -100)
pikachu.pendown()
pikachu.color("yellow")
pikachu.begin_fill()
pikachu.circle(100)
pikachu.end_fill()

# Draw left ear
pikachu.penup()
pikachu.goto(-70, 120)
pikachu.setheading(100)
pikachu.pendown()
pikachu.begin_fill()
pikachu.circle(40, 80)
pikachu.left(100)
pikachu.circle(40, 80)
pikachu.end_fill()

# Draw right ear
pikachu.penup()
pikachu.goto(70, 120)
pikachu.setheading(80)
pikachu.pendown()
pikachu.begin_fill()
pikachu.circle(-40, 80)
pikachu.right(100)
pikachu.circle(-40, 80)
pikachu.end_fill()

# Draw eyes
def draw_eye(x, y):
    pikachu.penup()
    pikachu.goto(x, y)
    pikachu.setheading(0)
    pikachu.color("black")
    pikachu.begin_fill()
    pikachu.circle(10)
    pikachu.end_fill()

draw_eye(-35, 40)
draw_eye(35, 40)

# Draw red cheeks
def draw_cheek(x, y):
    pikachu.penup()
    pikachu.goto(x, y)
    pikachu.color("red")
    pikachu.begin_fill()
    pikachu.circle(15)
    pikachu.end_fill()

draw_cheek(-55, 0)
draw_cheek(55, 0)

# Draw smile
pikachu.penup()
pikachu.goto(-25, -30)
pikachu.setheading(-60)
pikachu.pendown()
pikachu.circle(30, 120)

pikachu.hideturtle()
turtle.done()