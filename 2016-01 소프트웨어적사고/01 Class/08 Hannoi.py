## Not Finished


import turtle
import random


turtle.colormode(255)


class Disc(turtle.Turtle):
    def __init__(self, n):
        turtle.Turtle.__init__(self, shape="square", visible=False)
        self.penup()
        self.sety(100)
        self.shapesize(1.5, n * 1, 2)
        self.fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.speed("fast")
        self.showturtle()


class Tower(list):
    def __init__(self, x, h):
        self.x = x
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.shape('square')
        t.setpos(self.x, -60)
        t.shapesize(h, 1, 2)
        t.fillcolor('blue')
        t.showturtle()
        self.t = t

    def push(self, d):
        d.setx(self.x)
        d.sety(-150 + 34 * len(self))
        self.append(d)

    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d


def hannoi(n, from_, to_, with_):
    tw = [Tower(-300, n*2.5), Tower(0, n*2.5), Tower(300, n*2.5)]
    for j in range(n, 0, -1):
        tw[0].push(Disc(j))
    input()


hannoi(8, 0,0,0)
