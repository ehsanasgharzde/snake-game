from turtle import Turtle


alignment = 'center'
font = ('Courier', 20, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color('white')
        self.goto(0, 290)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Score: {self.score}", False, alignment, font)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, alignment, font)

    def scoretrack(self):
        self.score += 1
        self.undo()
        self.goto(0, 290)
        self.updatescoreboard()
        