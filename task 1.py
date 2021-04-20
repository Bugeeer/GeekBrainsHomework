"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
    email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
    email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
"""
import re

email = input("Введите email: ")


def email_parse(email_adress):
    result_dict = {}
    msg = f'Некорректный email: {email_adress}'
    RE_EMAIL = re.compile(
        r"^((?<!\.)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][A-Za-z0-9!#$%&'*+./=?^_`{|}~-]*)(?<!\.)@((?<![0-9-])[a-zA-Z][a-zA-Z0-9-]*(?<![-])[.][a-zA-Z]+)$")

    if RE_EMAIL.match(email_adress):
        result_dict['username'] = RE_EMAIL.findall(email_adress)[0][0]
        result_dict['domain'] = RE_EMAIL.findall(email_adress)[0][1]
        return (result_dict)
    else:
        raise ValueError(msg)


print(email_parse(email), '\n')
