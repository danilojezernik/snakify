"""
Given three integers, print the smallest value.
"""

a: int = int(input('A: '))
b: int = int(input('B: '))
c: int = int(input('C: '))

if a > c and b > c:
    print(c)
elif c > b and a > b:
    print(b)
elif b > a and c > a:
    print(a)