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


while True:
    inp = textinput('Valor del ángulo', '(O introduce cualquier otra cosa para cerrar esta ventana)')
    try:
        triangle(float(inp))
    except:
        bye()
done()