"""
Given three integers, determine how many of them are equal to each other. The program must print one of these numbers:
3 (if all are the same),
2 (if two of them are equal to each other and the third is different) or
0 (if all numbers are different).
"""

a: int = int(input('A: '))
b: int = int(input('B: '))
c: int = int(input('C: '))

if a == b == c:
    print('3')
elif a == b or b == c or c == a:
    print('2')
else:
    print('0')