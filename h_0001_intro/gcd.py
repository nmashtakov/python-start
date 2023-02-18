"""
● Вводится через пробел 2 натуральных числа. Вывести НОД чисел (не использовать
встроенные функции) (gcd.py)
ВВОД: 93 42
ВЫВОД: 3
"""
print("Введите два числа через пробел: ")
a = input()
massStr = a.split(" ", 1)
b = int(massStr[0])
c = int(massStr[1])
if max(b,c) % min(b,c) == 0:
    print(c)
    exit()
ostatok = -1

while ostatok != 0:
    NOD = ostatok
    ostatok = max(c,b) % min(c,b)
    b = min(c,b)
    c = ostatok
print(NOD)