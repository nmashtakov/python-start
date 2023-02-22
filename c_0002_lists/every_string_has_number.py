"""
Через командную строку вводится список строк, строки разделены пробелами.
Вывести yes, если в каждой строке содержится хотя бы одна цифра, иначе
вывести no. (every_string_has_number.py)
ВВОД: erdf3dfs dfas klfs21 343
ВЫВОД: no
"""
print("Введите список строк через запятую:")
string = input().split()
flag = 0
for i in range(len(string)):
    x = string[i].find("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0")
    if x == -1:
        flag += 1
        break
if flag == 0:
    print("yes")
else:
    print("no")