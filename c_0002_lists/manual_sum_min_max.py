"""
Через командную строку вводится список из целых чисел, числа
разделены пробелами. Преобразовать в список, найти и вывести его
через пробел сумму, максимум, минимум. Использовать ручной перебор,
НЕ использовать встроенные функции. Если какой-то элемент не
является числом, вывести -1. (manual_sum_min_max.py)

ВВОД: 30 -5 0 2
ВЫВОД: 27 30 -5
"""
print("Введите список чисел через пробел:")
try:
    l = input().split()
    intL = list(map(lambda x: int(x), l))
    print(sum(intL), max(intL), min(intL))
except ValueError:
    print(-1)