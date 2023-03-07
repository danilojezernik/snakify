"""
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
"""

dollar: int = int(input('Dollar: '))
cents: int = int(input('Cents: '))
cupcakes: int = int(input('How many cupcakes: '))

total_cost_in_cents = (dollar * 100 + cents) * cupcakes

total_dollars = total_cost_in_cents // 100
total_cent = total_cost_in_cents % 100

print(total_dollars, total_cent)