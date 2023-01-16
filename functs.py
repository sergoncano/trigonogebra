from turtle import *
from math import tan, radians
def tpto(x, y):
    pu()
    setpos(x, y)
    pd()

def draw_tangent(angle, radius, col, backcolor):
    quadrant = ((angle % 360) // 90) + 1
    tangent = tan(radians(angle))*radius
    tphome()
    lt(angle)
    tpfwd(radius)
    rt(90)
    color(col)
    fd(tangent)
    if quadrant == 1 or quadrant == 4:
        seth(180)
    else:
        seth(0)
    color(backcolor)
    fd(abs(xcor())-radius)
    tphome()

def draw_cotangent(angle, radius, col, backcolor):
    quadrant = ((angle % 360) // 90) + 1
    cotangent = (1/(tan(radians(angle))))*radius
    tphome()
    lt(angle)
    tpfwd(radius)
    lt(90)
    color(col)
    fd(cotangent)
    print(quadrant)
    if quadrant == 1 or quadrant == 2:
        seth(270)
    else:
        seth(90)
    color(backcolor)
    fd(abs(ycor())-radius)
    tphome()

def draw_cosec(angle, radius, sin, col, backcol):
    quadrant = ((angle%360) // 90) + 1
    cosec = (1/(sin/radius))*radius
    color(col)
    if quadrant == 1:
        tpto(-radius/5, 0)
        goto(xcor(), cosec)
        color(backcol)
        goto(0, cosec)
        tphome()
    elif quadrant == 2:
        tpto(radius/5, 0)
        goto(xcor(), cosec)
        color(backcol)
        goto(0, cosec)
        tphome()
    elif quadrant == 3:
        tpto(radius/5, 0)
        goto(xcor(), cosec)
        color(backcol)
        goto(0, cosec)
        tphome()
    elif quadrant == 4:
        tpto(-radius/5, 0)
        goto(xcor(), cosec)
        color(backcol)
        goto(0, cosec)
        tphome()

def draw_sec(angle, radius, cos, col, backcol):
    quadrant = ((angle%360) // 90) + 1
    sec = (1/(cos/radius))*radius
    color(col)
    if quadrant == 1:
        tpto(0, -radius/5)
        goto(sec, ycor())
        color(backcol)
        goto(sec, 0)
        tphome()
    elif quadrant == 2:
        tpto(0, -radius/5)
        goto(sec, ycor())
        color(backcol)
        goto(sec, 0)
        tphome()
    elif quadrant == 3:
        tpto(0, radius/5)
        goto(sec, ycor())
        color(backcol)
        goto(sec, 0)
        tphome()
    elif quadrant == 4:
        tpto(0, radius/5)
        goto(sec, ycor())
        color(backcol)
        goto(sec, 0)
        tphome()

def mid_circle(radius):
    tpto(xcor(), ycor() - radius)
    color('black')
    circle(radius)
    home()

def tpfwd(d):
    pu()
    fd(d)
    pd()

def tphome():
    pu()
    home()
    pd()

def line_return(x, y, col):
    ox = xcor()
    oy = ycor()
    color(col)
    goto(x, y)
    tpto(ox, oy)

def draw_quadrants(radius, col):
    x = xcor()
    y = ycor()
    line_return(x, y+radius, col)
    line_return(x, y-radius, col)
    line_return(x+radius, y, col)
    line_return(x-radius, y, col)