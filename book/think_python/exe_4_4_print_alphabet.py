"""This module is exe_4_4 letters.

Remark:
    author's answer: answer/letters.py

"""


import turtle



def line(t, length):
    t.fd(length)
    t.pu()
    t.lt(180)
    t.fd(length)
    t.pd()


def diagonal(t, x, y):
    from math import atan2, pi, sqrt
    angle = atan2(y, x) * 180 / pi  # angle to rad = angle * 180 / pi
    length = sqrt(x * x + y * y)
    t.lt(angle)
    line(t, length)
    t.lt(180 - angle)






if __name__ == "__main__":
    bob = turtle.Turtle()

    font_size = 22

    diagonal(bob, font_size / 2, font_size * 2)


    turtle.mainloop()
