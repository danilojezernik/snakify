"""
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.
"""

year: int = int(input('Year: '))

leap_check = year % 4
four_hundred = year % 400
one_hundred = year % 100

if leap_check == 0 and four_hundred == 0 or one_hundred == 1:
    print('LEAP')
else:
    print('COMMON')