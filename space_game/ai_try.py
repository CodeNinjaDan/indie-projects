import turtle
import math

# --- 1. Screen Setup ---
wn = turtle.Screen()
wn.title("Space Invaders by Python Turtle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic updates for performance

# Register shapes (optional, but good for custom feel)
wn.register_shape("invader", ((-10, 0), (10, 0), (10, 10), (-10, 10)))

# --- 2. Game Objects ---

# Player Ship
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)
player_speed = 20

# Player Bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("square")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
bullet.color("yellow")
bullet.penup()
bullet.goto(0, -400)  # Hide off screen
bullet.state = "ready"  # "ready" means ready to fire, "fire" means moving
bullet_speed = 35

# Barriers (Defensive Shields)
barriers = []
barrier_positions = [-200, 0, 200]


def create_barriers():
    for x_pos in barrier_positions:
        # Create a cluster of 3 blocks per barrier position
        for i in range(3):
            b = turtle.Turtle()
            b.speed(0)
            b.shape("square")
            b.color("green")
            b.penup()
            # Offset them slightly to make a wider shield
            b.goto(x_pos + (i * 25 - 25), -180)
            barriers.append(b)


create_barriers()

# Enemies (Invaders)
enemies = []
enemy_speed = 1.5  # Initial horizontal speed
enemy_drop = 30  # How far they drop down


def create_enemies():
    start_x = -225
    start_y = 250
    for row in range(4):  # 4 Rows
        for col in range(9):  # 9 Columns
            enemy = turtle.Turtle()
            enemy.speed(0)
            enemy.shape("circle")  # Simple circle or custom shape
            enemy.color("red")
            enemy.penup()
            x = start_x + (50 * col)
            y = start_y - (50 * row)
            enemy.goto(x, y)
            enemies.append(enemy)


create_enemies()

# Score & Game Over Text
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


# --- 3. Functions ---

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)


def fire_bullet():
    if bullet.state == "ready":
        # Start bullet just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.state = "fire"


def is_collision(t1, t2):
    # Calculate distance using Pythagorean theorem
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:  # 25 pixels threshold
        return True
    else:
        return False


# Key Bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# --- 4. Main Game Loop ---
is_running = True

while is_running:
    wn.update()  # Update the screen manually

    # Move the bullet
    if bullet.state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check bullet boundary (top of screen)
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet.state = "ready"

    # Move Enemies
    move_down = False

    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Check side boundaries and trigger drop
        if x > 380 or x < -380:
            move_down = True

        # Check Collision: Bullet vs Enemy
        if bullet.state == "fire" and is_collision(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -400)

            # Reset enemy (or remove)
            # For this version, we reset enemy to a random top spot to keep game going
            # or simply hide them. Let's hide them (Classic style).
            enemy.goto(1000, 1000)  # Move off screen
            enemies.remove(enemy)  # Remove from list

            # Update Score
            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        # Check Collision: Enemy vs Player (Game Over)
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            game_over_pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
            is_running = False
            break  # Exit loop

        # Check Collision: Enemy vs Barrier (Aliens eat shields)
        for barrier in barriers:
            if is_collision(enemy, barrier):
                barrier.goto(1000, 1000)
                if barrier in barriers:
                    barriers.remove(barrier)

    # Logic to move all enemies down if one hit the wall
    if move_down:
        enemy_speed *= -1  # Reverse direction
        for enemy in enemies:
            y = enemy.ycor()
            y -= enemy_drop  # Move down
            enemy.sety(y)

            # Check for Game Over (Aliens reached bottom)
            if y < -230:
                game_over_pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
                is_running = False

    # Check Collision: Bullet vs Barrier (Friendly Fire)
    # If you shoot your own shield, it breaks
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

    # Win Condition
    if len(enemies) == 0:
        game_over_pen.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
        is_running = False

wn.mainloop()