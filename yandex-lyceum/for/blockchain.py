"""
Блокчейн (blockchain) переводится как «цепочка блоков».
Это способ хранения данных, защищённый от подделки, используемый, в частности, криптовалютой биткоин.

Блокчейн действительно представляет собой последовательность блоков.
Каждый блок представляет собой некоторую полезную информацию
(в частности, в случае биткоина это список транзакций за определённый период времени —
кто кому когда сколько денег передал), снабжённую случайным числом и некоторыми служебными данными,
в том числе хэшем — числом, которое по определённой формуле зависит от остальной части блока и хэша предыдущего блока.

Хэш должен быть меньше определённого числа. При этом формула, по которой вычисляется хэш, устроена так,
что невозможно получить достаточно маленький хэш иначе, чем перебирая различные значения случайного числа.
Поэтому если злоумышленник решит подделать блокчейн
(и, допустим, вставить в его середину блок с записью о том, что все люди передают ему все свои деньги),
то ему придётся подобрать новое случайное число в новое поддельном блоке и всех последующих
(ведь хэш каждого следующего блока зависит от хэша предыдущего),
что потребует невозможно больших вычислительных мощностей.

Поэтому блокчейн в целом защищён от подобных атак.

Напишите программу, которая проводит проверку правильности хэшей в модельном блокчейне с простой хэш-функцией.

Блок bn с номером n включает:
# полезную информацию mn, представленную натуральным числом,
# rn — случайное число от 0 до 255 и
# hn — хеш (целое число от 0 до 255).
У каждого блока хэш вычисляется по формуле hn = 37×(mn+rn+hn-1) (по модулю 256),
при вычислении хэша начального блока h0 вместо хэша предыдущего блока берётся ноль.

При этом каждый блок представлен одним числом bn = hn + rn×256 + mn×2562.
При этом требуется, чтобы хэш hn был меньше 100.

Формат ввода
На первой строке вводится натуральное число N — количество блоков.
Далее следуют N чисел bn, каждое на отдельной строке.

Формат вывода
Следует вывести номер первого блока, у которого неправильный хэш
(не меньше 100 или не совпадает с вычисленным по указанной в условии формуле),
или -1, если все хэши в блокчейне правильные. Нумерация блоков идёт с нуля, т. е. они имеют номера от 0 до N-1.

Пример 1
Ввод	    Вывод
5           -1
6122802
14406496
15230209
2541121
1758741

Пример 2
Ввод	    Вывод
5           3
1865535
13479687
16689153
1839958
5214020
"""

n = int(input())
hash_previous = 0
hash_correct = True

for i in range(n):
    b = int(input())
    m = b // 256 ** 2
    b -= m * 256 ** 2
    r = b // 256
    hash_current = b - r * 256
    hash_counted = 37 * (m + r + hash_previous) % 256
    if hash_current >= 100 or hash_current != hash_counted:
        hash_correct = not hash_correct
        break
    hash_previous = hash_current

if hash_correct:
    print(-1)
else:
    print(i)
