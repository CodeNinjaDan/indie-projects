from turtle import Turtle
from brick import Brick

class BrickWall:

    def __init__(self):
        self.bricks = []
        self.colors = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "blue", "blue"]
        self.create_wall()

    def create_wall(self):
        for row in range(10):
            for col in range(14):
                x_pos = -350 + (col * 50)
                y_pos = 250 - (row * 20)
                color = self.colors[row] if row < len(self.colors) else "blue"
                brick = Brick(x_pos, y_pos, color)
                self.bricks.append(brick)

    def remove_brick(self, brick):
        if brick in self.bricks:
            brick.destroy()
            self.bricks.remove(brick)
            return brick.points
        return 0

    def check_collision(self, ball):
        for brick in self.bricks:
            if ball.distance(brick) < 25:
                return brick
        return None

    def is_wall_destroyed(self):
        return len(self.bricks) == 0

    def get_brick_count(self):
        return len(self.bricks)
