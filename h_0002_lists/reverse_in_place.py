"""
● Через командную строку вводится список из чисел, числа разделены
пробелами. Необходимо развернуть список и вывести как строку, где
числа отделяются друг от друга пробелом.
Обращаю внимание! Список нужно развернуть на месте, т.е. нельзя
создавать дополнительный список и записывать туда элементы в
обратном порядке. (reverse_in_place.py)
ВВОД: 932 856 2 43 -95
ВЫВОД: -95 43 2 856 932
"""
print("Введите целые числа через пробел:")
row = input().split()
list.reverse(row)
s = ''
for i in range(len(row)):
    if i != len(row) - 1:
        s = s + row[i] + " "
    else:
        s = s + row[i]
print(s)