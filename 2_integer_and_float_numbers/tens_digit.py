"""
Given an integer. Print its tens digit.
"""

number: int = int(input('Number: '))

tens_digit = repr(number)[-2]

print(tens_digit)