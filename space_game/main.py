import turtle
import math

screen = turtle.Screen()
screen.title("Space Invaders Game Python")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.penup()
player.color("cyan")
player.setheading(90)
player.goto(0, -260)
player_speed = 20

bullet = turtle.Turtle()
bullet.shape("square")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
bullet.penup()
bullet.color("yellow")
bullet.speed(0)
bullet.goto(0, -400)
bullet.state = "ready"
bullet_speed = 35


enemies = []
enemy_speed = 1.5
enemy_drop = 30

def make_enemies():
    start_x = -225
    start_y = 250

    for row in range(4):
        for col in range(9):
            enemy = turtle.Turtle()
            enemy.shape("circle")
            enemy.color("red")
            enemy.penup()
            enemy.speed(0)
            x = start_x + (50 * col)
            y = start_y - (50 * row)
            enemy.goto(x, y)
            enemies.append(enemy)

make_enemies()

barriers = []
barrier_positions = [-200, 0, 200]

def make_barriers():
    for x in barrier_positions:
        for i in range(4):
            barrier = turtle.Turtle()
            barrier.shape("square")
            barrier.color("green")
            barrier.speed(0)
            barrier.penup()
            barrier.goto(x +(i * 25 - 25), -180)
            barriers.append(barrier)

make_barriers()

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
score = 0
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)

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

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False

screen.listen()
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(fire_bullet, "space")


is_running = True
while True:
    screen.update()

    if bullet.state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet.state = "ready"

    move_enemies = False
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        if x > 380 or x < -380:
            move_enemies = True

        if bullet.state is "fire" and is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -400)

            enemy.goto(1000, 1000)
            enemies.remove(enemy)

            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            game_over_pen.write("GAME OVER!", align="center", font=("Courier", 30, "bold"))
            is_running = False
            break

        for barrier in barriers:
            if is_collision(enemy, barrier):
                barrier.goto(1000, 1000)
                if barrier in barriers:
                    barriers.remove(barrier)

    if move_enemies:
        enemy_speed *= -1
        for enemy in enemies:
            y = enemy.ycor()
            y -= enemy_drop
            enemy.sety(y)

            if y < -240:
                game_over_pen.write("GAME OVER!", align="center", font=("Courier", 30, "bold"))
                is_running = False

    if bullet.state == "fire":
        for barrier in barriers:
            if is_collision(bullet, barrier):
                bullet.hideturtle()
                bullet.state = "ready"
                bullet.goto(0, -400)
                barrier.goto(1000, 1000)
                if barrier in barriers:
                    barriers.remove(barrier)
                break

    if len(enemies) == 0:
        game_over_pen.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
        is_running = False

screen.mainloop()
