# Есть девятиэтажный дом, в котором 4 подъезда. Номер подъезда
# начинается с единицы. На одном этаже 4 квартиры. Напишите
# программу которая, получит номер квартиры с клавиатуры, и
# выведет на экран, на каком этаже, какого подъезда расположена эта
# квартира. Если такой квартиры нет в этом доме, то нужно сообщить
# об этом пользователю.

# Решение в 6 строк
flat = int(input('Enter the number of flat: '))
flat -= 1
entrance = flat // (FLOORS * FLATS_ON_FLOOR) + 1
floor = (flat - (entrance - 1) * FLOORS * FLATS_ON_FLOOR) // FLATS_ON_FLOOR + 1
numbers_flat_on_floor = flat % FLATS_ON_FLOOR + 1
print(flat + 1, '\t', entrance, '\t', floor, '\t', numbers_flat_on_floor)

# Решение задачи в 12 строк
from math import ceil
n = int(input())
if n <= 4*9:
    print(f'flat number {n} is on the entrance 1 and floor is {ceil(n / 4)}')
elif 4*9 < n <= 4*9*2:
    print(f'flat number {n} is on the entrance 2 and floor is {ceil(n / 4) - 9}')
elif 4 * 9* 2 < n <= 4 * 9 * 3:
    print(f'flat number {n} is on the entrance 3 and floor is {ceil(n / 4) - 18}')
elif 4 * 9 * 3 < n <= 4 * 9 * 4:
    print(f'flat number {n} is on the entrance 4 and floor is {ceil(n / 4) - 27}')
else:
    print('There is not such flat in this house')


# Решение задачи в 15 строк
from math import ceil
n = int(input())
if 1 <= n <= 36:
    if n in [12, 16, 20, 24, 28, 32]:
        print(f'Подъезд 1, этаж  {n // 4 + 1}')
    else:
        print(f'Подъезд 1, этаж {ceil(n / 4)}')
elif 36 < n <= 72:
    print(f'Подъезд 2, этаж {ceil(n / 4 - 9)}')
elif 72 < n <= 108:
    print(f'Подъезд 3, этаж {ceil(n / 4 - 18)}')
elif 108 < n <= 144:
    print(f'Подъезд 4, этаж {ceil(n / 4 - 27)}')
else:
    print('Такой кв. нет в доме')
