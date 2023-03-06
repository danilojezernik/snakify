"""
Given an integer number, print its last digit.
"""

number: int = int(input('Number: '))

last_digit = number % 10

print(last_digit)