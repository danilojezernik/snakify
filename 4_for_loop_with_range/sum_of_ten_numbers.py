"""
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
"""

print('Numbers should contain spaces between')
numbers = sum(int(num) for num in input('Numbers: ').split())
print(numbers)