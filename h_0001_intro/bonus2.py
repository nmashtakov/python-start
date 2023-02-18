"""
● Вводится натуральное число. Проверить его на простоту (вывести True
или False)
ВВОД: 13
ВЫВОД: True
"""

print("Введите натуральное число: ")
number = int(input())
for i in range (2, number):
    if number % i == 0:
        print("True")
        exit()