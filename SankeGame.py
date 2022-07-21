import turtle
import random
import time
import tkinter
import  winsound

delay=0.1
score=0
highestscore=0

bodies=[]

s=turtle.Screen()
s.title("Snake Game")

img = tkinter.Image("photo", file="snakeicon.png")
turtle._Screen._root.iconphoto(True, img)

def gameover():
    winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)

# s.bgcolor("green")
s.bgpic("snake1.png")
s.setup(width=600,height=600)

#Create snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
# head.color("white")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.direction="stop"


#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.color("black")
sb.penup()
sb.ht()
sb.goto(-280,-280)
sb.write("Score: 0  |  HighestScore: 0",font=("Calibri", 18, "bold"))

go=turtle.Turtle()
go.ht()
go.goto(-80,0)


def play():
    winsound.PlaySound('foodsound.wav',winsound.SND_ASYNC)

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
        head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#Event Handling-Key mappings
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")


while True:
    s.update() # to update screen
    go.ht()
    go.clear()

    #check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    #check collision with food
    if head.distance(food)<20:
        # play()
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    #increase the length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")

        bodies.append(body)
        # body.fillcolor("white")
        # body.color("black")
        body.ht()
    #increase the score
        score+=10

        #change delay for increasing speed
        if delay-0.04>=0:
            delay-=0.04

        #change highest score
        if score>highestscore:
            highestscore=score
        sb.clear()
        sb.write("Score: {}  |  HighestScore: {}".format(score,highestscore),font=("Calibri", 18, "bold"))

    for index in range(len(bodies)-1,0,-1):
        # body.fillcolor("white")
        body.color("black")
        body.st()
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        # body.fillcolor("white")
        body.color("black")
        body.st()
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)

    move()

    #check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            gameover()
            go.write("Game Over",font=("Calibri", 30, "bold"))
            time.sleep(1)
            head.home()
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            #update scoreboard
            sb.clear()
            sb.write("Score: {}  |  HighestScore: {}".format(score, highestscore) , font=("Calibri",18, "bold"))

    time.sleep(delay)

s.mainloop()





