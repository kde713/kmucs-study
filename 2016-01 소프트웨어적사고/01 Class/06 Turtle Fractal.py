import turtle


def preptree(length, angl, decVal, spd):
    t = turtle.Turtle()
    t.speed(spd)
    t.penup()
    t.sety(50 - length * 1.5)
    t.left(90)
    t.pendown()
    drawtree(t, length, angl, decVal)


def drawtree(t, length, angl, decVal):
    if length > 0:
        t.forward(length)
        t.left(angl)
        drawtree(t, length - decVal, angl, decVal)
        t.right(angl * 2)
        drawtree(t, length - decVal, angl, decVal)
        t.left(angl)
        t.backward(length)


def snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        snowflake(t, length/3, depth-1)
        t.right(60)
        snowflake(t, length/3, depth-1)
        t.left(120)
        snowflake(t, length/3, depth-1)
        t.right(60)
        snowflake(t, length/3, depth-1)



#preptree(16, 15, 1, 'fastest')
t = turtle.Turtle()
t.speed('fastest')
snowflake(t, 500, 1)
