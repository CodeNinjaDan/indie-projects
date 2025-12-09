import turtle

screen = turtle.Screen()
screen.title("Space Invaders Game Python")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.penup()
player.color("white")
player.setheading(90)
player.goto(0, -260)
player_speed = 20


bullet = turtle.Turtle()
bullet.speed("square")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
bullet.penup()
bullet.color("yellow")
bullet.speed(0)
bullet.goto(0, -400)
bullet.state = "ready"
bullet_speed = 35

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

def fire_bullet():
    if bullet.state == "ready":
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.state = "fire"

screen.listen()
screen.onkey(move_right, "right")
screen.onkey(move_left, "left")
screen.onkey(fire_bullet, "space")
