"""
Chess rook moves horizontally or vertically. Given two different cells of the chessboard,
determine whether a rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell.
The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
"""

x1: int = int(input('x1: '))
y1: int = int(input('y1: '))
x2: int = int(input('x2: '))
y2: int = int(input('y2: '))

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')