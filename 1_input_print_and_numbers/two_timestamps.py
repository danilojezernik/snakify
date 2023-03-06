"""
A timestamp is three numbers: a number of hours, minutes and seconds.
Given two timestamps, calculate how many seconds is between them.
The moment of the 1_input_print_and_numbers timestamp occurred before the moment of the 2_integer_and_float_numbers timestamp.
"""

h1: int = int(input('h1: '))
m1: int = int(input('m1: '))
s1: int = int(input('s1: '))

h2: int = int(input('h2: '))
m2: int = int(input('m2: '))
s2: int = int(input('s2: '))

seconds = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)

print(seconds)

