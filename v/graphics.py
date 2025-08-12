# Package this code into a class and export it to the trivia one
import turtle as t
left=90
t.reset()

def draw_rectangle(color, width, height): #Draw a rectangle
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(left)
        t.forward(height)
        t.left(left)
    t.end_fill()

t.penup()  #Draw the left green stripe
t.goto(-150, 50)
t.pendown()
draw_rectangle("green", 100, 200)

t.penup() # Draw the white stripe
t.goto(-50, 50)
t.pendown()
draw_rectangle("white", 100, 200)

t.penup()  #Draw the right green stripe
t.goto(50, 50)
t.pendown()
draw_rectangle("green", 100, 200)




#Kenya Flag:

import turtle as t
t. reset() #Setting up the screen
t.penup()
t.goto(-150, 100)
t.pendown() #Drawing first rectangle(in black)
t.fillcolor("black")
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(60)
t.right(90)
t.forward(300)
t.right(90)
t.forward(60)
t.end_fill()

t.right(180)
t.forward(80)
t.left(90)
t.forward(300)
t.left(90)
t.forward(20)
t.right(180)
t. forward(20)

t.fillcolor("red") #Drawing second rectangle(in red)
t.begin_fill()
t.forward(60)
t.right(90)
t.forward(300)
t.right(90)
t.forward(60)
t.end_fill()

t.right(180)
t.forward(60)
t.left(90)
t.forward(300)
t.left(90)
# t.forward(20)
t.right(180)
t. forward(40)

t.fillcolor("green") #Drawing third rectangle(green)
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(300)
t.right(90)
t.forward(60)
t.right(90)
t.forward(300)
t.end_fill()

t.backward(300)
t.left(90)
t.forward(20)



#Rwanda flag

import turtle as t

t.reset() #Clearing the background
t.penup()
t.goto(-150, 100)
t.color("white") #Setting the background
t.pendown()

t.forward(300) #Drawing first rectangle(blue)
t.fillcolor("sky blue")
t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.right(90)
t.forward(100)
t.end_fill()

t.backward(150) #Drawing second rectangle(yellow)
t.right(90)
t.fillcolor("yellow")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(50)
t.left(90)
t.forward(300)
t.left(90)
t.end_fill()

t.forward(100) #Drawing third rectangle(green)
t.left(90)
t.fillcolor("green")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(50)
t.left(90)
t.forward(300)
t.left(90)
t.end_fill()

t.penup() #Drawing the sun
t.goto(100,80)
t.pendown()
t.color("yellow")
for i in range(24):
    t.forward(50)
    t.left(195)

#Scotland

t.reset() #Clearing the screen
t.penup()
t.goto(-200, 100)
t.color("whitesmoke")
t.pendown()

t.fillcolor("steel blue") #Drawing blue rectangle
t.begin_fill()
t.forward(500)
t.right(90)
t.forward(300)
t.right(90)
t.forward(500)
t.right(90)
t.forward(300)
t.end_fill()

t.right(121) #Drawing the white diagonal line
t.color("white")
t.pensize(45)
t.forward(583)
t.left(121)

t.penup() #Drawing the second white diagonal line
t.goto(300,100)
t.left(121)
t.pendown()
t.color("white")
t.pensize(45)
t.forward(583)
