"""

3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

"""

count = 0
while count <= 5:                                               # не совсем понял, нужен ли был тут ввод для склонений
    percent = int(input("Введите число от 0 до 20: "))          # но реализовал и его тоже
    if percent == 0 or 5 <= percent <= 20:
        print(percent, 'процентов')
    elif percent == 1:
        print(percent, 'процент')
    elif 2 <= percent <= 4:
        print(percent, 'процента')
    else:
        print('Неверный ввод. Введите число от 0 до 20: ')
    count += 1


"""
Вывод всех склонений для проверки
"""

for percent in range(21):
    if percent == 0 or 5 <= percent <= 20:
        print(percent, 'процентов')
    elif percent == 1:
        print(percent, 'процент')
    elif 2 <= percent <= 4:
        print(percent, 'процента')

