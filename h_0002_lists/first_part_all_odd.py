"""
● Через командную строку вводится список целых чисел, числа разделены
пробелами. Вывести yes, если в первой половине списка (index < len(lst)
// 2) существует хотя бы одно число с чётным индексом в списке, в
котором ВСЕ ЦИФРЫ нечётные. Иначе вывести no.
Внимание! Каждое число необходимо преобразовать в int, проверку
чётности каждой цифры выполнять уже с преобразованным типом!
(first_part_all_odd.py)
ВВОД: 357 981 444
ВЫВОД: yes
"""
def odd_number(x):
    count_def = 0
    temporary = x
    while temporary != 0:
        number = temporary % 10
        if number % 2 == 1:
            count_def += 1
            temporary = temporary // 10
        else:
            temporary = temporary // 10
    if count_def == len(str(x)):
        return 1
    else:
        return 0


print("Введите целые числа через пробел:")
row = input().split()
intRow = list(map(int, row))
count = 0
for i in range(0, len(intRow) // 2, 2):
    if odd_number(intRow[i]) == 1:
        count += 1

if count > 0:
    print("yes")
else:
    print("no")