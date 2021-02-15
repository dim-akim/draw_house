"""
Системный администратор раз в неделю создаёт архив пользовательских файлов.
Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов.
Известно, какой объём занимает файл каждого пользователя.

По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске
определите максимальное число пользователей, чьи файлы можно сохранить в архиве,
а также максимальный размер имеющегося файла, который может быть сохранён в архиве,
при условии, что сохранены файлы максимально возможного числа пользователей.

Входные данные (файл 26_demo.txt)

В первой строке входного файла находятся два числа:
S — размер свободного места на диске (натуральное число, не превышающее 10 000)
N — количество пользователей (натуральное число, не превышающее 1000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.

Запишите в ответе два числа:
сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив,
затем максимальный размер имеющегося файла, который может быть сохранён в архиве,
при условии, что сохранены файлы максимально возможного числа пользователей.

Пример входного файла:

100 4
80
30
50
40

При таких исходных данных можно сохранить файлы максимум двух пользователей.
Возможные объёмы этих двух файлов 30 и 40, 30 и 50 или 40 и 50.
Наибольший объём файла из перечисленных пар — 50, поэтому ответ для приведённого примера:

2 50
"""

with open('26_demo.txt') as file:
    s, n = [int(i) for i in file.readline().strip('\n').split()]
    data = [int(line.strip('\n')) for line in file]
    data.sort()
    summa = 0
    for i in range(n):
        if summa + data[i] <= s:
            summa += data[i]
        else:
            break
    count = i
    max_num = data[i]
    print(i, data[i], s, s - summa + data[i])
    # for i in range(i, n):
