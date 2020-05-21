"""Print specified grids  contains "+ - |" with
   input grid numbers.

Remark:
    refer to answer answer/grid.py for author's answer.
"""

def print_grid(row, col):
    horizental_line = ('+ ' + '- ' * 4) * col + '+\n'
    vertical_block = (('|' + ' ' * 9) * col + '|\n') * 4
    one_row = horizental_line + vertical_block
    full_grid = one_row * row + horizental_line
    print(full_grid)


print_grid(2, 2)
print("")
print_grid(4, 4)

