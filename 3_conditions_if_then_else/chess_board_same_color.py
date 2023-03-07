"""
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell.
"""

x1: int = int(input('x1: '))
y1: int = int(input('y1: '))
x2: int = int(input('x2: '))
y2: int = int(input('y2: '))

white_one = 'white'

if x1 % 2 == 0 and y1 % 2 == 0:
    white_one = 'black'
elif x1 % 2 == 1 and y1 % 2 == 1:
    white_one = 'black'

white_two = 'white'

if x2 % 2 == 0 and y2 % 2 == 0:
    white_two = 'black'
elif x2 % 2 == 1 and y2 % 2 == 1:
    white_two = 'black'

if white_one == white_two:
    print('YES')
else:
    print('NO')