# Write a program that calculates and displays the area of a triangle if its sides
# are known

a = 5
b = 7
c = 10
s = (a + b + c / 2)
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area)

# 2ой способ
from math import sqrt
print(sqrt(s * (s - a) * (s - b) * (s - c)))
