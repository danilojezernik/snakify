"""
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
"""

a: int = int(input('A: '))
b: int = int(input('B: '))

for i in range(a, b + 1):
    print(i)