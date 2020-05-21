"""Solution to exe4-3 turtle pies question.

Remark:
    author's answer: answer/pie.py
"""

import math
import turtle


def pie(t, r, base_angle):
    """Draws pie.

    t: Turtle
    r: radius of pie
    base_angle: base angle of pie
    """
    # calculate side length
    # Note. rad to angle = rad * pi / 180
    side = 2 * r * math.cos(base_angle * math.pi / 180)
    
    # draw pie
    t.fd(r)
    t.lt(180 - base_angle)
    t.fd(side)
    t.lt(180 - base_angle)
    t.fd(r)
    t.lt(180)


def polygon(t, r, n):
    """Draws polygon.

    t: Turtle
    r: radius of polygon
    n: shape number of polygon
    """
    central_angle = 360 / n
    base_angle = (180 - central_angle) / 2

    # start drawing direction
    t.lt(central_angle / 2)

    # draws all pies
    for i in range(n):
        pie(t, r, base_angle)

    # return to horizental direction
    t.rt(central_angle / 2)
   

def move(t, length):
    """move the drawing start point.

    t: Turtle
    length: moving distance
    """
    t.pu()
    t.fd(length)
    t.pd()

# 
# main 
# 

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw specified turtle pies
    radius = 80
    move(bob, -200)
    polygon(bob, radius, 5)
    move(bob, 170)
    polygon(bob, radius, 6)
    move(bob, 190)
    polygon(bob, radius, 7)

    turtle.mainloop()
    
