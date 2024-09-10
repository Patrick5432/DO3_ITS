"""
Пример кода с ошибкой № 7
"""


print('Программа для визуализации работы индексов\n')
test_string = 'Тестовая строчка'
print(f'{test_string}\n')

ind_1 = input(
    'Введи первый индекс среза (или нажми Enter - это будет означать, что срез берется с начала строки): '
)
ind_2 = input(
    'Введи второй индекс среза (или нажми Enter - это будет означать, что срез берется до конца строки): '
)
step = input(
    'Введи шаг среза (или нажми Enter - это будет означать, что шаг по-умолчанию равен 1): '
)

# Проверяем, не пустая ли строка в ind_1, ind_2, step. Если нет, то переводим в число эти переменные.
if ind_1:
    ind_1 = int(ind_1)
if ind_2:
    ind_2 = int(ind_2)
if step:
    step = int(step)

# Напиши свой код тут, остальной код не трогай
try:
    if ind_1 > ind_2 or ind_1 > len(test_string) or ind_2 > len(test_string) or ind_1 == False and ind_2 == False:
        raise IndexError("Какая-то фигня у вас с индексами!")
except:
    print("Какая-то фигня у вас с индексами!")
else:
    print('\nТвой срез:')
    if ind_1 and ind_2 and step:
        print(test_string[ind_1:ind_2:step])
    elif (not ind_1) and ind_2 and step:
        print(test_string[:ind_2:step])
    elif ind_1 and (not ind_2) and step:
        print(test_string[ind_1::step])
    elif ind_1 and ind_2 and (not step):
        print(test_string[ind_1:ind_2])
    elif (not ind_1) and (not ind_2) and step:
        print(test_string[::step])
    elif ind_1 and (not ind_2) and (not step):
        print(test_string[ind_1::])
    elif (not ind_1) and ind_2 and (not step):
        print(test_string[:ind_2:])
    else:
        print(test_string[::])
