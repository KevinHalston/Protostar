import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(0)
n = 36
h = 0
r = 6
t.pencolor("red")

for j in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1 / n
    t.pencolor(c)
    t.circle(r + j, 35)
t.penup()
t.goto(110, 10)
t.pendown()

for i in range(17):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1 / n
    t.pencolor(c)
    t.circle(105, 103)
    t.backward(98)
    t.left(60)
    t.circle(70, 68)
    t.left(87)
    t.backward(108)
    t.forward(150)
turtle.done()

