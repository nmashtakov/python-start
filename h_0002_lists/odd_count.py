"""
● Через командную строку вводится список целых чисел, числа разделены
пробелами. Посчитать и вывести количество нечетных чисел в массиве.
(odd_count.py)
ВВОД: 66 923 5 8
ВЫВОД: 2
"""
print("Введите целые числа через пробел:")
row = input().split()
intRow = list(map(int, row))
count = 0
for i in range(len(intRow)):
    if intRow[i] % 2 != 0:
        count += 1
print(count)