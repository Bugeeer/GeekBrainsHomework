"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2')
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
"""


ngnx_log = open(r'nginx_logs.txt', 'r', encoding = 'utf-8')
content = ((i.split()[0], i.split()[5][1:], i.split()[6]) for i in ngnx_log)
for a in content:
    print(a)


with open(r'nginx_logs.txt', 'r', encoding = 'utf-8') as f:
    my_dict = {}
    content_t2 = (line.split()[0] for line in f)
    for i in content_t2:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

sorted_keys = sorted(my_dict, key=my_dict.get)
print(f'Спамер {sorted_keys[-1]} - {my_dict[sorted_keys[-1]]} раз')
