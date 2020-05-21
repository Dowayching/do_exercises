"""This module is for exe_4_2 flowers.

Remark:
    1. add flowers drawing by Anto
    2. remove original circle drawing, polygon, 
       squre functions
    3. Author's answer: answer/flower.py
"""

from __future__ import print_function, division

import math
import turtle


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def leaf(t, r, angle):
    """Draws leaf with the given radius & angle.

    t: Turtle
    r: radius of leaf
    angle: angle of leaf
    """
    arc(t, r, angle)
    bob.lt(180 - angle)
    arc(t, r, angle)
    

def flower(t, r, n, is_overlay):
    """Draw flower.

    t: Turtle
    r: radius of leaf
    n: number of leaf
    is_overlay: True to drawing overlay leaf 
    """
    num = n
    if is_overlay:
        num = int(n / 2)
    angle = 360 / num

    # 2nd run to draw the overlay leaf
    for j in range(2):
        for i in range(num):
            leaf(t, r, angle)
            bob.lt(180)
        if is_overlay:
            bob.lt(angle / 2)
        else:
            break


def next_draw_point(t):
    """Move pointer to the next drawing position.

    t: Turtle
    """
    t.pu()
    t.fd(200) # next drawing distance
    t.pd()


def anto_solution(t):
    """Show Anto's solution to this question.

    t: Turtle
    """
    # set start drawing point
    bob.pu()
    bob.lt(180)
    bob.fd(150)
    bob.rt(180)
    bob.pd()

    # draw 1st flower
    start_draw_angle = 100
    bob.lt(start_draw_angle)
    flower(bob, r = 120, n = 7, is_overlay = False)
    bob.rt(start_draw_angle)

    # draw 2nd flower
    next_draw_point(bob)
    flower(bob, r = 70, n = 10, is_overlay = True)
    bob.rt(360 / (10 / 2)) # 10 = n
    
    # draw 3rd flower
    next_draw_point(bob)
    flower(bob, r = 250, n = 20, is_overlay = False)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    anto_solution(bob)

    # wait for the user to close the window
    turtle.mainloop()
