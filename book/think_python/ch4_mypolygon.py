"""Turtle module demo
"""

import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, length, angle, n):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    angle = 360 / n
    # refactor
    #for i in range(n):
    #    t.fd(length)
    #    t.lt(angle)
    polyline(t, length, angle, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    # speed the drawing time for unknown r
    n = int(arc_length / 3) + 1
    polyline(t, arc_length / n, angle / n, n)

def circle(t, r):
    # refactor
    #circumference = 2 * math.pi * r
    #n = int(circumference / 3) + 1 
    #polygon(t, circumference / n, n) 
    arc(t, r, 360)

bob = turtle.Turtle()
square(bob, 10)
square(bob, 200)

polygon(bob, 30, 20)

circle(bob, 50)

arc(bob, 150, 232)

turtle.mainloop()


