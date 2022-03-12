from tkinter import *
import time
import random

class Ball:
    def __init__(self, b_canvas, i_paddle, b_color):
        self.canvas=b_canvas
        self.paddle=i_paddle
        self.id=canvas.create_oval(10, 10, 25, 25, fill = b_color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom=False
             
        
    def reappear(self):
        canvas.itemconfigure(self.id, fill='red')
        
    def detect_hit(self, ballposition):
        global score
        paddle_position=self.canvas.coords(self.paddle.id)
        if ballposition[2] >= paddle_position[1] and ballposition[0] <= paddle_position[2]:
            if ballposition[3] >= paddle_position[1] and ballposition[3] <= paddle_position[3]:
                score = score + 1
                canvas.itemconfigure(score_text, text = "Score: " + str(score))
                canvas.itemconfigure(self.id, fill='#F48024')#make the ball change color
                canvas.after(1000, self.reappear)
                if score==2:
                    self.hit_bottom=True
                    won_text = canvas.create_text(50, 100, anchor="nw", font=("Helvetica", 40), fill="Black", text="You Played Well!")     
                return True
        return False

        

    def draw(self):
        lives_left = 3
        self.canvas.move(self.id, self.x, self.y)
        p=self.canvas.coords(self.id)
        bouncespeed = [-5, -2, -1, 1, 7]
        random.shuffle(bouncespeed)
        if p[1] <= 0:
            self.y=3-bouncespeed[0]
        if p[3] >=self.canvas_height:
            self.hit_bottom=True
            gameover_label = Label(tk, text="Game Over", font=("Helvetica", 20), fg="red3")
            gameover_label.pack()  
        if self.detect_hit(p) == True:
            self.y=-3
        if p[0] <= 0:
            self.x = 3-bouncespeed[0]
        if p[2] >= self.canvas_width:
            self.x=-3-bouncespeed[0]

class Paddle:
    def __init__(self, p_canvas, p_color):
        self.canvas=p_canvas
        self.id=canvas.create_rectangle(0, 0, 100, 10, fill=p_color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        p=self.canvas.coords(self.id)
        if p[0] <= 0:
            self.x=0
        elif p[2] >= self.canvas_width:
            self.x=0

    def turn_left(self, evt):
        self.x =-2
    def turn_right(self, evt):
        self.x=2
        
tk = Tk()
tk.title ("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.create_rectangle(0,0, 500, 290, fill="ghostwhite")
canvas.create_rectangle(0,290, 500, 400, width=0, fill="cornflowerblue")
score = 0
score_text = canvas.create_text(14, 10, anchor="nw", font=("Helvetica", 14), fill="cornflowerblue", text="Score: "+str(score))

canvas.pack()
tk.update()

paddle=Paddle(canvas, "blue")
ball=Ball(canvas, paddle, "red")

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()     
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

