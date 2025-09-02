from turtle import Turtle

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(0, -280)

        # Set up key bindings
        screen = self.getscreen()
        screen.listen()
        screen.onkey(self.go_left, "Left")
        screen.onkey(self.go_right, "Right")

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -350:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 350:
            self.goto(new_x, self.ycor())


