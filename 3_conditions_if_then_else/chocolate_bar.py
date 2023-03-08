"""
Chocolate bar has the form of a rectangle divided into n×m
portions. Chocolate bar can be split into two rectangular parts
by breaking it along a selected straight line on its pattern.
Determine whether it is possible to split it so that one of the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO.
"""

n: int = int(input('n: '))
m: int = int(input('m: '))
k: int = int(input('k: '))

chocolate_bar = n * m
even_n = k % n
even_m = k % m

if k <= chocolate_bar and (even_n == 0 or even_m == 0):
    print("YES")
else:
    print("NO")
