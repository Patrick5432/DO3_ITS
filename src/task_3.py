"""
Пример кода с ошибкой № 3
"""


string = ' I like administration of hospital   '

exclamation_point ='!'
exclamation_point*=3  # О, кстати популярный метод записи операций - '*=', '+=', '-=' и т.д. Изучи такие записи.

string=string.strip()  # И не стесняйся гуглить неизвестные методы
string= string[:12].upper()

print(f'{string}{exclamation_point} Ох, так неожиданно и прияяятноооо.')

"""
11 строка: неправильно написана команда, которая удаляет по бокам пробелы (stripp()), нужно просто удалить лишний символ (strip())
12 строка: неправильно написана команда, которая все символы, кроме проблеов переделывает под верхние регистры (uppper()), нужно просто удалить лишний символ (upper())
"""