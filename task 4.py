"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


    a = calc_cube(5)
125
    a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(func):
    def _val_checker(func2):
        def wrapper(*args, **kwargs):
            for i in args:
                if func(i):
                    pass
                else:
                    raise ValueError(f'wrong val {i}')
            for i in kwargs.values():
                if func(i):
                    pass
                else:
                    raise ValueError(f'wrong val {i}')
            orig_func = func2(*args, **kwargs)
            return orig_func

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(*args, **kwargs):
    try:
        for i in kwargs.values():
            print(i ** 3)
        for i in args:
            print(i ** 3)

    except Exception as e:
        print(e)


# calc_cube(5)
# calc_cube(b=-5)
