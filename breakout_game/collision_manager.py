class CollisionManager:

    def __init__(self, ball, board, brick_wall, scoreboard):
        self.ball = ball
        self.board = board
        self.brick_wall = brick_wall
        self.scoreboard = scoreboard

    def check_wall_collisions(self):
        # Top wall collision
        if self.ball.ycor() > 290:
            self.ball.bounce_y()

        # Left and right wall collisions
        if self.ball.xcor() > 380 or self.ball.xcor() < -380:
            self.ball.bounce_x()

    def check_board_collisions(self):
        if self.ball.distance(self.board) < 50 and self.ball.ycor() > self.board.ycor():
            self.ball.bounce_y()

    def check_brick_collisions(self):
        hit_brick = self.brick_wall.check_collision(self.ball)
        if hit_brick:
            points = self.brick_wall.remove_brick(hit_brick)
            self.scoreboard.increase_score(points)
            self.ball.bounce_y()