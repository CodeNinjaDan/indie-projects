import turtle
from ball import Ball
from brick_wall import BrickWall
from scoreboard import Scoreboard
from collision_manager import CollisionManager
import time

class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.setup_screen()
        self.ball = Ball()
        self.board = self.create_board()
        self.brick_wall = BrickWall()
        self.scoreboard = Scoreboard()
        self.collision_manager = CollisionManager(self.ball, self.board, self.brick_wall, self.scoreboard)
        self.game_is_on = True
        self.setup_controls()

    def setup_screen(self):
        self.screen.bgcolor("black")
        self.screen.title("Breakout Game!")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def create_board(self):
        board = turtle.Turtle()
        board.shape("square")
        board.color("white")
        board.shapesize(stretch_wid=1, stretch_len=5)
        board.penup()
        board.goto(0, -200)
        return board

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")

    def move_left(self):
        if self.board.xcor() > -350:
            new_x = self.board.xcor() - 20
            self.board.goto(new_x, self.board.ycor())

    def move_right(self):
        if self.board.xcor() < 350:
            new_x = self.board.xcor() + 20
            self.board.goto(new_x, self.board.ycor())

    def check_ball_out_bounds(self):
        if self.ball.ycor() < -280:
            self.scoreboard.lose_life()
            self.ball.reset_position()
            if self.scoreboard.is_game_over():
                self.game_over()

    def check_win_condition(self):
        if self.brick_wall.is_wall_destroyed():
            self.scoreboard.display_winner()
            self.game_is_on = False

    def game_over(self):
        self.scoreboard.display_game_over()
        self.game_is_on = False

    def run(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()

            self.ball.move()

            self.collision_manager.check_wall_collisions()
            self.collision_manager.check_board_collisions()
            self.collision_manager.check_brick_collisions()

            self.check_ball_out_bounds()
            self.check_win_condition()

        self.screen.exitonclick()

if __name__ == "__main__":
    game = Game()
    game.run()