"""
Write a program that reads an integer number and prints its previous and next numbers.
See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
Remember that you can convert the numbers to strings using the function str.
"""

number: int = int(input('Number: '))

previous = number - 1
next = number + 1

print(f'The next number for the number {number} is {next}.')
print(f'The next number for the number {number} is {previous}.')
