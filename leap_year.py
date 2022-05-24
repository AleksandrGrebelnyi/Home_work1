# Определить количество дней в году, который вводит пользователь.
# В високосном году - 366 дней, тогда как в обычном их 365.
# Високосный год определяется по следующему правилу: Год
# високосный, если он делится на четыре без остатка, но если он
# делится на 100 без остатка, это не високосный год. Однако, если он
# делится без остатка на 400, это високосный год

year = int(input('Enter year: '))
days = 366 if not year %4 and year % 100 or not year % 400 else 365
print(days)

year = int(input('Enter year: '))
if (not year % 4) or (not year % 100) and (not year % 400):
    print(year, 'Leap year and has 366 days')
else:
    print(year, 'Common year and has 355 days')
