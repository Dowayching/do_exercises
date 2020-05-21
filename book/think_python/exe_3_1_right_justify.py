"""Align the input string to the right side

"""


def right_justify(s):
    print(' ' * (70 - len(s)) + '%s' %(s))

if __name__ == '__main__':
    right_justify("show me the money")
