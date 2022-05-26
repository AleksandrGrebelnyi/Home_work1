# Write a Python program to print the number entered by user only if the
# number entered is negative.

number = int(input())
print((number < 0 and number) or 'Number is not negative')
