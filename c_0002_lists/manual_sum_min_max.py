"""Через командную строку вводится список из целых чисел, числа
разделены пробелами. Преобразовать в список, найти и вывести его
через пробел сумму, максимум, минимум. Использовать ручной перебор,
НЕ использовать встроенные функции. Если какой-то элемент не
является числом, вывести -1. (manual_sum_min_max.py)
ВВОД: 30 -5 0 2
ВЫВОД: 27 30 -5
"""

print("Введите список чисел через пробел:")
string = input()
massive = []
number = ""
# Разделение данных и добавление в массив
for i in range(len(string)):
    if string[i] != " " and i != len(string) - 1:
        number += string[i]
    elif i != len(string) - 1:
        massive.append(number)
        number = ""
    else:
        number += string[i]
        massive.append(number)

# Преобразование частей массива из строкового типа в числовой
notInt = 0
for i in range(len(massive)):
    try:
        massive[i] = int(massive[i])
    # Если не число, то помечаем через переменную
    except ValueError:
        notInt = -1

if notInt == -1:
    print(notInt)
else:
    print(sum(massive), max(massive), min(massive))