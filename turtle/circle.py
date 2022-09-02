import turtle
import colorsys
ninja = turtle.Turtle()

ninja.speed(100)
turtle.Screen().bgcolor("black")
ninja.pensize(2)
ninja.speed(0)
n = 36
h = 0
r = 6
ninja.pencolor("red")

for i in range(90):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1 / n
    ninja.pencolor(c)
    ninja.forward(20)
    ninja.right(50)
    ninja.forward(20)
    ninja.left(50)
    ninja.forward(20)
    ninja.right(50)
    ninja.forward(20)
    ninja.left(50)
    ninja.forward(20)
    ninja.left(50)
    ninja.forward(20)
    ninja.right(50)
    ninja.forward(20)
    ninja.left(50)
    ninja.forward(20)
    ninja.left(50)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)

turtle.done()