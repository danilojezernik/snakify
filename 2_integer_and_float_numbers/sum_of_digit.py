"""
Given a three-digit number. Find the sum of its digits.
"""

number: int = int(input('Number with 3 digits: '))

three_digit = sum(map(int, str(number)))

print(three_digit)
