"""
In chess, the bishop moves diagonally, any number of squares.
Given two different squares of the chessboard,
determine whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8,
specifying the column and row numbers of the starting square and the column and row numbers of the ending square.
The program should output YES if a Bishop can go from the first square to the second in one move, and NO otherwise.
"""

x1: int = int(input('x1: '))
y1: int = int(input('y1: '))
x2: int = int(input('x2: '))
y2: int = int(input('y2: '))

if (x1 - x2) == (y1 - y2):
    print('YES')
else:
    print('NO')