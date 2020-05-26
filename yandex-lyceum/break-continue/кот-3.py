"""
Напишите программу, которая находит кота.

Пользователь вводит строки до тех пор, пока он не введёт «СТОП».
Программа выводит, во-первых, общее количество строк, в которых были упомянуты коты,
во-вторых, номер строки, на которой впервые был упомянут кот (в том же смысле, что и в предыдущих задачах),
или -1 (минус один), если кот не был упомянут.

Формат ввода

Несколько строк.
Сигнал остановки — строка «СТОП».

Формат вывода

Всегда два числа — общее количество строк с котом и номер первой такой строки (или -1, если такой строки нет).
Числа должны быть разделены пробелом.

Пример 1

Ввод	                        Вывод
Как устроен типичный фрукт:     1 3
кожура;
мякоть;
косточки.
СТОП

Пример 2

Ввод	                        Вывод
Животное такое.                 0 -1
С усами, хвостом.
Мяукать умеет.
Мышей ловит.
(Если настроение подходящее.)
Кто бы это мог быть?
СТОП
"""

message = ''
first = -1
n = 0
i = 0

while message != 'СТОП':
    i += 1
    message = input()
    if 'кот' in message or 'Кот' in message:
        if first < 0:
            first = i
        n += 1

print(n, first)
