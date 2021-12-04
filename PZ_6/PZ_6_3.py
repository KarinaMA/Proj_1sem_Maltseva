# Дано множество A и N точек (N>2, точки заданы своими координатами х, у).
# Найти такую точку из данного множества, сумма расстояний от которой до остальных
# его точек минимальна, и сам эту сумму.
# Расстояние R мужду точками с координатами (x1,y1) и (x2,y2) вычисляется по формуле:
#                              R=√(x2-x1)^2+(y2-y1)^2.
# Для хранения данных о каждом наборе точек следует использовать по два списка:
# первый список для хранения абсцисс, второй- для хранения ординат.

import math


def get_r(x1, x2, y1, y2):  # функция для поиска расстояния между точками
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x_coords = [1, 3, 5, 2]
y_coords = [5, 2, 9, 10]

# Промежуточная переменная, для хранения данных и сумм
sum_dict = []

for x1, y1 in zip(x_coords, y_coords):
    # Ищем расcтояния от точек
    r_sum = 0  # тут будет хранится сумма расcтояний
    for x2, y2 in zip(x_coords, y_coords):
        # До точек
        r_sum += get_r(x1, y1, x2, y2)
    sum_dict.append(r_sum)

min_sum = min(sum_dict)
index_min_sum = sum_dict.index(min_sum)
print(f'Минимальная сумма расcтояний: {min_sum}.\n '
      f'Точка с координатами \n'
      f'х = {x_coords[index_min_sum]}\n'
      f'y = {y_coords[index_min_sum]}')
