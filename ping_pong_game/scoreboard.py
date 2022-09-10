from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center",font = ("Courier",60,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center",font = ("Courier",60,"normal"))
           
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()
    
    
    def print_results(self,wining_side):
        self.goto(0,120)
        if wining_side == "l":
            self.write("Game Over, Left side won",align="center",font = ("Mono",25,"normal"))
        if wining_side == "r": 
            self.write("Game Over, Right side won",align="center",font = ("Mono",25,"normal"))
            