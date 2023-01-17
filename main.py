from turtle import *
from functs import *
from math import sin, cos, radians


angle = 1
r = 200
Screen().screensize(1500, 1500, 'light gray')
tracer(0,0)
ht()

def triangle(a):
    clear()
    rad = radians(a)
    grey = '#b3b3b3'
    sinus = sin(rad)*r
    cosinus = cos(rad)*r

    speed(0)
    mid_circle(r)
    draw_quadrants(r, grey)


    line_return(cosinus, 0, 'green') #cosinus
    line_return(0, sinus, 'blue') #sinus
    line_return(cosinus, sinus, 'red') #radius


    tpto(0, sinus)
    line_return(cosinus, ycor(), grey)
    tpto(cosinus, 0)
    line_return(xcor(), sinus, grey)
    tpto(0,0)

    draw_tangent(a, r, '#fc21c6', grey)

    draw_cotangent(a, r, 'yellow', grey)

    draw_cosec(a, r, sinus, 'brown', grey)

    draw_sec(a, r, cosinus, 'white', grey)

    update()


while True:
    inp = textinput('Valor del ángulo', '(O introduce cualquier otra cosa para cerrar esta ventana)')
    try:
        triangle(float(inp))
    except:
        break

done()