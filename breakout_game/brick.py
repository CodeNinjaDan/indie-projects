from turtle import Turtle

class Brick(Turtle):

    def __init__(self, x_pos, y_pos, color="red"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x_pos, y_pos)
        self.points = self.get_points_value(color)

    def get_points_value(self, color):
        points_values = {
            "red": 100,
            "orange": 80,
            "yellow": 60,
            "green": 40,
            "blue": 20
        }
        return points_values.get(color, 50)

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()