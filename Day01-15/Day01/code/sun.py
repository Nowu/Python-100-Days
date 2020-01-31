from turtle import *
from math import pi
from math import sin

length = 100
angle = 360/8

length2 = 2*length*sin(angle/2/180*pi)
angle2 = (180-angle)/2

for i in range(8):
    if i%2 == 0:
        color('red')
    else:
        color('blue')
    begin_fill()

    forward(length)
    left(angle)
    forward(length)
    left(180-angle)
    forward(length)
    left(angle)
    forward(length)
    left(180)
    end_fill()

forward(length)
left(180-angle2)
color('yellow')
begin_fill()
for i in range(8):
    forward(length2)
    left(angle)
end_fill()


exitonclick()
