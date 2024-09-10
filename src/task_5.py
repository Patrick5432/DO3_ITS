"""
Пример кода с ошибкой № 5
"""
from random import randint  # И опять повод загуглить незнакомый модуль
import math

input_number = int(input('Введите целое число от -10 до 10: '))

random_number = randint(-10, 10)
print(f'Случайное число = {random_number}')

difference_numbers = input_number - random_number
print(f'{input_number} - ({random_number}) = {difference_numbers}')
try:
    sqlt_number = round(math.sqrt(difference_numbers), 2)
    print(f'Корень из {difference_numbers} = {sqlt_number}')
except ValueError:
    print("Корень из отрицательного числа брать нельзя!")

"""
5 строка: непраивльно написана библиотека (mathh), нужно удалить один символ, чтобы работало правильно (math)
"""