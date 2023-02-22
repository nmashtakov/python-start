"""
● Аналогично предыдущему, НО решить и использованием слайсов и
встроенных функций. (slices_hard_indexing_sum_min_max.py)
ВВОД: 30 -5 0 2
ВЫВОД: 30 30 0
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
massive = massive[slice(None, None, 2)]
newMassive = []

for i in range(len(massive)):
    try:
        if i <= len(massive):
            newMassive.append(int(massive[i]))
    # Если не число, то помечаем через переменную
    except ValueError:
        notInt = -1

if notInt == -1:
    print(notInt)
else:
    print(sum(newMassive), max(newMassive), min(newMassive))