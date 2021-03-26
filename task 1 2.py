"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3


(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

"""

""" C yield"""


def odd_nums(end_num):
    for el in (el for el in range(1, end_num+1) if el % 2 != 0):
        yield el


odd_to_15 = odd_nums(15)

"""Без yield? Такой вариант подходит?"""


def odd_nums(end_num):
    odd_numbers = (el for el in range(1, end_num+1) if el % 2 != 0)
    for number in odd_numbers:
        print(number)


odd_nums(17)
