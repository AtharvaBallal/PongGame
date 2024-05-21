from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, cordinate):
        super().__init__()

        self.cordinate = cordinate
        self.screen = Screen()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.cordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# screen.listen()
#
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
