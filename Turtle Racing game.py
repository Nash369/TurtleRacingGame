import turtle
import random

screen = turtle.Screen()
screen.setup(700,500)
screen.bgcolor("cyan")
guess = screen.textinput("PREDICTION","Guess which turtle will win?(red, blue, yellow, purple, green)")

#just for the track
track_turtle = turtle.Turtle()
track_turtle.penup()
track_turtle.goto(-325,150)
track_x = -320
track_y = 150
screen.tracer(0)
for track in range(6):
    track_turtle.goto(track_x,track_y)
    for i in range(18):
        track_turtle.pendown()
        track_turtle.fd(20)
        track_turtle.penup()
        track_turtle.fd(20)
    track_y -= 60
track_turtle.hideturtle()
screen.tracer(1)

#for the finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(300,-150)
finish_line.left(90)
screen.tracer(0)
for i in range(12):
    finish_line.pendown()
    finish_line.fd(15)
    finish_line.penup()
    finish_line.fd(10)
finish_line.hideturtle()
screen.tracer(1)

#filling in the turtles
colors = ["red", "blue", "yellow", "purple", "green"]
turtles = []
y_axis = 120
screen.tracer(0)
running = random.randint(30,70)
for i in range(5):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(f"{colors[i]}")
    new_turtle.goto(-290,y_axis)
    turtles.append(new_turtle)
    new_turtle.fd(running)
    y_axis -= 60
screen.tracer(1)

winner = ""
counter = 0
game_on = True
while game_on:
    for each in turtles:
        each.fd(random.randint(1,10))
        if each.xcor() >= 300:
            winner = each.color()[0]
            game_on = False
        counter += 1

#showing the winner
screen.tracer(0)
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.goto(-100,210)
text_turtle.hideturtle()

if guess == winner:
    text_turtle.write(f"You are correct, {winner} is the winner!", font = ("Yo Ghothic",18,"bold"))
else:
    text_turtle.write(f"You are wrong, {winner} was the winner", font = ("Yo Ghothic",18,"bold"))
screen.tracer(1)

##filling = random.choice(colors)
##race_turtle = turtle.Turtle("turtle")
##race_turtle.color(filling)
##track_f = -290
##track_r = 120
##race_turtle.penup()
##race_turtle.goto(track_f,track_r)













