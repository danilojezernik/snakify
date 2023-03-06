"""
Given a positive real number, print its first digit to the right of the decimal point.
"""

number: float = float(input('Number: '))

first_digit = int((number - int(number)) * 10)

print(first_digit)
