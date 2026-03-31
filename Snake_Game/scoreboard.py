from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        with open(r"\Users\Ordulu\Documents\Python_Course_2\Day20_SnakeGame\highscore.txt", mode="r") as file:
            self.highscore = file.read()

        self.update_score()

    def increase_score(self):

        self.score += 1
        
        if self.score > int(self.highscore):
            self.highscore = str(self.score)
            
            with open(r"\Users\Ordulu\Documents\Python_Course_2\Day20_SnakeGame\highscore.txt", mode="w") as file:
                file.write(self.highscore)

        self.update_score()

        
    def update_score(self):

        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.highscore}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        
        self.score = 0
        self.update_score()
        



        # self.home()
        # self.write("Game over!", align="center", font=("Arial", 10, "normal"))

    
        

        