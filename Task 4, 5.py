"""Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
import collections


def size_group(size):
    """
    e_group(size)
    :param size:
    :return: upper limit half-integral 10
    """
    i = 1
    while size > 0:
        size //= 10
        i *=10
    return i


folder = input('Введите путь к папке: ')
files_dict = collections.defaultdict(int)

try:
    for file in os.listdir(folder):
        if os.path.isfile(f'{folder}\\{file}'):
            file_size = os.path.getsize(f'{folder}\\{file}')

            print(f'{file}: {file_size} < {size_group(file_size)}')
            files_dict[size_group(file_size)] += 1
except Exception as e:
    print(f'Exception: {e}')

print(files_dict)