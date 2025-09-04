from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.font = ("Arial", 16, "normal")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-380, 270)
        self.write(f"Score: {self.score}", align="left", font=self.font)
        self.goto(300, 270)
        self.write(f"Lives: {self.lives}", align="left", font=self.font)

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def is_game_over(self):
        return self.lives <= 0

    def reset_score(self):
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def display_winner(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Arial", 24, "normal"))