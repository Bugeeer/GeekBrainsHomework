
"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""

duration = int(input('Введите продолжительность в секундах: '))
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
minutes = duration // 60
hours = duration // 3600
days = duration // 86400

if duration > seconds_in_minute:
    if minutes >= minutes_in_hour:
        if hours >= hours_in_day:
            print(days, 'дн', hours % hours_in_day, 'час', minutes % minutes_in_hour, 'мин', duration % seconds_in_minute, 'сек')
        else:
            print(hours, 'час', minutes % minutes_in_hour, 'мин', duration % seconds_in_minute, 'сек')
    else:
        print(minutes, 'мин', duration % seconds_in_minute, 'сек')
else:
    print(duration, 'сек')
