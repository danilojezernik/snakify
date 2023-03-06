"""
A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers?
The program gets two numbers: N and M.
"""

from math import ceil

n: int = int(input('Kilometers per day: '))
m: int = int(input('Route length: '))

total = m / n

print(ceil(total))