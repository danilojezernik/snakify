"""
A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks is also enough for the third group of 22 students. So we need 32 desks in total.
"""

s1: int = int(input('No. of students 1: '))
s2: int = int(input('No. of students 2: '))
s3: int = int(input('No. of students 3: '))

tables = (s1 // 2) + (s1 % 2) + (s2 // 2) + (s2 % 2) + (s3 // 2) + (s3 % 2)

print(tables)
