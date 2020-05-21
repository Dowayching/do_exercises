"""Print input string for multiple times by function call

Remark:
    refer to answer/do_four for author's answer
"""

def do_twice(f, val):
    f(val)
    f(val)

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
do_four(print_twice, 'show')
