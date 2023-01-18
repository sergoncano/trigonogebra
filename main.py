from turtle import *
from functs import *
from math import sin, cos, radians


angle = 1
r = 200
Screen().screensize(900, 900, 'white')
tracer(0,0)
ht()
width(2)

def triangle(a):
    clear()
    rad = radians(a)
    
    
    grey = '#b3b3b3'

    sin_col = '#FF9800'
    cos_col = '#DE8E21'
    tan_col = '#CD8D32'

    sec_col = '#2171DE'
    cosec_col = '#0067FF'
    cotan_col = '#3272CD'

    sinus = sin(rad)*r
    cosinus = cos(rad)*r

    speed(0)
    mid_circle(r)
    draw_quadrants(r, grey)

    ta = a%360
    if (ta == 0) or (ta == 90) or (ta == 180) or (ta == 270):
        if ta == 0 or ta == 180:
            line_return(cosinus, 0, cos_col)
            return
        elif ta == 90 or ta == 270:
            line_return(0, sinus, sin_col)
            return


    line_return(cosinus, 0, cos_col) #cosinus
    line_return(0, sinus, sin_col) #sinus
    line_return(cosinus, sinus, grey) #radius


    tpto(0, sinus)
    line_return(cosinus, ycor(), grey)
    tpto(cosinus, 0)
    line_return(xcor(), sinus, grey)
    tpto(0,0)

    draw_tangent(a, r, tan_col, grey)

    draw_cotangent(a, r, cotan_col, grey)

    draw_cosec(a, r, sinus, cosec_col, grey)

    draw_sec(a, r, cosinus, sec_col, grey)

    update()


def up():
    with open('a.txt', 'r') as f:
        val = f.read()
    with open('a.txt', 'w') as f:
        f.write(str(int(val) + 1))
    with open('a.txt', 'r') as f:
        triangle(int(f.read()))

def down():
    with open('a.txt', 'r') as f:
        val = f.read()
    with open('a.txt', 'w') as f:
        f.write(str(int(val) - 1))
    with open('a.txt', 'r') as f:
        triangle(int(f.read()))

def num_input():
    i = numinput('New angle', '')
    open('a.txt', 'w').write(str(int(i)))
    triangle(i)
    Screen().listen()
    
Screen().onkeypress(up, 'Up')
Screen().onkeypress(down, 'Down')
Screen().onkeypress(up, 'w')
Screen().onkeypress(down, 's')
Screen().onkeypress(num_input, 'a')

with open('a.txt', 'w') as f:
        f.write(str(0))
with open('a.txt', 'r') as f:
        triangle(int(f.read()))
        

Screen().listen()
mainloop()