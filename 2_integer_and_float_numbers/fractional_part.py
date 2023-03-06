"""
Given a positive real number, print its fractional part.
"""

number: float = float(input())

fractional = round(number % 1, 3)

print(fractional)