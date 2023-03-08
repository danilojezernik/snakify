"""
Given two integers A and B.
Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.
"""

a: int = int(input('A: '))
b: int = int(input('B: '))

if a < b:
    for i in range(a, b + 1):
        print(i)
elif a >= b:
    for i in range(a, b - 1, -1):
        print(i)
