from turtle import Turtle

# Constants for text alignment and font style
alignment = "center"
font = ("Courier", 24, "normal")

# Scoreboard class definition
class Scoreboard(Turtle):

    # Constructor for the Scoreboard class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Method to update the scoreboard with the current score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=alignment, font=font)

    # Method to display "GAME OVER" on the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=font)

    # Method to increase the player's score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
