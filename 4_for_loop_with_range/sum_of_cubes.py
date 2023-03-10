"""
For the given integer N calculate the following sum:

1^3 + 2^3 + … + N^3
"""

number: int = int(input('Number: '))

# Variation 1: formula
sum_formula = (number * (number + 1) / 2) ** 2
print(int(sum_formula))

# Variation 2: loop
sum_loop = 0
for i in range(1, number+1):
    sum_loop += i**3

print(sum_loop)