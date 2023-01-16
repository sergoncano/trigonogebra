from turtle import *
from functs import *
from math import sin, cos, tan, radians

angle = 4000
r = 200
rad = radians(angle)
grey = '#b3b3b3'
quadrant = ((angle % 360) // 90) + 1
sinus = sin(rad)*r
cosinus = cos(rad)*r
secant = 1/cosinus
cosecant = 1/sinus

ht()
tracer(0,0)
Screen().screensize(1500, 1500, 'light gray')
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

draw_tangent(angle, r, '#fc21c6', grey)

draw_cotangent(angle, r, 'yellow', grey)

draw_cosec(angle, r, sinus, 'brown', grey)

draw_sec(angle, r, cosinus, 'white', grey)

update()

done()
